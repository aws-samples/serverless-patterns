#!/usr/bin/env python3
"""SQS load generator for the LMI-to-Lambda overflow pattern.

Sends messages at a target rate for a fixed duration and reports the rate actually
achieved. Use it to hold a steady baseline, then to apply a burst on top.

    # 20 minutes of steady baseline
    ./load_generator.py --queue-url "$QUEUE_URL" --rate 25 --duration 1200

    # 20 minutes of 10x burst -- long enough for LMI to scale through it
    ./load_generator.py --queue-url "$QUEUE_URL" --rate 300 --duration 1200

    # the same burst, but arriving the way real traffic does
    ./load_generator.py --queue-url "$QUEUE_URL" --rate 275 --duration 1200 \
        --ramp-up-seconds 60 --ramp-down-seconds 60 --jitter poisson

The duration matters more than people expect. LMI's managed scaler adds roughly 2x
capacity per five minutes, so a 10x burst needs about 17 minutes before LMI alone can
carry it. A two-minute burst only ever demonstrates the burst tier.

Two flags exist because evenly paced arrivals are not what production looks like, and
both of them change what the test proves:

--jitter poisson   Draws each inter-batch gap from an exponential distribution with the
                   same mean. The average rate is unchanged, but the queue depth now
                   wanders the way a real backlog does, so a depth threshold can be
                   crossed by noise rather than by a genuine trend. Even pacing hides
                   that failure mode entirely.
--ramp-*-seconds   Ramps the rate linearly in and out instead of stepping. An instant
                   step crosses the open threshold within seconds, which makes detector
                   latency look like the only thing that matters. Under a ramp the
                   crossing is gradual and the close logic gets tested as well.
"""

import argparse
import json
import random
import sys
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor

import boto3
from botocore.config import Config

# How far the send schedule may fall behind before the missed batches are abandoned rather
# than sent late. Generous enough to absorb ordinary send latency, short enough that a
# suspended laptop or a dropped network cannot turn into a fake spike.
MAX_LAG_SECONDS = 5.0


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue-url", required=True)
    parser.add_argument(
        "--rate", type=float, required=True, help="Target messages per second."
    )
    parser.add_argument(
        "--duration", type=float, required=True, help="Seconds to sustain the rate."
    )
    parser.add_argument("--region", default=None)
    parser.add_argument(
        "--senders",
        type=int,
        default=0,
        help="Sender threads. Default: one per 100 msg/s, minimum 4.",
    )
    parser.add_argument(
        "--label",
        default="load",
        help="Included in each message body so you can tell runs apart in the logs.",
    )
    parser.add_argument(
        "--jitter",
        choices=("none", "poisson"),
        default="none",
        help="Arrival process. poisson gives the same mean rate with realistic clumping.",
    )
    parser.add_argument(
        "--ramp-up-seconds",
        type=float,
        default=0.0,
        help="Ramp linearly from near zero to --rate over this many seconds.",
    )
    parser.add_argument(
        "--ramp-down-seconds",
        type=float,
        default=0.0,
        help="Ramp linearly back down to near zero over the final seconds.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Seed for --jitter poisson, so a run can be repeated exactly.",
    )
    return parser.parse_args()


def rate_at(elapsed, args):
    """Instantaneous target rate, honouring the ramps.

    Floored at 2% of the target so the ramp's first instant does not ask for an
    infinite inter-batch gap.
    """
    floor = args.rate * 0.02
    if args.ramp_up_seconds and elapsed < args.ramp_up_seconds:
        return max(floor, args.rate * elapsed / args.ramp_up_seconds)
    remaining = args.duration - elapsed
    if args.ramp_down_seconds and remaining < args.ramp_down_seconds:
        return max(floor, args.rate * remaining / args.ramp_down_seconds)
    return args.rate


def expected_messages(args):
    """A ramp delivers half the messages a plateau of the same length would."""
    plateau = args.duration - args.ramp_up_seconds - args.ramp_down_seconds
    return args.rate * (plateau + (args.ramp_up_seconds + args.ramp_down_seconds) / 2)


class Counter:
    def __init__(self):
        self._lock = threading.Lock()
        self.sent = 0
        self.failed = 0

    def add(self, sent, failed):
        with self._lock:
            self.sent += sent
            self.failed += failed


