#!/usr/bin/env bash
# Deploys the app in ../src to the Lambda Web Function created by this pattern.
#
#   scripts/deploy.sh production               Deploy to the prod endpoint (creates the function the first time)
#   scripts/deploy.sh preview <pr-number>      Deploy to the pr-<number> endpoint, creating it if needed
#   scripts/deploy.sh delete-preview <pr-number>  Delete the pr-<number> endpoint and its revisions
#   scripts/deploy.sh destroy                  Delete the Web Function and empty the code bucket, before sam delete
#
# Environment: STACK_NAME (default lambda-web-pr-previews), GIT_SHA (default: git rev-parse HEAD).
# Uses the AWS Region from your AWS CLI configuration or AWS_REGION. Needs AWS CLI 2.37.13 or later.
set -euo pipefail

export AWS_PAGER=""
STACK_NAME="${STACK_NAME:-lambda-web-pr-previews}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR="$SCRIPT_DIR/../src"
BUILD_DIR="$SCRIPT_DIR/../build"

usage() { sed -n '2,10p' "$0" >&2; exit 2; }
[[ $# -ge 1 ]] || usage
COMMAND="$1"
PR="${2:-}"
case "$COMMAND" in
  production|destroy) ;;
  preview|delete-preview) [[ "$PR" =~ ^[0-9]+$ ]] || { echo "Pull request number must be numeric" >&2; exit 2; } ;;
  *) usage ;;
esac

output() {
  aws cloudformation describe-stacks --stack-name "$STACK_NAME" \
    --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text
}
FUNCTION="$(output FunctionName)"
BUCKET="$(output CodeBucketName)"

endpoint_exists() {
  aws lambda-web get-web-function-endpoint --function-name "$FUNCTION" --endpoint-name "$1" >/dev/null 2>&1
}
endpoint_url() {
  echo "https://$(aws lambda-web get-web-function-endpoint --function-name "$FUNCTION" --endpoint-name "$1" --query domainName --output text)/"
}
weights() { printf '[{"revisionId":"%s","weight":100}]' "$1"; }

# Package src/ and upload it. Prints the S3 object version ID.
upload() {
  local key="$1"
  rm -rf "$BUILD_DIR" && mkdir -p "$BUILD_DIR"
  cp -R "$SRC_DIR"/. "$BUILD_DIR/app"
  if [[ -f "$BUILD_DIR/app/package-lock.json" ]]; then
    (cd "$BUILD_DIR/app" && npm ci --omit=dev --no-audit --no-fund >&2)
  fi
  (cd "$BUILD_DIR/app" && zip -q -r ../app.zip .)
  aws s3api put-object --bucket "$BUCKET" --key "$key" --body "$BUILD_DIR/app.zip" --query VersionId --output text
}

build_config() {
  printf '{"codeConfig":{"s3Object":{"bucket":"%s","key":"%s","versionId":"%s"}},"runtimeConfig":{"runtime":"nodejs24.x"}}' "$BUCKET" "$1" "$2"
}
service_config() {
  printf '{"executionRoleArn":"%s","timeoutSeconds":30,"environmentVariables":{"GIT_SHA":"%s"}}' "$1" "$GIT_SHA"
}

# Create a revision and wait until it is Active. Prints the revision ID.
create_revision() {
  local description="$1" key="$2" role="$3" version revision
  version="$(upload "$key")"
  revision="$(aws lambda-web create-web-function-revision --function-name "$FUNCTION" \
    --description "$description" \
    --build-config "$(build_config "$key" "$version")" \
    --service-config "$(service_config "$role")" \
    --query revisionId --output text)"
  aws lambda-web wait web-function-revision-active --function-name "$FUNCTION" --revision-id "$revision"
  echo "$revision"
}

# Point an existing endpoint at a revision and wait for the update to finish.
route() {
  aws lambda-web update-web-function-endpoint --function-name "$FUNCTION" --endpoint-name "$1" \
    --revision-weights "$(weights "$2")" >/dev/null
  aws lambda-web wait web-function-endpoint-updated --function-name "$FUNCTION" --endpoint-name "$1"
}

# Delete revisions whose description starts with the prefix, except the one to keep.
# A revision that an endpoint still routes to cannot be deleted, so that error is ignored.
delete_revisions() {
  local prefix="$1" keep="${2:-}" id
  for id in $(aws lambda-web list-web-function-revisions --function-name "$FUNCTION" \
      --query "revisions[?starts_with(description, '$prefix')].revisionId" --output text); do
    [[ "$id" == "$keep" ]] && continue
    aws lambda-web delete-web-function-revision --function-name "$FUNCTION" --revision-id "$id" >/dev/null 2>&1 || true
  done
}

publish_url() {
  echo "$1"
  if [[ -n "${GITHUB_OUTPUT:-}" ]]; then echo "url=$1" >> "$GITHUB_OUTPUT"; fi
}

