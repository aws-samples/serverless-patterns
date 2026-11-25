#!/usr/bin/env bash
#
# deploy.sh: deploy lambda-web-weighted-rollout and roll out new releases.
#
# Usage:
#   ./deploy.sh [deploy]       First deploy (current src/ in both slots, 100% blue), or
#                              re-apply the template with the current slots and weights
#   ./deploy.sh canary PCT     Upload src/ into the idle slot, then send it PCT% (1-99)
#   ./deploy.sh shift PCT      Change the share of the canary in progress (1-99)
#   ./deploy.sh promote        Send 100% to the canary; it becomes the live slot
#   ./deploy.sh rollback       Abort the canary in progress (100% back to the live slot),
#                              or, after a promote, switch back to the previous release
#   ./deploy.sh status         Show slots, code versions, weights, and the URL
#
# Options: --stack-name NAME  --bucket BUCKET  --key KEY  --region REGION
#   stack name : lambda-web-weighted-rollout
#   bucket     : <stack-name>-code-<account-id>-<region> (created on first deploy)
#   region     : --region, then $AWS_REGION, $AWS_DEFAULT_REGION, aws configure
#
set -euo pipefail

STACK_NAME="lambda-web-weighted-rollout"
CODE_KEY="web-function/app.zip"
CODE_BUCKET=""
REGION_FLAG=""
CMD=""
PCT=""

die() { echo "ERROR: $*" >&2; exit 1; }

while [[ $# -gt 0 ]]; do
  case "$1" in
    --stack-name) STACK_NAME="$2"; shift 2;;
    --bucket)     CODE_BUCKET="$2"; shift 2;;
    --key)        CODE_KEY="$2"; shift 2;;
    --region)     REGION_FLAG="$2"; shift 2;;
    -h|--help)    sed -n '3,/^set -euo/p' "$0" | sed '$d' | sed 's/^# \{0,1\}//'; exit 0;;
    deploy|canary|shift|promote|rollback|status)
      if [[ -n "${CMD}" ]]; then die "run one command at a time"; fi
      CMD="$1"; shift
      if [[ "${CMD}" == "canary" || "${CMD}" == "shift" ]]; then
        PCT="${1:-}"
        if [[ $# -gt 0 ]]; then shift; fi
      fi;;
    *) die "unknown argument: $1 (try --help)";;
  esac
done
CMD="${CMD:-deploy}"

if [[ "${CMD}" == "canary" || "${CMD}" == "shift" ]]; then
  if ! [[ "${PCT}" =~ ^[0-9]+$ ]] || (( PCT < 1 || PCT > 99 )); then
    die "${CMD} needs a percentage from 1 to 99, for example: ./deploy.sh ${CMD} 10"
  fi
fi

REGION="${REGION_FLAG:-${AWS_REGION:-${AWS_DEFAULT_REGION:-$(aws configure get region 2>/dev/null || true)}}}"
[[ -n "${REGION}" ]] || die "no AWS Region. Pass --region, set AWS_REGION, or run 'aws configure'."
case "${REGION}" in
  us-east-1|us-east-2|us-west-2|ap-northeast-1|eu-west-1) ;;
  *) echo "WARNING: ${REGION} may not support Lambda Web Functions. Check the Lambda documentation." >&2;;
esac

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

stack_exists() {
  aws cloudformation describe-stacks --stack-name "${STACK_NAME}" --region "${REGION}" >/dev/null 2>&1
}
param() {
  aws cloudformation describe-stacks --stack-name "${STACK_NAME}" --region "${REGION}" \
    --query "Stacks[0].Parameters[?ParameterKey=='$1'].ParameterValue | [0]" --output text
}
output() {
  aws cloudformation describe-stacks --stack-name "${STACK_NAME}" --region "${REGION}" \
    --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue | [0]" --output text
}
other() { if [[ "$1" == "blue" ]]; then echo green; else echo blue; fi; }
weight_of() { if [[ "$1" == "blue" ]]; then echo "${BLUE_WEIGHT}"; else echo "${GREEN_WEIGHT}"; fi; }
set_weight() { if [[ "$1" == "blue" ]]; then BLUE_WEIGHT="$2"; else GREEN_WEIGHT="$2"; fi; }
set_version() { if [[ "$1" == "blue" ]]; then BLUE_VERSION="$2"; else GREEN_VERSION="$2"; fi; }
set_deployed() { if [[ "$1" == "blue" ]]; then BLUE_DEPLOYED="$2"; else GREEN_DEPLOYED="$2"; fi; }
now_utc() { date -u +%Y-%m-%dT%H:%M:%SZ; }

