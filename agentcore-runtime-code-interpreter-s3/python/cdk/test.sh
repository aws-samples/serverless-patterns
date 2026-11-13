#!/usr/bin/env bash
# Test the deployed agent with the sample files from samples/generate.py.
# Uploads the files to the bucket if they aren't there yet, then asks the agent about them.
# Set STACK_NAME if you deployed the stack under a different name.
set -euo pipefail
cd "$(dirname "$0")"

STACK_NAME="${STACK_NAME:-AgentCoreRuntimeCodeInterpreterS3Stack}"
PREFIX="demo/"
FILES=(statement.pdf ledger.xlsx)

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install --quiet --disable-pip-version-check -r client/requirements.txt -r samples/requirements.txt

# Ask up front, so the run is hands-off after this. Only ask when a person is at the terminal,
# so the script never waits for input in automation.
answer=n
if [ -t 0 ] && [ -t 1 ]; then
  read -r -p "Show the code that the agent ran after each answer? [y/N] " answer || answer=n
fi
SHOW_LOGS=false
if [[ "$answer" =~ ^[Yy] ]]; then
  SHOW_LOGS=true
fi

BUCKET=$(aws cloudformation describe-stacks --stack-name "$STACK_NAME" \
  --query "Stacks[0].Outputs[?OutputKey=='DocumentBucketName'].OutputValue" --output text)
echo "Bucket: $BUCKET"

missing=()
for file in "${FILES[@]}"; do
  if ! aws s3api head-object --bucket "$BUCKET" --key "$PREFIX$file" > /dev/null 2>&1; then
    missing+=("$file")
  fi
done

if [ ${#missing[@]} -gt 0 ]; then
  echo "Missing from s3://$BUCKET/$PREFIX: ${missing[*]}. Generating and uploading the sample files."
  python samples/generate.py
  for file in "${FILES[@]}"; do
    aws s3 cp "samples/output/$file" "s3://$BUCKET/$PREFIX$file"
  done
  # S3 Files reflects new objects in the file system in the background, so wait before asking. See
  # https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-synchronization.html
  # If the agent reports that a file is missing, run this script again.
  echo "Waiting 60 seconds for the files to appear in the S3 Files file system."
  sleep 60
else
  echo "The sample files are already in s3://$BUCKET/$PREFIX."
fi

# Each question gets its own runtime session, so that client/logs.py can show the code for that question only.
ask() {
  local session_id
  session_id=$(python -c "import uuid; print(uuid.uuid4())")
  echo
  echo "=== $1"
  python client/invoke.py --stack-name "$STACK_NAME" --session-id "$session_id" "$1"

  if [ "$SHOW_LOGS" = true ]; then
    # CloudWatch Logs can take a few seconds to make new log records available.
    echo
    echo "--- Code that the agent ran (waiting 10 seconds for the latest log records to arrive)"
    sleep 10
    python client/logs.py --stack-name "$STACK_NAME" --session-id "$session_id"
  else
    echo
    echo "To see the code that the agent ran for this question, run:"
    echo "  source .venv/bin/activate && python client/logs.py --stack-name $STACK_NAME --session-id $session_id"
  fi
}

ask "Reconcile statement.pdf with ledger.xlsx. List transactions that are only in one of the files and transactions whose amounts differ. Check the PDF's comments and attachments for anything that explains a difference."
ask "What form fields does statement.pdf contain, and what are their values? Is the statement approved? What does its metadata say?"

echo
echo "Compare the answers with the expected findings that samples/generate.py prints."
