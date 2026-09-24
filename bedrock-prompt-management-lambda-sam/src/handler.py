"""Invoke a managed, versioned Amazon Bedrock prompt via the Converse API.

The prompt template and its variables live in Amazon Bedrock (Prompt Management), not in
this code. Converse accepts the prompt version ARN as its modelId, fetches the managed
prompt, substitutes the promptVariables, and runs it against the configured model. To change
the prompt, publish a new version in Bedrock and repoint PROMPT_VERSION_ARN - no code change.
"""
import os
import boto3

bedrock = boto3.client("bedrock-runtime")

PROMPT_VERSION_ARN = os.environ["PROMPT_VERSION_ARN"]
DEFAULT_TEXT = (
    "Amazon S3 is object storage built to store and retrieve any amount of data "
    "from anywhere, offering industry-leading scalability, availability, and durability."
)


def handler(event, context):
    text = (event or {}).get("input") or DEFAULT_TEXT
    response = bedrock.converse(
        modelId=PROMPT_VERSION_ARN,
        promptVariables={"input": {"text": text}},
    )
    summary = response["output"]["message"]["content"][0]["text"]
    print("Invoked prompt version: " + PROMPT_VERSION_ARN)
    print("Summary: " + summary)
    return {"summary": summary}