load_state() {
  stack_exists || die "stack ${STACK_NAME} not found in ${REGION}. Run ./deploy.sh first."
  CODE_BUCKET="$(param CodeBucket)"
  CODE_KEY="$(param CodeKey)"
  BLUE_VERSION="$(param BlueCodeVersionId)"
  GREEN_VERSION="$(param GreenCodeVersionId)"
  BLUE_DEPLOYED="$(param BlueDeployedAt)"
  GREEN_DEPLOYED="$(param GreenDeployedAt)"
  [[ "${BLUE_DEPLOYED}" == "None" ]] && BLUE_DEPLOYED="unknown"
  [[ "${GREEN_DEPLOYED}" == "None" ]] && GREEN_DEPLOYED="unknown"
  BLUE_WEIGHT="$(param BlueWeight)"
  GREEN_WEIGHT="$(param GreenWeight)"
  LIVE_SLOT="$(param LiveSlot)"
  ROLLBACK_AVAILABLE="$(param RollbackAvailable)"
  CANARY_SLOT="$(other "${LIVE_SLOT}")"
}

ensure_bucket() {
  if aws s3api head-bucket --bucket "${CODE_BUCKET}" --region "${REGION}" 2>/dev/null; then
    echo "==> Bucket exists: ${CODE_BUCKET}"
    local status
    status="$(aws s3api get-bucket-versioning --bucket "${CODE_BUCKET}" --region "${REGION}" --query Status --output text)"
    [[ "${status}" == "Enabled" ]] || die "bucket ${CODE_BUCKET} must have versioning enabled"
    return
  fi
  echo "==> Creating bucket: ${CODE_BUCKET}"
  if [[ "${REGION}" == "us-east-1" ]]; then
    aws s3api create-bucket --bucket "${CODE_BUCKET}" --region "${REGION}" >/dev/null
  else
    aws s3api create-bucket --bucket "${CODE_BUCKET}" --region "${REGION}" \
      --create-bucket-configuration LocationConstraint="${REGION}" >/dev/null
  fi
  aws s3api put-bucket-versioning --bucket "${CODE_BUCKET}" --region "${REGION}" \
    --versioning-configuration Status=Enabled
  aws s3api put-public-access-block --bucket "${CODE_BUCKET}" --region "${REGION}" \
    --public-access-block-configuration \
    BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
  aws s3api put-bucket-encryption --bucket "${CODE_BUCKET}" --region "${REGION}" \
    --server-side-encryption-configuration \
    '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"},"BucketKeyEnabled":true}]}'
}

# Zips src/ and uploads it; sets NEW_VERSION to the new S3 object version.
upload() {
  local zip_dir
  zip_dir="$(mktemp -d)"
  trap 'rm -rf "${zip_dir}"' RETURN
  ( cd "${SCRIPT_DIR}/src" && zip -r -q "${zip_dir}/app.zip" . )
  echo "==> Uploading src/ to s3://${CODE_BUCKET}/${CODE_KEY}"
  NEW_VERSION="$(aws s3api put-object --bucket "${CODE_BUCKET}" --key "${CODE_KEY}" \
    --body "${zip_dir}/app.zip" --region "${REGION}" --query VersionId --output text)"
  [[ -n "${NEW_VERSION}" && "${NEW_VERSION}" != "None" ]] || die "upload returned no object version"
  echo "==> New code version: ${NEW_VERSION}"
}

