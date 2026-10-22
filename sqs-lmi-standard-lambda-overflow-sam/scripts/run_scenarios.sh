#!/usr/bin/env bash
# Runs the two load-test scenarios and prints the dashboard time window for each.
#
#   ./run_scenarios.sh <stack-name> [scenario]
#
#   scenario 1  Baseline, then a burst held long enough for LMI to scale through it.
#               Shows the burst tier opening, LMI catching up, and the burst tier closing.
#   scenario 2  Baseline, then a short spike. Shows the burst tier absorbing a spike that
#               ends before LMI has scaled at all.
#   scenario 3  Scenario 1's shape with production-like arrivals: Poisson inter-arrival
#               times throughout, and a burst that ramps in and out over a minute instead
#               of stepping. Use this one to judge the controller; scenario 1's instant
#               step and metronome pacing flatter it.
#   scenario 0  Baseline only. Establishes the steady-state footprint to reserve.
#
# Default is scenario 1.

set -euo pipefail

STACK_NAME="${1:?usage: run_scenarios.sh <stack-name> [0|1|2]}"
SCENARIO="${2:-1}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Match the deployed template. Baseline drain rate = LmiBaselineExecutionEnvironments
# x LmiPerEnvironmentConcurrency / (WorkDurationMs / 1000) = 3 x 10 / 1 = 30 msg/s.
BASELINE_RATE="${BASELINE_RATE:-25}"
BURST_RATE="${BURST_RATE:-300}"
WARMUP_SECONDS="${WARMUP_SECONDS:-600}"
BURST_SECONDS="${BURST_SECONDS:-1200}"
SPIKE_SECONDS="${SPIKE_SECONDS:-90}"
COOLDOWN_SECONDS="${COOLDOWN_SECONDS:-600}"
RAMP_SECONDS="${RAMP_SECONDS:-60}"
SEED="${SEED:-1}"

query_output() {
  aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" \
    --output text
}

QUEUE_URL="$(query_output WorkQueueUrl)"
DASHBOARD_URL="$(query_output DashboardUrl)"
START_ISO="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

echo "queue:     $QUEUE_URL"
echo "dashboard: $DASHBOARD_URL"
echo "scenario:  $SCENARIO"
echo

baseline() {
  local seconds="$1" label="$2"
  echo "== baseline ${BASELINE_RATE} msg/s for ${seconds}s (${label}) =="
  python3 "$HERE/load_generator.py" \
    --queue-url "$QUEUE_URL" --rate "$BASELINE_RATE" --duration "$seconds" \
    --label "$label"
}

# Same baseline, but with Poisson arrivals, for scenario 3.
baseline_poisson() {
  local seconds="$1" label="$2"
  echo "== baseline ${BASELINE_RATE} msg/s for ${seconds}s, poisson (${label}) =="
  python3 "$HERE/load_generator.py" \
    --queue-url "$QUEUE_URL" --rate "$BASELINE_RATE" --duration "$seconds" \
    --label "$label" --jitter poisson --seed "$SEED"
}

case "$SCENARIO" in
  0)
    baseline "$WARMUP_SECONDS" baseline
    ;;
  1)
    baseline "$WARMUP_SECONDS" warmup
    echo
    echo "== burst ${BURST_RATE} msg/s for ${BURST_SECONDS}s (baseline continues) =="
    # Baseline keeps running underneath the burst: a real burst is additional traffic,
    # not a replacement for the steady state.
    python3 "$HERE/load_generator.py" \
      --queue-url "$QUEUE_URL" --rate "$BASELINE_RATE" \
      --duration "$BURST_SECONDS" --label baseline &
    BASELINE_PID=$!
    python3 "$HERE/load_generator.py" \
      --queue-url "$QUEUE_URL" --rate "$((BURST_RATE - BASELINE_RATE))" \
      --duration "$BURST_SECONDS" --label burst
    wait "$BASELINE_PID"
    echo
    baseline "$COOLDOWN_SECONDS" cooldown
    ;;
  2)
    baseline "$WARMUP_SECONDS" warmup
    echo
    echo "== spike ${BURST_RATE} msg/s for ${SPIKE_SECONDS}s =="
    python3 "$HERE/load_generator.py" \
      --queue-url "$QUEUE_URL" --rate "$BURST_RATE" \
      --duration "$SPIKE_SECONDS" --label spike
    echo
    baseline "$COOLDOWN_SECONDS" cooldown
    ;;
  3)
    baseline_poisson "$WARMUP_SECONDS" warmup
    echo
    echo "== burst to ${BURST_RATE} msg/s over ${RAMP_SECONDS}s, hold, ramp out =="
    # The baseline never stops: the burst is extra traffic arriving on top of the steady
    # state, and the steady state is what pays for the reserved LMI capacity.
    python3 "$HERE/load_generator.py" \
      --queue-url "$QUEUE_URL" --rate "$BASELINE_RATE" \
      --duration "$BURST_SECONDS" --label baseline \
      --jitter poisson --seed "$SEED" &
    BASELINE_PID=$!
    python3 "$HERE/load_generator.py" \
      --queue-url "$QUEUE_URL" --rate "$((BURST_RATE - BASELINE_RATE))" \
      --duration "$BURST_SECONDS" --label burst \
      --jitter poisson --seed "$((SEED + 1))" \
      --ramp-up-seconds "$RAMP_SECONDS" --ramp-down-seconds "$RAMP_SECONDS"
    wait "$BASELINE_PID"
    echo
    baseline_poisson "$COOLDOWN_SECONDS" cooldown
    ;;
  *)
    echo "unknown scenario: $SCENARIO" >&2
    exit 2
    ;;
esac

END_ISO="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo
echo "run window: $START_ISO to $END_ISO"
echo "open the dashboard and set the time range to that window:"
echo "  $DASHBOARD_URL"
echo
echo "burst-tier transitions:"
echo "  aws logs tail /aws/lambda/\$(aws cloudformation describe-stack-resource \\"
echo "    --stack-name $STACK_NAME --logical-resource-id SpillControllerFunction \\"
echo "    --query 'StackResourceDetail.PhysicalResourceId' --output text) --since 1h"
