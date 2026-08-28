# Manage and version GenAI prompts with Amazon Bedrock Prompt Management

This pattern defines an Amazon Bedrock managed prompt and a published version as native CloudFormation resources, and invokes the prompt from AWS Lambda through the Bedrock Converse API. The prompt text lives in Bedrock, not in the function, so you can update or roll back the prompt by publishing a new version, with no function code change.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/bedrock-prompt-management-lambda-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## How it works

```
   {"input": "..."}          Converse (modelId = prompt version ARN,
        |                                promptVariables = {...})
        v                                        |
   AWS Lambda  --------------------------------> Amazon Bedrock
   (no prompt text,                     managed prompt + published version
    only the version ARN)               (template, variables, model)
```

- `AWS::Bedrock::Prompt` defines the prompt: template text with `{{variables}}`, the target model, and inference settings.
- `AWS::Bedrock::PromptVersion` publishes an immutable version of that prompt.
- The Lambda function calls `Converse` with the prompt version ARN as `modelId` and supplies `promptVariables`. Bedrock fetches the managed prompt, fills the variables, and runs the model.
- To change behaviour, publish a new version and repoint the function (a configuration value), or roll back to an older version - the function code never changes.

## Requirements

- An AWS account with permissions for AWS Lambda and Amazon Bedrock, and access to the chosen Bedrock model in your Region.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) v2.
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).

## Deployment

```bash
sam build
sam deploy --guided
#   - Stack Name : bedrock-prompt-management
#   - AWS Region : us-east-1 (or a Region where the model is available)
#   - ModelId    : us.amazon.nova-lite-v1:0 (default; any Converse-compatible model or inference profile)
```

Note the `InvokePromptFunctionName` and `PromptArn` outputs.

## Testing

### 1. Invoke the managed prompt

```bash
FN=<the InvokePromptFunctionName output>
echo {\"input\":\"AWS Lambda runs code in response to events and scales automatically.\"} > event.json
aws lambda invoke --function-name $FN --cli-binary-format raw-in-base64-out --payload file://event.json out.json
cat out.json
```

You get a one-sentence summary, produced by the managed prompt (the function holds no prompt text).

### 2. Change the prompt without changing code

Edit the prompt, publish a new version, and repoint the function. The output changes; `handler.py` does not.

```bash
PID=<the prompt id, the last part of the PromptArn output>

# Update the draft template (here: bullet points instead of one sentence)
aws bedrock-agent update-prompt --prompt-identifier $PID --name bedrock-prompt-management-summary-prompt \
  --default-variant v1 --variants "[{\"name\":\"v1\",\"templateType\":\"TEXT\",\"modelId\":\"us.amazon.nova-lite-v1:0\",\"templateConfiguration\":{\"text\":{\"text\":\"Rewrite the following as exactly three concise bullet points:\\n\\n{{input}}\",\"inputVariables\":[{\"name\":\"input\"}]}}}]"

# Publish version 2 and note its ARN
V2=$(aws bedrock-agent create-prompt-version --prompt-identifier $PID --query arn --output text)

# Repoint the function to v2 (configuration, not code) and re-invoke
aws lambda update-function-configuration --function-name $FN --environment "Variables={PROMPT_VERSION_ARN=$V2}"
sleep 6
aws lambda invoke --function-name $FN --cli-binary-format raw-in-base64-out --payload file://event.json out2.json; cat out2.json
```

The response is now bullet points. Roll back by pointing `PROMPT_VERSION_ARN` at the earlier version ARN.

## Cleanup

```bash
sam delete
```

----

Author: Manish S

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved. SPDX-License-Identifier: MIT-0