apply() {
  echo "==> Updating stack: blue ${BLUE_WEIGHT}%, green ${GREEN_WEIGHT}%, live slot ${LIVE_SLOT}"
  (( BLUE_WEIGHT + GREEN_WEIGHT == 100 )) || die "weights must add up to 100"
  sam deploy \
    --template-file "${SCRIPT_DIR}/template.yaml" \
    --stack-name "${STACK_NAME}" \
    --region "${REGION}" \
    --capabilities CAPABILITY_IAM \
    --s3-bucket "${CODE_BUCKET}" \
    --s3-prefix sam-artifacts \
    --no-confirm-changeset \
    --no-fail-on-empty-changeset \
    --tags pattern=lambda-web-weighted-rollout stack="${STACK_NAME}" \
    --parameter-overrides \
      CodeBucket="${CODE_BUCKET}" \
      CodeKey="${CODE_KEY}" \
      BlueCodeVersionId="${BLUE_VERSION}" \
      GreenCodeVersionId="${GREEN_VERSION}" \
      BlueDeployedAt="${BLUE_DEPLOYED}" \
      GreenDeployedAt="${GREEN_DEPLOYED}" \
      BlueWeight="${BLUE_WEIGHT}" \
      GreenWeight="${GREEN_WEIGHT}" \
      LiveSlot="${LIVE_SLOT}" \
      RollbackAvailable="${ROLLBACK_AVAILABLE}"
}

# Colors only on a terminal, and never when NO_COLOR is set (https://no-color.org).
if [[ -t 1 && -z "${NO_COLOR:-}" ]]; then
  C_BOLD=$'\033[1m'; C_DIM=$'\033[2m'; C_RESET=$'\033[0m'
  C_BLUE=$'\033[1;34m'; C_GREEN=$'\033[1;32m'; C_YELLOW=$'\033[1;33m'; C_CYAN=$'\033[1;36m'
else
  C_BOLD=""; C_DIM=""; C_RESET=""; C_BLUE=""; C_GREEN=""; C_YELLOW=""; C_CYAN=""
fi
RULE="======================================================================"

show_status() {
  load_state
  local slot role color code deployed
  echo
  echo "${C_CYAN}${RULE}${C_RESET}"
  echo "${C_BOLD}  Rollout status${C_RESET}"
  echo "${C_CYAN}${RULE}${C_RESET}"
  echo "  Stack:  ${STACK_NAME} (${REGION})"
  echo "  URL:    ${C_BOLD}$(output CloudFrontUrl)${C_RESET}"
  echo
  for slot in blue green; do
    if [[ "${slot}" == "${LIVE_SLOT}" ]]; then role="live"; elif (( $(weight_of "${slot}") > 0 )); then role="canary"; else role="idle"; fi
    if [[ "${slot}" == "blue" ]]; then color="${C_BLUE}"; code="${BLUE_VERSION}"; deployed="${BLUE_DEPLOYED}"; else color="${C_GREEN}"; code="${GREEN_VERSION}"; deployed="${GREEN_DEPLOYED}"; fi
    printf "  %s%-6s%s %3s%%  %-7s deployed %-20s ${C_DIM}code %s${C_RESET}\n" "${color}" "${slot}" "${C_RESET}" "$(weight_of "${slot}")" "${role}" "${deployed}" "${code}"
  done
  echo
  if (( $(weight_of "${CANARY_SLOT}") > 0 )); then
    echo "  ${C_YELLOW}Canary in progress on ${CANARY_SLOT}.${C_RESET}"
    echo "  ${C_YELLOW}Next: ./deploy.sh shift PCT (change canary %) | promote | rollback${C_RESET}"
  elif [[ "${ROLLBACK_AVAILABLE}" == "yes" ]]; then
    echo "  ${C_YELLOW}The ${CANARY_SLOT} slot holds the previous release.${C_RESET}"
    echo "  ${C_YELLOW}Next: ./deploy.sh rollback switches back to it.${C_RESET}"
  else
    echo "  ${C_YELLOW}Next: change src/, then ./deploy.sh canary 10${C_RESET}"
  fi
  echo "${C_CYAN}${RULE}${C_RESET}"
  echo
}

