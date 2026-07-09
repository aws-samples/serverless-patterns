#!/usr/bin/env bash
# Data-plane helper for the Lambda MicroVMs + S3 Files pattern.
#
# CloudFormation (template.yaml) provisions the image, the S3 Files file system /
# mount target / access point, the VPC egress connector, and all IAM roles. The
# two things CloudFormation can NOT do are runtime/data-plane operations:
#
#   package  — zip src/ and upload it to the artifact bucket. The image build
#              reads this zip, so it must exist BEFORE `sam deploy`.
#   run      — RunMicrovm + mint an auth token + exercise the app. RunMicrovm is
#              a runtime API (like invoking a Lambda), not a CloudFormation resource.
#
# Usage:
#   ./src/run.sh package <artifact-bucket> [key]      # before sam deploy
#   ./src/run.sh run     <cfn-stack-name>             # after  sam deploy
#   ./src/run.sh prove   <cfn-stack-name>             # write a file, watch it sync to S3
#   ./src/run.sh terminate <cfn-stack-name>           # terminate the running MicroVM
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

# curl an endpoint with the proxy auth headers, retrying until HTTP 200.
# Usage: wait_for_200 <url> <token> <out-file> [tries] [sleep] [max-time]
# Echoes the last HTTP code; returns non-zero if 200 was never seen.
wait_for_200() {
  local url=$1 token=$2 out=$3 tries=${4:-40} slp=${5:-2} mt=${6:-5} i code=000
  for ((i=0; i<tries; i++)); do
    code=$(curl -sS -o "$out" -w "%{http_code}" "$url" \
            -H "X-aws-proxy-auth: $token" -H "X-aws-proxy-port: ${APP_PORT}" \
            --max-time "$mt" || true)
    [[ "$code" == "200" ]] && { echo "$code"; return 0; }
    sleep "$slp"
  done
  echo "$code"; return 1
}