def send_batch(sqs, queue_url, label, size, counter):
    entries = [
        {
            "Id": str(index),
            "MessageBody": json.dumps(
                {
                    "workItemId": str(uuid.uuid4()),
                    "label": label,
                    "operation": "process",
                    "createdAt": int(time.time() * 1000),
                }
            ),
        }
        for index in range(size)
    ]
    try:
        response = sqs.send_message_batch(QueueUrl=queue_url, Entries=entries)
        failed = len(response.get("Failed", []))
        counter.add(size - failed, failed)
    except Exception as error:  # noqa: BLE001 - a load generator should keep going
        print(f"batch failed: {error}", file=sys.stderr)
        counter.add(0, size)


def main():
    args = parse_args()
    senders = args.senders or max(4, int(args.rate // 100) + 1)

    sqs = boto3.client(
        "sqs",
        region_name=args.region,
        config=Config(
            max_pool_connections=senders * 2,
            retries={"max_attempts": 3, "mode": "standard"},
        ),
    )

    # SendMessageBatch takes at most 10 entries. Pace by batch rather than by message so
    # the generator itself is not the bottleneck at high rates.
    batch_size = 10 if args.rate >= 10 else 1
    expected = expected_messages(args)
    rng = random.Random(args.seed)

    counter = Counter()
    started = time.monotonic()
    shape = []
    if args.ramp_up_seconds:
        shape.append(f"ramp up {args.ramp_up_seconds:g}s")
    if args.ramp_down_seconds:
        shape.append(f"ramp down {args.ramp_down_seconds:g}s")
    if args.jitter != "none":
        shape.append(f"{args.jitter} arrivals")
    print(
        f"sending ~{args.rate:g} msg/s for {args.duration:g}s "
        f"({expected:.0f} messages in batches of {batch_size}, {senders} threads"
        + (", " + ", ".join(shape) if shape else "")
        + ")"
    )

    # The rate varies, so the schedule is built as it is walked rather than precomputed.
    # `target` accumulates the intended send times, which keeps the mean rate honest even
    # when an individual send runs slow.
    with ThreadPoolExecutor(max_workers=senders) as pool:
        target = started
        next_report = 30.0
        skipped = 0
        while True:
            elapsed = target - started
            if elapsed >= args.duration:
                break
            delay = target - time.monotonic()
            if delay > 0:
                time.sleep(delay)
            elif delay < -MAX_LAG_SECONDS:
                # The schedule is further behind than any send could explain: the host was
                # suspended, or the network went away. Firing the whole missed backlog now
                # would inject a spike the test never asked for and would look exactly like
                # the burst under test, so drop those batches and resynchronise.
                skipped += 1
                target = time.monotonic()
                continue
            pool.submit(
                send_batch, sqs, args.queue_url, args.label, batch_size, counter
            )

            interval = batch_size / rate_at(elapsed, args)
            if args.jitter == "poisson":
                # Exponential gaps: same mean, but arrivals clump the way real ones do.
                interval = rng.expovariate(1.0 / interval)
            target += interval

            if elapsed >= next_report:
                next_report += 30.0
                actual = time.monotonic() - started
                print(
                    f"  t+{actual:6.1f}s  sent={counter.sent:<8} "
                    f"failed={counter.failed:<6} target={rate_at(elapsed, args):5.0f}/s "
                    f"achieved={counter.sent / actual:6.1f}/s"
                )

    elapsed = time.monotonic() - started
    print(
        f"done: sent={counter.sent} failed={counter.failed} "
        f"elapsed={elapsed:.1f}s achieved={counter.sent / elapsed:.1f} msg/s"
    )
    if skipped:
        print(
            f"WARNING: dropped {skipped} batch(es) after falling more than "
            f"{MAX_LAG_SECONDS:g}s behind schedule. The host was suspended or the network "
            "went away, so this run has a gap in the arrival rate. Do not report its "
            "timings.",
            file=sys.stderr,
        )
        return 1
    if counter.sent < expected * 0.95:
        print(
            "WARNING: the generator did not keep up with the target rate. "
            "Raise --senders or run it from an EC2 instance in the same Region.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
