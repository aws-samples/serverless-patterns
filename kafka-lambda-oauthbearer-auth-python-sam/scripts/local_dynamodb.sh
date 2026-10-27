#!/bin/bash
# =============================================================================
# Start DynamoDB Local for `sam local invoke` and create the consumer's table in
# it, so a local test never writes to the real DynamoDB table.
#
# When `sam local invoke` runs the function it sets AWS_SAM_LOCAL=true, and the
# handler then sends its writes to http://dynamodb-local:8000 instead of
# DynamoDB. That host name resolves only on the Docker network this script
# creates, so the script also records that network (and the sample event) in
# samconfig.toml, which `sam local invoke` reads. Run from the pattern folder:
#
#   bash scripts/local_dynamodb.sh
#   sam build
#   sam local invoke
#
# The client instance runs this at boot, so normally there's nothing to do. The
# container restarts with Docker and keeps its data in the dynamodb-local-data
# volume, so it also survives an instance restart. Re-running the script is
# harmless. To remove DynamoDB Local and its data:
#   docker rm -f dynamodb-local && docker volume rm dynamodb-local-data
# =============================================================================
set -eo pipefail
source /home/ec2-user/kafka_oauth.env

NETWORK=sam-local
CONTAINER=dynamodb-local
PORT=8000
IMAGE=public.ecr.aws/aws-dynamodb-local/aws-dynamodb-local:latest
VOLUME=dynamodb-local-data
# Same default the SAM template's DynamoDBTableName parameter gets
TABLE="${DYNAMODB_TABLE_NAME:-$PATTERN_PREFIX-sam-messages}"
LOCAL="--endpoint-url http://localhost:$PORT"

# The pattern folder holds template.yaml and samconfig.toml. Usually that's the
# folder above this script; fall back to the current one if the script was run
# from a copy elsewhere (the client also copies it to ~/scripts).
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PATTERN_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
[ -f "$PATTERN_DIR/template.yaml" ] || PATTERN_DIR="$PWD"
[ -f "$PATTERN_DIR/template.yaml" ] || { echo "ERROR: run this from the pattern folder (the one with template.yaml)"; exit 1; }

docker network inspect "$NETWORK" >/dev/null 2>&1 || docker network create "$NETWORK" >/dev/null

if ! docker ps --format '{{.Names}}' | grep -qx "$CONTAINER"; then
  docker rm -f "$CONTAINER" >/dev/null 2>&1 || true
  echo "Starting DynamoDB Local ($CONTAINER on network $NETWORK, localhost:$PORT)..."
  # -sharedDb: one database for every caller. Without it DynamoDB Local keeps a
  # separate database per access key and region, and the function's credentials
  # differ from this shell's, so it wouldn't see the table created below.
  # -dbPath on a named volume plus --restart unless-stopped: the table and its
  # items survive container and instance restarts. --user root lets it write to
  # the volume, which Docker creates root-owned.
  docker run -d --name "$CONTAINER" --network "$NETWORK" --restart unless-stopped \
    -p "127.0.0.1:$PORT:8000" -v "$VOLUME:/home/dynamodblocal/data" --user root \
    "$IMAGE" -jar DynamoDBLocal.jar -sharedDb -dbPath /home/dynamodblocal/data >/dev/null
fi

for i in $(seq 1 30); do
  aws dynamodb list-tables $LOCAL --region "$AWS_REGION" >/dev/null 2>&1 && break
  sleep 1
done

if aws dynamodb describe-table $LOCAL --region "$AWS_REGION" --table-name "$TABLE" >/dev/null 2>&1; then
  echo "Table $TABLE already exists in DynamoDB Local."
else
  echo "Creating table $TABLE in DynamoDB Local..."
  aws dynamodb create-table $LOCAL --region "$AWS_REGION" --table-name "$TABLE" \
    --attribute-definitions AttributeName=topicPartition,AttributeType=S AttributeName=offset,AttributeType=N \
    --key-schema AttributeName=topicPartition,KeyType=HASH AttributeName=offset,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST >/dev/null
fi

# Make a plain `sam local invoke` join $NETWORK and use the sample event, by
# setting them under [default.local_invoke.parameters] in samconfig.toml. Any
# other section, such as the one `sam deploy --guided` saves, is left as is.
python3 - "$PATTERN_DIR/samconfig.toml" <<'PY'
import os, re, sys
path = sys.argv[1]
want = {"docker_network": '"sam-local"', "event": '"events/event.json"'}
hdr = "[default.local_invoke.parameters]"
s = open(path).read() if os.path.exists(path) else "version = 0.1\n"
if hdr in s:
    start = s.index(hdr) + len(hdr)
    nxt = re.search(r"^\[", s[start:], re.M)
    end = start + nxt.start() if nxt else len(s)
    body = s[start:end]
    for k, v in want.items():
        if re.search(rf"^{k}\s*=", body, re.M):
            body = re.sub(rf"^{k}\s*=.*$", f"{k} = {v}", body, flags=re.M)
        else:
            body = body.rstrip("\n") + f"\n{k} = {v}\n" + ("\n" if nxt else "")
    s = s[:start] + body + s[end:]
else:
    s = s.rstrip("\n") + f"\n\n{hdr}\n" + "".join(f"{k} = {v}\n" for k, v in want.items())
open(path, "w").write(s)
PY
# Also give `sam deploy` the tag the client instance's IAM role looks for on SAM
# stacks (kafka-sample=<prefix>), and a default stack name (SAM's own default is
# sam-app). The stack name can be anything; the tag is what matters.
python3 - "$PATTERN_DIR/samconfig.toml" "$STACK_NAME-sam" "kafka-sample=$PATTERN_PREFIX" <<'PY'
import re, sys
path, stack, tag = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(path).read()
hdr = "[default.deploy.parameters]"
if hdr not in s:
    s = s.rstrip("\n") + f"\n\n{hdr}\n"
start = s.index(hdr) + len(hdr)
nxt = re.search(r"^\[", s[start:], re.M)
end = start + nxt.start() if nxt else len(s)
section = s[start:end]
m = re.search(r'^tags\s*=\s*"(.*)"', section, re.M)
if not m:
    section = f"\ntags = \"{tag}\"" + section
elif tag.split("=")[0] + "=" not in m.group(1):
    section = section[:m.start(1)] + (m.group(1) + " " + tag).strip() + section[m.end(1):]
if not re.search(r"^stack_name\s*=", section, re.M):
    section = f"\nstack_name = \"{stack}\"" + section
s = s[:start] + section + s[end:]
open(path, "w").write(s)
PY
echo "Set docker_network and event for sam local invoke, and the stack tag and name for sam deploy, in $PATTERN_DIR/samconfig.toml."

cat <<EOF

DynamoDB Local is ready. Run the function against it with:
  sam local invoke

Then look at what it wrote:
  aws dynamodb scan --endpoint-url http://localhost:$PORT --region $AWS_REGION --table-name $TABLE
EOF
