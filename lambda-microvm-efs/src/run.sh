#!/usr/bin/env bash
# Data-plane helper for the Lambda MicroVMs + Amazon EFS pattern.
#
# CloudFormation (template.yaml) provisions the image, the EFS file system /
# mount target / access point, the VPC egress connector, and all IAM roles. The
# things CloudFormation can NOT do are runtime/data-plane operations:
#
#   package  — zip src/ and upload it to the artifact bucket. The image build
#              reads this zip, so it must exist BEFORE `sam deploy`.
#   run      — RunMicrovm + mint an auth token + exercise the app. RunMicrovm is
#              a runtime API (like invoking a Lambda), not a CloudFormation resource.
#   prove    — launch a SECOND MicroVM and show it reading a file the first one
#              just wrote. This is the point of EFS: one shared POSIX tree.
#   bench    — measure real read throughput from the MicroVM to EFS.
#
# Usage:
#   ./src/run.sh package <artifact-bucket> [key]     # before sam deploy
#   ./src/run.sh run <stack-name>                    # after sam deploy
#   ./src/run.sh prove <stack-name>                  # two VMs, one file system
#   ./src/run.sh bench <stack-name> [seconds] [streams]
#   ./src/run.sh terminate <stack-name>
#
# REGION defaults to us-west-2 (override with REGION=...). Credentials come from
# the usual AWS chain (AWS_PROFILE / env / instance role).

set -euo pipefail

: "${REGION:=us-west-2}"
: "${APP_PORT:=8080}"

SRC_DIR="$(cd "$(dirname "$0")" && pwd)"
STATE_FILE="${SRC_DIR}/../.run-state.${REGION}.env"

log()  { printf '\033[1;36m[%s]\033[0m %s\n' "$(date +%H:%M:%S)" "$*"; }
die()  { printf '\033[1;31merror:\033[0m %s\n' "$*" >&2; exit 1; }

# Load ALL of a stack's outputs into shell vars OUT_<OutputKey> in one
# describe-stacks call (instead of one round-trip per output).
load_stack_outputs() {
  local kv
  kv=$(aws cloudformation describe-stacks --stack-name "$1" --region "$REGION" \
        --query "Stacks[0].Outputs[].[OutputKey,OutputValue]" --output text)
  [[ -n "$kv" ]] || die "stack '$1' not found or has no outputs"
  while IFS=$'\t' read -r key val; do
    [[ -n "$key" ]] && eval "OUT_${key}=\$val"
  done <<< "$kv"
}

mint_token() {
  aws lambda-microvms create-microvm-auth-token --region "$REGION" \
    --microvm-identifier "$1" --expiration-in-minutes 30 \
    --allowed-ports "[{\"port\":${APP_PORT}}]" \
    --query 'authToken."X-aws-proxy-auth"' --output text
}

# curl an endpoint with the proxy auth headers, retrying until HTTP 200.
# Usage: wait_for_200 <url> <token> <out-file> [tries] [sleep] [max-time]
wait_for_200() {
  local url=$1 token=$2 out=$3 tries=${4:-40} slp=${5:-2} mt=${6:-5} i code=000
  for ((i=0; i<tries; i++)); do
    code=$(curl -sS -o "$out" -w '%{http_code}' --max-time "$mt" \
             -H "X-aws-proxy-auth: $token" -H "X-aws-proxy-port: ${APP_PORT}" \
             "$url" 2>/dev/null || echo 000)
    [[ "$code" == "200" ]] && { echo "$code"; return 0; }
    sleep "$slp"
  done
  echo "$code"; return 1
}

