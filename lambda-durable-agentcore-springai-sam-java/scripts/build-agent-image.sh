#!/bin/bash
#
# Builds the Spring AI agent as an ARM64 container image and pushes it to ECR.
#
# AgentCore Runtime can host plain source code only for Python and Node, so a Java agent must
# be delivered as a container image. SAM cannot build it for us either: its Metadata/Dockerfile
# support applies to PackageType: Image Lambda functions and builds for the host architecture.
# So the image is produced here, before `sam deploy`, and its URI is passed in as a parameter.
#
# Usage: ./scripts/build-agent-image.sh [region] [repository-name]

set -euo pipefail

REGION="${1:-${AWS_REGION:-us-east-1}}"
REPO_NAME="${2:-document-review-agent}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)/agent"

# Prefer docker, fall back to finch, nerdctl or podman.
CONTAINER_CLI=""
for candidate in docker finch nerdctl podman; do
    if command -v "$candidate" >/dev/null 2>&1; then
        CONTAINER_CLI="$candidate"
        break
    fi
done
if [[ -z "$CONTAINER_CLI" ]]; then
    echo "ERROR: no container CLI found (looked for docker, finch, nerdctl, podman)." >&2
    exit 1
fi

command -v aws >/dev/null 2>&1 || { echo "ERROR: aws CLI is not installed." >&2; exit 1; }

if command -v mvn >/dev/null 2>&1; then
    MVN=mvn
elif [[ -n "${MAVEN_HOME:-}" && -x "${MAVEN_HOME}/bin/mvn" ]]; then
    MVN="${MAVEN_HOME}/bin/mvn"
else
    echo "ERROR: Maven is not installed or not on PATH." >&2
    exit 1
fi

ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
REGISTRY="${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"
IMAGE_URI="${REGISTRY}/${REPO_NAME}"

echo "==> Building the Spring AI agent jar"
"$MVN" -q -f "${AGENT_DIR}/pom.xml" clean package -DskipTests

echo "==> Ensuring ECR repository '${REPO_NAME}' exists in ${REGION}"
if ! aws ecr describe-repositories --repository-names "$REPO_NAME" --region "$REGION" >/dev/null 2>&1; then
    aws ecr create-repository \
        --repository-name "$REPO_NAME" \
        --region "$REGION" \
        --image-scanning-configuration scanOnPush=true >/dev/null
    echo "    created"
else
    echo "    already exists"
fi

echo "==> Logging in to ECR"
aws ecr get-login-password --region "$REGION" \
    | "$CONTAINER_CLI" login --username AWS --password-stdin "$REGISTRY"

# A content-independent but unique tag; AgentCore requires an explicit tag (not :latest only)
# and a new tag makes each deployment an unambiguous update.
TAG="$(date +%Y%m%d%H%M%S)"

echo "==> Building ARM64 image with ${CONTAINER_CLI}"
"$CONTAINER_CLI" build \
    --platform linux/arm64 \
    -t "${IMAGE_URI}:${TAG}" \
    -t "${IMAGE_URI}:latest" \
    "$AGENT_DIR"

echo "==> Pushing"
"$CONTAINER_CLI" push "${IMAGE_URI}:${TAG}"
"$CONTAINER_CLI" push "${IMAGE_URI}:latest"

cat <<EOF

==> Done.

Image: ${IMAGE_URI}:${TAG}

Deploy with:

  sam deploy --guided --parameter-overrides \\
      ApproverEmail=you@example.com \\
      AgentImageUri=${IMAGE_URI}:${TAG}

EOF
