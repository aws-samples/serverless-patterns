#!/usr/bin/env bash
# Deploy the stack. Extra arguments are passed to cdk deploy, for example:
#   ./deploy.sh -c availabilityZoneIds=<az-id-1>,<az-id-2>
# See "Choosing Availability Zones" in the README for the zone IDs to use.
set -euo pipefail
cd "$(dirname "$0")"

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install --quiet --disable-pip-version-check -r cdk/requirements.txt -r client/requirements.txt

cd cdk
# Hide the jsii warning about Node.js versions it hasn't been tested with.
export JSII_SILENCE_WARNING_UNTESTED_NODE_VERSION=1
# --require-approval never deploys without asking to confirm the IAM and security group changes.
npx --yes aws-cdk deploy --require-approval never "$@"
