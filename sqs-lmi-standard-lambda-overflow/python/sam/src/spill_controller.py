"""Opens and closes the Standard Lambda burst tier from live queue depth.

This runs on the control plane, not the data path: it never sees a workload message. It
reads the work queue's depth with `GetQueueAttributes` and toggles the `Enabled` flag of
the burst event source mapping.

Why `GetQueueAttributes` rather than a CloudWatch alarm on
`ApproximateNumberOfMessagesVisible`: the metric is published by SQS on a one-minute
grain, and the end-to-end publish-plus-alarm-evaluation lag measured on this pattern was
2m 15s -- roughly half of the total time to engage the burst tier, and the single largest
term in it. `GetQueueAttributes` reads live queue state, so the same threshold decision
costs one API call. Detection drops to POLL_INTERVAL_SECONDS.

The trade is that a schedule is the coarsest clock EventBridge offers, and its floor is
one minute. So each invocation polls in a loop for most of a minute and then exits,
leaving the next scheduled invocation to pick up. Set POLL_INTERVAL_SECONDS to 0 for a
single poll per minute, which costs almost nothing but puts detection back at up to 60s.

Every invocation reads current state and converges on the correct valve position, so
overlapping invocations, a missed schedule, and a stack redeploy are all safe.

Two thresholds rather than one give a dead band. Above SPILL_OPEN_DEPTH the burst tier
opens, below SPILL_CLOSE_DEPTH it closes, and in between the current position is held.
A single threshold would flap around it.
"""

import datetime
import json
import logging
import os
import time

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

lambda_client = boto3.client("lambda")
sqs = boto3.client("sqs")

BURST_UUID = os.environ["BURST_EVENT_SOURCE_MAPPING_UUID"]
WORK_QUEUE_URL = os.environ["WORK_QUEUE_URL"]
SPILL_OPEN_DEPTH = int(os.environ["SPILL_OPEN_DEPTH"])
SPILL_CLOSE_DEPTH = int(os.environ["SPILL_CLOSE_DEPTH"])
POLL_INTERVAL_SECONDS = int(os.environ.get("POLL_INTERVAL_SECONDS", "10"))
CLOSE_TREND_WINDOW_SECONDS = int(os.environ.get("CLOSE_TREND_WINDOW_SECONDS", "30"))
MINIMUM_DWELL_SECONDS = int(os.environ.get("MINIMUM_DWELL_SECONDS", "300"))
METRIC_NAMESPACE = os.environ["METRIC_NAMESPACE"]

# Stop polling with this much of the invocation left, so that a decision taken on the
# last poll still has time to complete its UpdateEventSourceMapping call.
#
# Keep this small. Every second reserved here is a second of the minute in which nothing
# is watching the queue, because the next invocation cannot start early. At 10s this
# guard cost a whole poll: with a 60s timeout and a 10s interval the loop covered 40.5s
# of every 60, measured, leaving a 19.5s blind window. UpdateEventSourceMapping is a
# single control-plane call that returns in well under a second.
RESERVED_MILLIS = 3_000

# States the mapping passes through mid-update. Acting on one of these would race the
# in-flight change.
TRANSITIONAL_STATES = {"Creating", "Enabling", "Disabling", "Updating", "Deleting"}

ACTED = {"opened-burst-tier", "closed-burst-tier"}


def queue_depth():
    """Live visible and in-flight message counts.

    Both numbers are approximate -- SQS is distributed, and a count taken across its
    partitions is a snapshot rather than a transaction. It is approximate in the same way
    the CloudWatch metric is, but without the minutes of publish lag.
    """
    response = sqs.get_queue_attributes(
        QueueUrl=WORK_QUEUE_URL,
        AttributeNames=[
            "ApproximateNumberOfMessages",
            "ApproximateNumberOfMessagesNotVisible",
        ],
    )
    attributes = response["Attributes"]
    return (
        int(attributes["ApproximateNumberOfMessages"]),
        int(attributes["ApproximateNumberOfMessagesNotVisible"]),
    )


def depth_trend(samples):
    """Change in visible depth per second, or None if the window is not yet covered.

    This is the term a depth-only close condition is missing. Depth dipping below the
    close threshold says nothing about whether it is on its way down or on its way back
    up; the slope does. Returning None until the samples span
    CLOSE_TREND_WINDOW_SECONDS keeps a slope from being read off two adjacent samples of
    an approximate counter, which is mostly noise.

    Samples do not carry across invocations, so the window has to fit inside one poll
    loop. A window of 0 disables the check and restores a depth-only close, which is the
    only sensible setting when POLL_INTERVAL_SECONDS is 0 -- a single poll can never
    establish a slope, so the tier would otherwise never close.
    """
    if CLOSE_TREND_WINDOW_SECONDS <= 0:
        return 0.0
    if len(samples) < 2:
        return None
    first_at, first_depth = samples[0]
    last_at, last_depth = samples[-1]
    elapsed = last_at - first_at
    if elapsed < CLOSE_TREND_WINDOW_SECONDS:
        return None
    return (last_depth - first_depth) / elapsed


