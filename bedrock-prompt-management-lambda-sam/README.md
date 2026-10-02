# Version generative AI prompts with Amazon Bedrock Prompt Management

This pattern defines an Amazon Bedrock managed prompt and a published prompt version as native AWS CloudFormation resources, and invokes that prompt from AWS Lambda through the Amazon Bedrock Converse API. The prompt text lives in Amazon Bedrock Prompt Management, not in the function, so you change or roll back the prompt by publishing a new version and repointing the function at it, with no function code change.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/bedrock-prompt-management-lambda-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

```
   {"input": "..."}          Converse (modelId = prompt version ARN,
        |                              promptVariables = {...})
        v                                      |
   AWS Lambda  ------------------------------> Amazon Bedrock
   (no prompt text,                   managed prompt + published version
    only the version ARN)             (template, variables, model)
```

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* Access to the Amazon Bedrock model the prompt targets. The default `ModelId` is `us.amazon.nova-lite-v1:0`, an Amazon Nova Lite cross-Region inference profile for the US geography. Access to Amazon Bedrock foundation models is enabled by default in commercial AWS Regions when the calling principal has the required AWS Marketplace permissions; see [Request access to models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) and check the model in the Amazon Bedrock console before deploying.
* An AWS Region where Amazon Bedrock Prompt Management and the chosen model or inference profile are available. This pattern was tested in `us-east-1`. For the Regions a cross-Region inference profile can route to, see [Supported Regions and models for inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html).

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/bedrock-prompt-management-lambda-sam
    ```
1. The function has a Python dependency, so build it first, then deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region (the Region must offer Amazon Bedrock Prompt Management and the model you choose)
    * Parameter ModelId: press Enter to accept the default `us.amazon.nova-lite-v1:0`, or enter another Converse-compatible Amazon Bedrock model identifier or inference profile identifier
    * Parameter PromptRevision: press Enter to accept the default `1`. Bump this value on a later deployment, after you edit the prompt or `ModelId` in template.yaml, to publish a new prompt version (see Notes)
    * Confirm changes before deploy: press Enter for the default `N`, or enter `y` to review the changeset first
    * Allow SAM CLI IAM role creation: press Enter to accept the default `Y`. The template creates the function execution role, so this must be allowed
    * Disable rollback: press Enter for the default `N`
    * Save arguments to configuration file: press Enter to accept the default `Y`, keep the default file name `samconfig.toml` and the default environment `default`

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing: `InvokePromptFunctionName`, `PromptArn`, `PromptVersionArn` (the rollback value used in Testing step 3) and `LogGroupName`.

## How it works

* `AWS::Bedrock::Prompt` defines the prompt: the template text with `{{variables}}`, the input variables, the target model, and the inference settings (temperature and maximum tokens).
* `AWS::Bedrock::PromptVersion` publishes an immutable version of that prompt. The draft stays editable; the published version does not change.
* The AWS Lambda function calls Converse with the prompt version ARN as `modelId` and supplies `promptVariables`. Amazon Bedrock renders the managed prompt with those values and runs it against the model the prompt variant targets, so the function carries no prompt text, only the version ARN it reads from the `PROMPT_VERSION_ARN` environment variable.
* Because a prompt from Prompt Management owns the inference settings, Converse rejects `inferenceConfig`, `system`, `toolConfig` and `additionalModelRequestFields` in the same request (Amazon Bedrock API Reference, [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html)).
* To change behavior, publish a new version and repoint the function at it, or point it back at an older version. The function code never changes.
* The execution role is scoped to `bedrock:RenderPrompt` on this prompt and its versions, which is the permission Converse checks for a prompt resource, plus `bedrock:InvokeModel` on the model the prompt variant targets.

## Testing

The commands below work in both `bash` and `zsh`. Amazon Bedrock Prompt Management is part of the Amazon Bedrock control plane, so its commands live under `aws bedrock-agent` (for example `get-prompt`, `update-prompt`, `create-prompt-version`), while inference runs through `aws bedrock-runtime`.

1. Set the Region you deployed to and the function name from the `InvokePromptFunctionName` output, write a test event, and invoke the function:

    ```bash
    export AWS_REGION=<the AWS Region you deployed to>
    FN=<the InvokePromptFunctionName output>
    echo '{"input":"AWS Lambda runs code in response to events and scales automatically."}' > event.json
    aws lambda invoke --function-name $FN --cli-binary-format raw-in-base64-out --payload file://event.json out.json
    cat out.json
    ```

    The invoke call prints the status, and `out.json` holds a one-sentence summary produced by the managed prompt:

    ```
    {
        "StatusCode": 200,
        "ExecutedVersion": "$LATEST"
    }
    {"summary": "AWS Lambda automatically executes code in reaction to events and adjusts its capacity accordingly."}
    ```

    The prompt runs at temperature 0.5, so the exact wording differs from run to run; only the one-sentence shape is fixed by the prompt template.

2. Change the prompt without changing code. Edit the draft, publish it as a new version, and repoint the function. The commands read the current prompt name and model identifier back and send them again, because `update-prompt` replaces the prompt wholesale: hardcoding them would rename the stack's prompt or switch its model. The inference configuration is the value set in template.yaml, and it has to be repeated for the same reason.

    ```bash
    PID=<the prompt id, the last part of the PromptArn output>
    PNAME=$(aws bedrock-agent get-prompt --prompt-identifier $PID --query name --output text)
    MID=$(aws bedrock-agent get-prompt --prompt-identifier $PID --query 'variants[0].modelId' --output text)
    aws bedrock-agent update-prompt --prompt-identifier "$PID" --name "$PNAME" --default-variant v1 \
      --variants '[{"name":"v1","templateType":"TEXT","modelId":"'"$MID"'","templateConfiguration":{"text":{"text":"Rewrite the following as exactly three concise bullet points:\n\n{{input}}","inputVariables":[{"name":"input"}]}},"inferenceConfiguration":{"text":{"temperature":0.5,"maxTokens":300}}}]'
    V2=$(aws bedrock-agent create-prompt-version --prompt-identifier "$PID" --query arn --output text)
    aws lambda update-function-configuration --function-name $FN --environment "Variables={PROMPT_VERSION_ARN=$V2}"
    aws lambda wait function-updated-v2 --function-name $FN
    aws lambda invoke --function-name $FN --cli-binary-format raw-in-base64-out --payload file://event.json out2.json
    cat out2.json
    ```

    The same input now comes back as bullet points, from the same unchanged function code:

    ```
    {"summary": "- AWS Lambda executes code triggered by events.\n- It scales automatically based on demand.\n- Provides seamless event-driven computing."}
    ```

    Confirm that only the template text changed:

    ```bash
    aws bedrock-agent get-prompt --prompt-identifier $PID --query '{name:name,modelId:variants[0].modelId,inferenceConfiguration:variants[0].inferenceConfiguration}'
    ```

    ```
    {
        "name": "<your stack name>-summary-prompt",
        "modelId": "us.amazon.nova-lite-v1:0",
        "inferenceConfiguration": {
            "text": {
                "temperature": 0.5,
                "maxTokens": 300
            }
        }
    }
    ```

3. Roll back to the version the stack published. Repointing the function in step 2 is deliberate configuration drift from the stack: the stack still records version 1 in the `PromptVersionArn` output, while the live function points at version 2. An unchanged `sam deploy` does not correct that, because AWS CloudFormation finds no template change to make and reports `Error: No changes to deploy`. Roll back explicitly with the `PromptVersionArn` output:

    ```bash
    ARN=<the PromptVersionArn output>
    aws lambda update-function-configuration --function-name $FN --environment "Variables={PROMPT_VERSION_ARN=$ARN}"
    aws lambda wait function-updated-v2 --function-name $FN
    aws lambda invoke --function-name $FN --cli-binary-format raw-in-base64-out --payload file://event.json out3.json
    cat out3.json
    ```

    The output is a single sentence again. A stack update that does change the function, such as a deployment with a new `PromptRevision`, also resets `PROMPT_VERSION_ARN` to whatever the template says.

    Note that `update-function-configuration --environment` replaces the whole environment variable map. This template has only `PROMPT_VERSION_ARN`, so a single assignment is safe here; if you add variables, repeat all of them in the command.

4. The function logs the prompt version it invoked and the length of the summary, never the model output. Read them from the stack's log group:

    ```bash
    aws logs tail <the LogGroupName output> --since 10m
    ```

    ```
    2026-10-02T17:27:21.858000+00:00 2026/10/02/<function>[$LATEST]1c49e5ae Invoked prompt version: arn:aws:bedrock:us-east-1:111122223333:prompt/ABCDEFGHIJ:4 summary_length=95
    ```

## Notes

* Editing the prompt text or `ModelId` in template.yaml and redeploying updates only the prompt draft. `AWS::Bedrock::PromptVersion` is replaced only when one of its own properties changes, so the published version, and therefore the version the function invokes, stays as it was. To publish the edited draft as a new version, change the prompt and increment the `PromptRevision` parameter in the same deployment: its value is interpolated into the version description, which forces a replacement and a new version ARN.
* A stack update also rewrites the prompt draft from template.yaml, so draft edits made with `aws bedrock-agent update-prompt` are discarded on the next deployment. Keep prompt wording you want to keep in template.yaml.
* The function accepts the event `{"input": "text to summarize"}`. If the `input` key is absent, for example an empty test event `{}`, the function summarizes a short piece of sample text so that a first test returns something. An `input` key that is present but empty or blank is rejected with `"input" must be a non-empty string.`, and an event that is not a JSON object is rejected the same way, rather than silently summarizing the sample text.
* If Amazon Bedrock denies the Converse call, the function raises a message naming the prompt version ARN and the permissions and model access to check, which is the most likely first-run failure.
* `bedrock:InvokeModel` is granted on `foundation-model/*` in every Region on purpose. A cross-Region inference profile such as the default `us.amazon.nova-lite-v1:0` routes a request to a Region that Amazon Bedrock selects inside the profile's geography ([cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)), so the foundation model that serves the call cannot be pinned to one Region. The inference profile itself is scoped to the exact `ModelId` the stack deploys.

## Cleanup

1. Delete the stack, confirming both prompts the AWS SAM CLI shows. This deletes the managed prompt with every version published from it, including the versions you published during testing, along with the function, its execution role and its log group:
    ```bash
    sam delete --stack-name STACK_NAME --region REGION
    ```
    Pass `--region` explicitly: unlike the AWS CLI, `sam delete` does not read the `AWS_REGION` environment variable, so without it the AWS SAM CLI looks for the stack in the Region configured in your AWS profile.
1. Delete the local files created during testing:
    ```bash
    rm -f event.json out.json out2.json out3.json
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