# Wait until the /run lifecycle hook has finished mounting. The hook records a
# "run" event with detail.mounted only AFTER the S3 Files mount is usable (a real
# I/O round trip succeeded, not just findmnt registering the mountpoint). Gating
# on this — instead of the first HTTP 200 — is what keeps an immediately-following
# `prove` from writing before the efs-proxy tunnel is ready and losing the file.
# Returns 0 once mounted, 1 on an observed mount failure, 2 if it never appeared.
wait_for_mount() {
  local endpoint=$1 token=$2 tries=${3:-40} slp=${4:-3} i body mounted
  for ((i=0; i<tries; i++)); do
    body=$(curl -sS "https://${endpoint}/lifecycle" \
             -H "X-aws-proxy-auth: $token" -H "X-aws-proxy-port: ${APP_PORT}" \
             --max-time 5 2>/dev/null || true)
    if [[ -n "$body" ]]; then
      mounted=$(printf '%s' "$body" | python3 -c '
import json, sys
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
runs = [e for e in d.get("events", []) if e.get("event") == "run"]
if runs:
    print("true" if (runs[-1].get("detail") or {}).get("mounted") else "false")
' 2>/dev/null || true)
      [[ "$mounted" == "true" ]] && return 0
      [[ "$mounted" == "false" ]] && return 1
    fi
    sleep "$slp"
  done
  return 2
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
  local zip; zip="$(mktemp -t s3files-app).zip"
  ( cd "$SRC_DIR" && zip -q "$zip" Dockerfile app.py )
  aws s3 cp "$zip" "s3://${bucket}/${key}" --region "$REGION" >/dev/null
  rm -f "$zip"
  log "uploaded → s3://${bucket}/${key}"
  log "now: sam deploy --guided  (CodeArtifactBucket=${bucket} CodeArtifactKey=${key})"
}

# ── run: launch a MicroVM from the stack's image and mount S3 Files ──────────
run() {
  local stack="${1:?usage: run.sh run <cfn-stack-name>}"
  load_stack_outputs "$stack"
  [[ -n "${OUT_ImageArn:-}" && "$OUT_ImageArn" != "None" ]] \
    || die "stack '$stack' has no ImageArn output"

  # The MicroVM mounts by mount-target IP (regional mount DNS may not resolve over
  # the connector). Look the IPv4 up from the mount target id.
  local mt_ip
  mt_ip=$(aws s3files get-mount-target --mount-target-id "$OUT_MountTargetId" --region "$REGION" \
            --query 'ipv4Address' --output text 2>/dev/null || echo "")
  [[ -n "$mt_ip" && "$mt_ip" != "None" ]] \
    || die "could not resolve mount-target IP for $OUT_MountTargetId (is the file system AVAILABLE?)"

  # The access point roots the mount at a sub-directory (e.g. /microvm), so files
  # written on the mount land under that prefix in the bucket. Look the path up and
  # pass it so the app reports correct s3:// locations (bucket + AP prefix + file).
  local ap_path
  ap_path=$(aws s3files get-access-point --access-point-id "$OUT_AccessPointId" --region "$REGION" \
              --query 'rootDirectory.path' --output text 2>/dev/null || echo "")
  [[ "$ap_path" == "None" ]] && ap_path=""

  local payload
  payload=$(python3 - "$OUT_FileSystemId" "$OUT_AccessPointId" "$mt_ip" "$REGION" "$OUT_DataBucket" "$ap_path" <<'PY'
import json, sys
fsid, apid, mt_ip, region, bucket, ap_path = sys.argv[1:7]
payload = {"fileSystemId": fsid, "accessPointId": apid,
           "mountTargetIp": mt_ip, "region": region, "bucket": bucket}
# The access-point root directory becomes the bucket-side prefix for synced files.
prefix = ap_path.strip("/")
if prefix:
    payload["prefix"] = prefix
print(json.dumps(payload))
PY
)
  log "running MicroVM from $OUT_ImageArn"
  local out mvm_id endpoint
  out=$(aws lambda-microvms run-microvm --region "$REGION" \
    --image-identifier "$OUT_ImageArn" \
    --execution-role-arn "$OUT_ExecutionRoleArn" \
    --egress-network-connectors "[\"${OUT_EgressConnectorArn}\"]" \
    --idle-policy '{"maxIdleDurationSeconds":900,"suspendedDurationSeconds":600,"autoResumeEnabled":true}' \
    --maximum-duration-in-seconds 3600 \
    --run-hook-payload "$payload")
  # Pull both fields in one python invocation.
  read -r mvm_id endpoint < <(echo "$out" | python3 -c \
    "import sys,json;d=json.load(sys.stdin);print(d['microvmId'],d['endpoint'])")
  # Persist DATA_BUCKET too so prove/terminate need no further describe-stacks call.
  printf 'MVM_ID=%s\nMVM_ENDPOINT=%s\nDATA_BUCKET=%s\n' \
    "$mvm_id" "$endpoint" "$OUT_DataBucket" > "$STATE_FILE"
  log "microvmId=$mvm_id"
  log "endpoint=$endpoint"

  local token; token=$(mint_token "$mvm_id")
  log "polling app until first 200…"
  wait_for_200 "https://${endpoint}/" "$token" /dev/null 40 2 5 >/dev/null || true
  # Do NOT return on the first 200: the app answers before the /run hook has
  # finished mounting. Wait for the mount to be usable so a following `prove`
  # (or any write) does not race the efs-proxy tunnel and silently lose data.
  log "waiting for the S3 Files mount to become usable…"
  if wait_for_mount "$endpoint" "$token" 40 3; then
    log "mount ready"
  else
    log "WARNING: mount did not report ready — check /lifecycle and CloudWatch (last GET / below)"
  fi
  log "GET / →"
  curl -sS "https://${endpoint}/" -H "X-aws-proxy-auth: $token" \
    -H "X-aws-proxy-port: ${APP_PORT}" | python3 -m json.tool
}

mint_token() {
  aws lambda-microvms create-microvm-auth-token --region "$REGION" \
    --microvm-identifier "$1" --expiration-in-minutes 30 \
    --allowed-ports "[{\"port\":${APP_PORT}}]" \
    --query 'authToken."X-aws-proxy-auth"' --output text
}

# ── prove: write a file through the mount and watch it sync to S3 ────────────
prove() {
  local stack="${1:?usage: run.sh prove <cfn-stack-name>}"
  [[ -f "$STATE_FILE" ]] || die "run './src/run.sh run $stack' first"
  # shellcheck disable=SC1090
  source "$STATE_FILE"   # provides MVM_ID, MVM_ENDPOINT, DATA_BUCKET
  local token; token=$(mint_token "$MVM_ID")

  # The VM may have idle-suspended; the first request auto-resumes it and can
  # cold-path time out. Retry /sync-proof until it returns a 200 body.
  local body code
  body=$(mktemp); trap 'rm -f "$body"' RETURN
  log "GET /sync-proof (writes a file through the mount) →"
  code=$(wait_for_200 "https://${MVM_ENDPOINT}/sync-proof" "$token" "$body" 20 3 15) \
    || die "/sync-proof did not return 200 (last code: ${code})"
  python3 -m json.tool < "$body"

  # Poll for the EXACT s3:// object this call just wrote (from the response's
  # will_appear_in_s3_at), not merely a non-empty prefix — otherwise a re-run
  # would "pass" instantly on a file left by a previous run.
  local s3_uri
  s3_uri=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1])).get("will_appear_in_s3_at",""))' "$body" 2>/dev/null || true)
  [[ "$s3_uri" == s3://* ]] || die "could not determine the written object's S3 URI from the response"

  log "polling ${s3_uri} for the synced file (S3 export is async)…"
  local i
  for i in $(seq 1 24); do
    if aws s3 ls "$s3_uri" --region "$REGION" 2>/dev/null | grep -q .; then
      log "synced to S3:"; aws s3 ls "$s3_uri" --region "$REGION"; return 0
    fi
    sleep 5
  done
  log "not visible yet — sync can lag; re-check: aws s3 ls ${s3_uri}"
}

# ── terminate ────────────────────────────────────────────────────────────────
terminate() {
  local stack="${1:?usage: run.sh terminate <cfn-stack-name>}"
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
  terminate) terminate "$@" ;;
  *) die "usage: run.sh {package <bucket> [key] | run <stack> | prove <stack> | terminate <stack>}" ;;
esac
