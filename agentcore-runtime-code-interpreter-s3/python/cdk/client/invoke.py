"""Send a prompt to the deployed agent and print the streamed response as it arrives.

Usage: python invoke.py "<prompt>" [--stack-name NAME] [--session-id ID]
"""
import argparse
import json
import sys
import uuid

import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

DEFAULT_STACK_NAME = "AgentCoreRuntimeCodeInterpreterS3Stack"


def get_stack_output(stack_name: str, key: str) -> str:
    try:
        stack = boto3.client("cloudformation").describe_stacks(StackName=stack_name)["Stacks"][0]
    except ClientError as error:
        sys.exit(f"Can't read stack {stack_name}: {error}. Deploy it first, or pass --stack-name.")
    outputs = {o["OutputKey"]: o["OutputValue"] for o in stack.get("Outputs", [])}
    if key not in outputs:
        sys.exit(f"Stack {stack_name} has no {key} output. Deploy the latest version of this pattern's stack.")
    return outputs[key]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("prompt")
    parser.add_argument("--stack-name", default=DEFAULT_STACK_NAME)
    # runtimeSessionId must be 33 to 256 characters long; a UUID has 36. See
    # https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeAgentRuntime.html
    parser.add_argument("--session-id", default=str(uuid.uuid4()),
                        help="Runtime session ID (at least 33 characters). Defaults to a new UUID.")
    args = parser.parse_args()

    # The agent sends nothing while its code runs in the Code Interpreter, which can take several minutes,
    # so wait up to 15 minutes, the session lifetime, instead of botocore's default 60 seconds.
    # No retries, so that a timeout never sends the same prompt to the agent again.
    # https://docs.aws.amazon.com/botocore/latest/reference/config.html
    # https://docs.aws.amazon.com/boto3/latest/guide/retries.html
    client = boto3.client("bedrock-agentcore", config=Config(read_timeout=900, retries={"total_max_attempts": 1}))
    try:
        response = client.invoke_agent_runtime(
            agentRuntimeArn=get_stack_output(args.stack_name, "AgentRuntimeArn"),
            runtimeSessionId=args.session_id,
            contentType="application/json",
            accept="text/event-stream",
            payload=json.dumps({"prompt": args.prompt}).encode(),
        )
    except ClientError as error:
        sys.exit(f"Invocation failed: {error}")
    # stderr keeps the session ID out of the answer; pass it to logs.py to see the code the agent ran.
    print(f"Session ID: {args.session_id}", file=sys.stderr)

    # The agent streams server-sent events; each "data:" line holds one JSON-encoded chunk:
    # https://github.com/aws/bedrock-agentcore-sdk-python/blob/v1.25.4/src/bedrock_agentcore/runtime/app.py#L926
    # chunk_size=1 prints each line as soon as it arrives; the default (1024) waits for 1 KB. See iter_lines in
    # https://docs.aws.amazon.com/botocore/latest/reference/response.html
    for line in response["response"].iter_lines(chunk_size=1):
        if not line.startswith(b"data: "):
            continue
        chunk = json.loads(line[len(b"data: "):])
        if isinstance(chunk, dict) and "error" in chunk:
            sys.exit(f"Agent error: {chunk['error']}")
        print(chunk, end="", flush=True)
    print()


if __name__ == "__main__":
    main()
