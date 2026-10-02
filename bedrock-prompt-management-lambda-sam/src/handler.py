"""Invoke a managed, versioned Amazon Bedrock prompt through the Converse API.

The prompt template and its variables live in Amazon Bedrock Prompt Management, not in this
code. Converse accepts the prompt version ARN as its modelId, renders the managed prompt with
the supplied promptVariables, and runs it against the model configured on the prompt variant.
To change the prompt, publish a new version in Amazon Bedrock and repoint PROMPT_VERSION_ARN,
with no code change.

Event shape: {"input": "text to summarize"}. If "input" is absent the sample text below is used
so that an empty test event still returns something; an "input" key that is present but blank is
rejected, because silently summarizing unrelated text would hide a caller bug.
"""
import os

import boto3
from botocore.exceptions import ClientError

bedrock = boto3.client("bedrock-runtime")

PROMPT_VERSION_ARN = os.environ["PROMPT_VERSION_ARN"]
DEFAULT_TEXT = (
    "Amazon S3 is object storage built to store and retrieve any amount of data "
    "from anywhere, offering industry-leading scalability, availability, and durability."
)


def handler(event, context):
    if not isinstance(event, dict):
        raise ValueError(
            "Event must be a JSON object such as {\"input\": \"text to summarize\"}, "
            "got " + type(event).__name__
        )

    text = event.get("input", DEFAULT_TEXT)
    if not isinstance(text, str) or not text.strip():
        raise ValueError('"input" must be a non-empty string.')

    try:
        response = bedrock.converse(
            modelId=PROMPT_VERSION_ARN,
            promptVariables={"input": {"text": text}},
        )
    except ClientError as error:
        code = error.response.get("Error", {}).get("Code")
        if code == "AccessDeniedException":
            raise RuntimeError(
                "Amazon Bedrock denied the Converse call on " + PROMPT_VERSION_ARN + ". "
                "Check that the execution role has bedrock:RenderPrompt on the prompt and its "
                "versions and bedrock:InvokeModel on the model the prompt variant targets, and "
                "that the account has access to that model in this Region. See "
                "https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html"
            ) from error
        raise

    content = response.get("output", {}).get("message", {}).get("content") or []
    if not content or "text" not in content[0]:
        raise RuntimeError(
            "Converse returned no text content for " + PROMPT_VERSION_ARN
            + "; stopReason=" + str(response.get("stopReason"))
        )

    summary = content[0]["text"]
    # Log the version that ran and the size of the result, never the model output itself.
    print(
        "Invoked prompt version: " + PROMPT_VERSION_ARN
        + " summary_length=" + str(len(summary))
    )
    return {"summary": summary}