case "${CMD}" in
  deploy)
    if stack_exists; then
      load_state
      echo "==> Stack exists. Re-applying the template with the current slots and weights."
      echo "    To release new code, use: ./deploy.sh canary 10"
      apply
    else
      ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
      CODE_BUCKET="${CODE_BUCKET:-${STACK_NAME}-code-${ACCOUNT_ID}-${REGION}}"
      ensure_bucket
      upload
      BLUE_VERSION="${NEW_VERSION}"; GREEN_VERSION="${NEW_VERSION}"
      BLUE_DEPLOYED="$(now_utc)"; GREEN_DEPLOYED="${BLUE_DEPLOYED}"
      BLUE_WEIGHT=100; GREEN_WEIGHT=0; LIVE_SLOT=blue; ROLLBACK_AVAILABLE=no
      apply
    fi
    show_status;;

  canary)
    load_state
    if (( $(weight_of "${CANARY_SLOT}") > 0 )); then
      die "a canary is already in progress on ${CANARY_SLOT} ($(weight_of "${CANARY_SLOT}")%). Nothing was changed.
  To change its share:       ./deploy.sh shift ${PCT}
  To finish it:              ./deploy.sh promote
  To release different code: ./deploy.sh rollback, then ./deploy.sh canary ${PCT}"
    fi
    upload
    # Step 1: replace the idle slot's revision while it has no traffic.
    set_version "${CANARY_SLOT}" "${NEW_VERSION}"
    set_deployed "${CANARY_SLOT}" "$(now_utc)"
    ROLLBACK_AVAILABLE=no
    echo "==> Step 1 of 2: create the ${CANARY_SLOT} revision with the new code (no traffic yet)"
    apply
    # Step 2: route traffic to it now that it exists and is Active.
    set_weight "${CANARY_SLOT}" "${PCT}"
    set_weight "${LIVE_SLOT}" "$(( 100 - PCT ))"
    echo "==> Step 2 of 2: send ${PCT}% of traffic to ${CANARY_SLOT}"
    apply
    show_status;;

  shift)
    load_state
    (( $(weight_of "${CANARY_SLOT}") > 0 )) || die "no canary in progress. Start one with: ./deploy.sh canary 10"
    set_weight "${CANARY_SLOT}" "${PCT}"
    set_weight "${LIVE_SLOT}" "$(( 100 - PCT ))"
    apply
    show_status;;

  promote)
    load_state
    (( $(weight_of "${CANARY_SLOT}") > 0 )) || die "no canary in progress to promote"
    set_weight "${CANARY_SLOT}" 100
    set_weight "${LIVE_SLOT}" 0
    LIVE_SLOT="${CANARY_SLOT}"
    ROLLBACK_AVAILABLE=yes
    apply
    show_status;;

  rollback)
    load_state
    if (( $(weight_of "${CANARY_SLOT}") > 0 )); then
      echo "==> Aborting the canary: 100% back to ${LIVE_SLOT}"
      set_weight "${LIVE_SLOT}" 100
      set_weight "${CANARY_SLOT}" 0
      ROLLBACK_AVAILABLE=no
    elif [[ "${ROLLBACK_AVAILABLE}" == "yes" ]]; then
      echo "==> Switching back to the previous release in the ${CANARY_SLOT} slot"
      set_weight "${CANARY_SLOT}" 100
      set_weight "${LIVE_SLOT}" 0
      LIVE_SLOT="${CANARY_SLOT}"
      ROLLBACK_AVAILABLE=no
    else
      die "nothing to roll back: no canary in progress and no previous release in the idle slot"
    fi
    apply
    show_status;;

  status)
    show_status;;
esac