# Poll /lifecycle until the most recent run/resume event reports mounted=true.
# Returns 0 mounted, 1 explicitly not mounted, 2 never answered.
wait_for_mount() {
  local endpoint=$1 token=$2 tries=${3:-40} slp=${4:-3} i body mounted
  for ((i=0; i<tries; i++)); do
    body=$(curl -sS --max-time 5 -H "X-aws-proxy-auth: $token" \
             -H "X-aws-proxy-port: ${APP_PORT}" \
             "https://${endpoint}/lifecycle" 2>/dev/null || true)
    if [[ -n "$body" ]]; then
      mounted=$(printf '%s' "$body" | python3 -c '
import json, sys
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
evs = [e for e in d.get("events", []) if e.get("event") in ("run", "resume")]
if evs:
    print("true" if (evs[-1].get("detail") or {}).get("mounted") else "false")
' 2>/dev/null || true)
      [[ "$mounted" == "true" ]] && return 0
      [[ "$mounted" == "false" ]] && return 1
    fi
    sleep "$slp"
  done
  return 2
}

# Build the run-hook payload. Unlike the S3 Files pattern there is no bucket or
# prefix to pass: the mount IS the storage, so the guest only needs the file
# system, the access point, and the mount-target IP to reach it by.
build_payload() {
  local stack=$1 mt_ip
  # Mount by mount-target IP: the regional mount DNS name may not resolve over
  # the egress connector, but the AZ-local mount-target IP always works.
  mt_ip=$(aws efs describe-mount-targets --mount-target-id "$OUT_MountTargetId" --region "$REGION" \
            --query 'MountTargets[0].IpAddress' --output text 2>/dev/null || echo "")
  [[ -n "$mt_ip" && "$mt_ip" != "None" ]] \
    || die "could not resolve mount-target IP for $OUT_MountTargetId (is the file system available?)"
  python3 - "$OUT_FileSystemId" "$OUT_AccessPointId" "$mt_ip" "$REGION" <<'PY'
import json, sys
fsid, apid, mt_ip, region = sys.argv[1:5]
print(json.dumps({
    "fileSystemId": fsid,
    "accessPointId": apid,
    "mountTargetIp": mt_ip,
    "region": region,
}))
PY
}

# Launch one MicroVM. Echoes "<microvmId> <endpoint>".
launch_microvm() {
  local payload=$1 out
  out=$(aws lambda-microvms run-microvm --region "$REGION" \
          --image-identifier "$OUT_ImageArn" \
          --execution-role-arn "$OUT_ExecutionRoleArn" \
          --egress-network-connectors "[\"${OUT_EgressConnectorArn}\"]" \
          --idle-policy '{"maxIdleDurationSeconds":900,"suspendedDurationSeconds":600,"autoResumeEnabled":true}' \
          --maximum-duration-in-seconds 3600 \
          --run-hook-payload "$payload")
  echo "$out" | python3 -c \
    "import sys,json;d=json.load(sys.stdin);print(d['microvmId'],d['endpoint'])"
}

# ── package: zip src/ and upload to the artifact bucket ──────────────────────
package() {
  local bucket="${1:?usage: run.sh package <artifact-bucket> [key]}" key="${2:-app.zip}"
  [[ -f "$SRC_DIR/Dockerfile" && -f "$SRC_DIR/app.py" ]] \
    || die "Dockerfile and app.py must exist in $SRC_DIR"

  # Create the artifact bucket if it is missing (must be in REGION).
  if ! aws s3api head-bucket --bucket "$bucket" --region "$REGION" 2>/dev/null; then
    log "creating artifact bucket $bucket ($REGION)"
    if [[ "$REGION" == "us-east-1" ]]; then
      aws s3api create-bucket --bucket "$bucket" --region "$REGION" >/dev/null
    else
      aws s3api create-bucket --bucket "$bucket" --region "$REGION" \
        --create-bucket-configuration "LocationConstraint=${REGION}" >/dev/null
    fi
  fi

  local zip; zip="$(mktemp -t efs-app.XXXXXX).zip"
  ( cd "$SRC_DIR" && zip -q "$zip" Dockerfile app.py )
  aws s3 cp "$zip" "s3://${bucket}/${key}" --region "$REGION" >/dev/null
  rm -f "$zip"
  log "uploaded → s3://${bucket}/${key}"
  log "now: sam deploy --guided (CodeArtifactBucket=${bucket} CodeArtifactKey=${key})"
}

# ── run: launch a MicroVM from the stack's image and mount EFS ───────────────
run() {
  local stack="${1:?usage: run.sh run <stack-name>}"
  load_stack_outputs "$stack"
  [[ -n "${OUT_ImageArn:-}" && "$OUT_ImageArn" != "None" ]] \
    || die "stack '$stack' has no ImageArn output"

  local payload; payload=$(build_payload "$stack")

  log "running MicroVM from $OUT_ImageArn"
  local mvm_id endpoint
  read -r mvm_id endpoint < <(launch_microvm "$payload")

  printf 'MVM_ID=%s\nMVM_ENDPOINT=%s\n' "$mvm_id" "$endpoint" > "$STATE_FILE"
  log "microvmId=$mvm_id"
  log "endpoint=$endpoint"

  local token; token=$(mint_token "$mvm_id")

  log "polling app until first 200…"
  wait_for_200 "https://${endpoint}/" "$token" /dev/null 40 2 5 >/dev/null || true

  # Do NOT return on the first 200: the app answers before the /run hook has
  # finished mounting. Wait for the mount to be usable so a following write does
  # not race the efs-proxy tunnel.
  log "waiting for the EFS mount to become usable…"
  if wait_for_mount "$endpoint" "$token" 40 3; then
    log "mount ready"
  else
    log "WARNING: mount did not report ready — check /lifecycle and CloudWatch (GET / below)"
  fi

  log "GET / →"
  curl -sS "https://${endpoint}/" -H "X-aws-proxy-auth: $token" \
    -H "X-aws-proxy-port: ${APP_PORT}" | python3 -m json.tool
}

# ── prove: two MicroVMs, one file system ────────────────────────────────────
# Write a file from VM #1, then launch VM #2 and read the SAME file back through
# its own independent mount. This is the property that distinguishes EFS from an
# object-store facade: no export step, no sync lag — the second VM sees the bytes
# because it is the same file system, not a copy of it.
prove() {
  local stack="${1:?usage: run.sh prove <stack-name>}"
  [[ -f "$STATE_FILE" ]] || die "run './src/run.sh run $stack' first"
  # shellcheck disable=SC1090
  source "$STATE_FILE"   # provides MVM_ID, MVM_ENDPOINT
  load_stack_outputs "$stack"

  local token1; token1=$(mint_token "$MVM_ID")
  local marker="handoff-$(date +%s)-$RANDOM"
  local rel="shared/${marker}.txt"
  local content="written by microVM ${MVM_ID} at $(date -u +%FT%TZ)"

  log "VM #1 ($MVM_ID): PUT /files/${rel} →"
  curl -sS -X PUT "https://${MVM_ENDPOINT}/files/${rel}" \
    -H "X-aws-proxy-auth: $token1" -H "X-aws-proxy-port: ${APP_PORT}" \
    --data-binary "$content" | python3 -m json.tool

  log "launching VM #2 against the same file system…"
  local payload; payload=$(build_payload "$stack")
  local id2 ep2
  read -r id2 ep2 < <(launch_microvm "$payload")
  log "VM #2 microvmId=$id2"

  # Always clean up VM #2, even if the read below fails.
  # shellcheck disable=SC2064
  trap "log 'terminating VM #2 ($id2)'; aws lambda-microvms terminate-microvm --microvm-identifier '$id2' --region '$REGION' >/dev/null 2>&1 || true" RETURN

  local token2; token2=$(mint_token "$id2")
  wait_for_200 "https://${ep2}/" "$token2" /dev/null 40 2 5 >/dev/null || true
  log "waiting for VM #2's mount…"
  wait_for_mount "$ep2" "$token2" 40 3 \
    || die "VM #2 did not mount the file system — check its /lifecycle and CloudWatch"

  local body; body=$(mktemp)
  log "VM #2 ($id2): GET /files/${rel} →"
  local code
  code=$(wait_for_200 "https://${ep2}/files/${rel}" "$token2" "$body" 10 3 10) \
    || { rm -f "$body"; die "VM #2 could not read the file (last code: ${code})"; }

  local got; got=$(cat "$body"); rm -f "$body"
  printf '  %s\n' "$got"

  if [[ "$got" == "$content" ]]; then
    log "PROVED: VM #2 read the exact bytes VM #1 wrote, through its own mount."
  else
    die "content mismatch — expected '$content', got '$got'"
  fi

  # Both VMs have appended to the shared log by now; show the distinct writers.
  log "GET /shared-log from VM #2 (shows every MicroVM that has mounted this fs) →"
  curl -sS "https://${ep2}/shared-log" -H "X-aws-proxy-auth: $token2" \
    -H "X-aws-proxy-port: ${APP_PORT}" \
    | python3 -c 'import json,sys; d=json.load(sys.stdin); print(json.dumps({k:d[k] for k in ("total_visits","distinct_instances","other_instances_seen")}, indent=2))'
}

# ── bench: measure read throughput from the MicroVM to EFS ───────────────────
bench() {
  local stack="${1:?usage: run.sh bench <stack-name> [seconds] [streams]}"
  local seconds="${2:-15}" streams="${3:-8}" seed_mib="${SEED_MIB:-256}"
  [[ -f "$STATE_FILE" ]] || die "run './src/run.sh run $stack' first"
  # shellcheck disable=SC1090
  source "$STATE_FILE"
  local token; token=$(mint_token "$MVM_ID")

  # Seeding writes the read-test file onto EFS. It persists on the file system, so
  # this is a no-op on every run after the first (even from a different MicroVM).
  log "seeding ${seed_mib} MiB read file (skipped if already present)…"
  local body; body=$(mktemp)
  wait_for_200 "https://${MVM_ENDPOINT}/benchmark/seed?mib=${seed_mib}" "$token" "$body" 20 5 120 \
    >/dev/null || { rm -f "$body"; die "seeding failed"; }
  python3 -m json.tool < "$body"

  log "measuring: ${seconds}s, ${streams} parallel O_DIRECT streams →"
  wait_for_200 \
    "https://${MVM_ENDPOINT}/benchmark?seconds=${seconds}&streams=${streams}&mib=${seed_mib}" \
    "$token" "$body" 10 5 $((seconds + 60)) >/dev/null \
    || { rm -f "$body"; die "benchmark call failed"; }
  python3 -m json.tool < "$body"
  rm -f "$body"

  log "note: sustained throughput tracks MinimumMemoryInMiB (the egress allocation)."
  log "      redeploy with a larger value to see it scale; see README \"Throughput\"."
}

# ── terminate ───────────────────────────────────────────────────────────────
terminate() {
  local stack="${1:?usage: run.sh terminate <stack-name>}"
  [[ -f "$STATE_FILE" ]] || die "no run state for region $REGION"
  # shellcheck disable=SC1090
  source "$STATE_FILE"
  log "terminating $MVM_ID"
  aws lambda-microvms terminate-microvm --microvm-identifier "$MVM_ID" --region "$REGION" >/dev/null
  rm -f "$STATE_FILE"
  log "terminated"
}

cmd="${1:-}"; shift || true
case "$cmd" in
  package)   package "$@" ;;
  run)       run "$@" ;;
  prove)     prove "$@" ;;
  bench)     bench "$@" ;;
  terminate) terminate "$@" ;;
  *) die "usage: run.sh {package <bucket> [key] | run <stack> | prove <stack> | bench <stack> [seconds] [streams] | terminate <stack>}" ;;
esac