def desired_state(visible, trend):
    """Return True to open the burst tier, False to close it, None to hold."""
    if visible >= SPILL_OPEN_DEPTH:
        # Opening is unconditional and immediate. There is no trend requirement: by the
        # time depth is this high the deficit is established, and every second spent
        # confirming it is a second of backlog.
        return True
    if visible <= SPILL_CLOSE_DEPTH:
        if trend is None:
            # Not enough history in this invocation yet.
            return None
        if trend > 0:
            # Below the close threshold, but the backlog is still growing. Closing here
            # is what produces a reopen a minute later.
            return None
        return False
    # Inside the dead band.
    return None


def emit_state_metric(enabled):
    print(
        json.dumps(
            {
                "_aws": {
                    "Timestamp": int(time.time() * 1000),
                    "CloudWatchMetrics": [
                        {
                            "Namespace": METRIC_NAMESPACE,
                            "Dimensions": [[]],
                            "Metrics": [{"Name": "BurstTierOpen", "Unit": "Count"}],
                        }
                    ],
                },
                "BurstTierOpen": 1 if enabled else 0,
            }
        )
    )


def seconds_since(last_modified):
    if not isinstance(last_modified, datetime.datetime):
        return None
    now = datetime.datetime.now(tz=last_modified.tzinfo or datetime.timezone.utc)
    return (now - last_modified).total_seconds()


def evaluate(samples):
    """One poll: read depth and mapping state, decide, and act if a change is due."""
    visible, in_flight = queue_depth()
    samples.append((time.monotonic(), visible))
    trend = depth_trend(samples)
    target = desired_state(visible, trend)

    mapping = lambda_client.get_event_source_mapping(UUID=BURST_UUID)
    mapping_state = mapping.get("State")
    currently_enabled = mapping_state == "Enabled"

    decision = {
        "visibleDepth": visible,
        "inFlight": in_flight,
        "depthTrendPerSecond": None if trend is None else round(trend, 1),
        "mappingState": mapping_state,
        "desired": target,
        # The position the valve is in when this poll returns. Every early return below
        # leaves it unchanged; only a successful update overwrites it.
        "burstTierOpen": currently_enabled,
    }

    if mapping_state in TRANSITIONAL_STATES:
        decision["action"] = "wait-for-transition"
        return decision

    if target is None:
        decision["action"] = "hold-dead-band"
        return decision

    if target == currently_enabled:
        decision["action"] = "already-in-desired-state"
        return decision

    if target is False:
        # Closing early is the expensive mistake. LMI needs roughly five minutes per
        # doubling, so removing the relief valve as soon as the backlog dips can send
        # the queue straight back through the open threshold.
        elapsed = seconds_since(mapping.get("LastModified"))
        if elapsed is not None and elapsed < MINIMUM_DWELL_SECONDS:
            decision["action"] = "hold-minimum-dwell"
            decision["secondsOpen"] = round(elapsed)
            decision["minimumDwellSeconds"] = MINIMUM_DWELL_SECONDS
            return decision

    try:
        lambda_client.update_event_source_mapping(UUID=BURST_UUID, Enabled=target)
    except ClientError as error:
        if error.response["Error"]["Code"] == "ResourceConflictException":
            # An overlapping invocation is already applying an update. The next poll
            # will see the result and converge.
            decision["action"] = "conflict-retry-next-poll"
            return decision
        raise

    decision["action"] = "opened-burst-tier" if target else "closed-burst-tier"
    decision["burstTierOpen"] = target
    return decision


def lambda_handler(event, context):
    samples = []
    decision = None

    while True:
        decision = evaluate(samples)
        logger.info(json.dumps(decision))
        emit_state_metric(decision["burstTierOpen"])

        if decision["action"] in ACTED:
            # The mapping is now transitional, so further polls in this invocation would
            # only log wait-for-transition. Exit and let the next schedule take over.
            break
        if POLL_INTERVAL_SECONDS <= 0:
            # Single-poll mode: detection is bounded by the one-minute schedule instead.
            break
        if context.get_remaining_time_in_millis() < (
            RESERVED_MILLIS + POLL_INTERVAL_SECONDS * 1000
        ):
            break
        time.sleep(POLL_INTERVAL_SECONDS)

    if (
        decision["burstTierOpen"]
        and decision["action"] not in ACTED
        and decision["depthTrendPerSecond"] is None
    ):
        # The loop ran out of invocation before the trend window closed, so no close
        # decision was ever possible. Left unnoticed this welds the valve open at
        # on-demand Lambda rates. SpillCloseTrendWindowSeconds is too large for
        # ControllerPollIntervalSeconds and the 60-second timeout.
        logger.warning(
            json.dumps(
                {
                    "action": "misconfigured-trend-window",
                    "closeTrendWindowSeconds": CLOSE_TREND_WINDOW_SECONDS,
                    "pollIntervalSeconds": POLL_INTERVAL_SECONDS,
                    "samplesTaken": len(samples),
                }
            )
        )

    return decision