if [[ "$COMMAND" == "production" || "$COMMAND" == "preview" ]]; then
  GIT_SHA="${GIT_SHA:-$(git -C "$SCRIPT_DIR" rev-parse HEAD 2>/dev/null || echo unknown)}"
fi

case "$COMMAND" in
  production)
    ROLE="$(output ProductionExecutionRoleArn)"
    KEY="production/app.zip"
    if ! aws lambda-web get-web-function --function-name "$FUNCTION" >/dev/null 2>&1; then
      # A Web Function is created together with its first revision and first endpoint. The prod
      # endpoint uses Disabled auto-deployment, so it serves only the revision it is pointed at.
      # With LatestRevision it would serve every new revision, including pull request previews.
      VERSION="$(upload "$KEY")"
      aws lambda-web create-web-function --function-name "$FUNCTION" \
        --revision-config "{\"description\":\"production $GIT_SHA\",\"buildConfig\":$(build_config "$KEY" "$VERSION"),\"serviceConfig\":$(service_config "$ROLE")}" \
        --endpoint-config '{"endpointName":"prod","endpointType":"HomeRegion","authType":"ApplicationManaged","autoDeploymentMode":"Disabled"}' >/dev/null
      aws lambda-web wait web-function-endpoint-active --function-name "$FUNCTION" --endpoint-name prod
    else
      REVISION="$(create_revision "production $GIT_SHA" "$KEY" "$ROLE")"
      route prod "$REVISION"
    fi
    publish_url "$(endpoint_url prod)"
    ;;

  preview)
    aws lambda-web get-web-function --function-name "$FUNCTION" >/dev/null 2>&1 || {
      echo "Web Function $FUNCTION does not exist yet. Deploy production first: scripts/deploy.sh production" >&2; exit 1; }
    ENDPOINT="pr-$PR"
    REVISION="$(create_revision "$ENDPOINT $GIT_SHA" "previews/$ENDPOINT/app.zip" "$(output PreviewExecutionRoleArn)")"
    if endpoint_exists "$ENDPOINT"; then
      route "$ENDPOINT" "$REVISION"
      delete_revisions "$ENDPOINT " "$REVISION"
    else
      # Each preview endpoint is capped at 2 execution environments and 100 requests per second.
      if ! aws lambda-web create-web-function-endpoint --function-name "$FUNCTION" --endpoint-name "$ENDPOINT" \
          --endpoint-type HomeRegion --auth-type ApplicationManaged --auto-deployment-mode Disabled \
          --revision-weights "$(weights "$REVISION")" \
          --scaling-config '{"maxEnvironments":2}' --throttle-config '{"rateLimit":100}' >/dev/null 2>"$BUILD_DIR/error.txt"; then
        cat "$BUILD_DIR/error.txt" >&2
        if grep -q ServiceQuotaExceededException "$BUILD_DIR/error.txt"; then
          echo "A Web Function has at most 10 endpoints: prod and 9 previews. Close a pull request or run scripts/deploy.sh delete-preview <number>." >&2
        fi
        delete_revisions "$ENDPOINT "
        exit 1
      fi
      aws lambda-web wait web-function-endpoint-active --function-name "$FUNCTION" --endpoint-name "$ENDPOINT"
    fi
    publish_url "$(endpoint_url "$ENDPOINT")"
    ;;

  delete-preview)
    ENDPOINT="pr-$PR"
    if ! endpoint_exists "$ENDPOINT"; then
      echo "No preview $ENDPOINT to delete"
      exit 0
    fi
    aws lambda-web delete-web-function-endpoint --function-name "$FUNCTION" --endpoint-name "$ENDPOINT" >/dev/null
    aws lambda-web wait web-function-endpoint-deleted --function-name "$FUNCTION" --endpoint-name "$ENDPOINT"
    delete_revisions "$ENDPOINT "
    echo "Deleted preview $ENDPOINT"
    ;;

  destroy)
    # Deleting a Web Function also deletes its endpoints and revisions.
    if aws lambda-web get-web-function --function-name "$FUNCTION" >/dev/null 2>&1; then
      aws lambda-web delete-web-function --function-name "$FUNCTION" >/dev/null
      aws lambda-web wait web-function-deleted --function-name "$FUNCTION"
      echo "Deleted Web Function $FUNCTION"
    fi
    # The bucket is versioned, so delete every object version and delete marker.
    while true; do
      batch="$(aws s3api list-object-versions --bucket "$BUCKET" --max-items 500 --output json \
        --query '{Objects: [Versions, DeleteMarkers][][].{Key: Key, VersionId: VersionId}}')"
      [[ "$batch" == *'"Key"'* ]] || break
      aws s3api delete-objects --bucket "$BUCKET" --delete "$batch" >/dev/null
    done
    echo "Emptied bucket $BUCKET. Now run sam delete."
    ;;
esac
