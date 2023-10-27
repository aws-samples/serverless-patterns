# AWS Lambda and Amazon Bedrock response streaming

This pattern demonstrates how to write a Lambda function, exposes a function URL, uses the Bedrock InvokeModelWithResponseStreamCommand API to invoke the Anthropic Claude V2 model, and streams the response back to the API client.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-bedrock-response-streaming

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) model enabled (Anthropic Claude V2)
* Install the `@aws-sdk/client-bedrock-runtime` dependency in the src directory: `npm install --prefix src @aws-sdk/client-bedrock-runtime`

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns/lambda-bedrock-response-streaming
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-bedrock-response-streaming
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Once the application is deployed, a public function URL (furl) endpoint is published and available for requests. If you set `AuthType` to `AWS_IAM`, you need credentials from an IAM user or IAM role to sign the requests. The credentials need permission for the `lambda:InvokeFunctionUrl` action for your deployed Lambda function. If you set `AuthType` to `NONE`, you can make requests against the endpoint without any credentials but be aware that any unauthenticated user can invoke your furl.

## Testing

In order to use the curl commands with IAM auth enabled, you can use the `--user access_key:secret_access_key` parameter but this is insecure as it exposes your credentials to the command line history. Alternatively, you can configure a `~/.netrc` file and setup your credentials there. This allows you to instead use `--netrc` which then retrieves the credentials from that file. More details can be found in the [curl](https://everything.curl.dev/usingcurl/netrc) documentation.

You use `events/event.json` for the POST body request:

```json
{
    "bedrockParams": {
        "modelId": "anthropic.claude-v2",
        "contentType": "application/json",
        "accept": "*/*"
    },
    "modelParams": {
        "max_tokens_to_sample": 2048,
        "temperature": 0.5,
        "top_k": 250,
        "top_p": 0.5,
        "prompt": "Explain serverless to a 5th grader."
    }
}
```

You can then invoke your furl with the following curl command: `curl -s -XPOST -d @events/event.json ${FURL_ENDPOINT} --netrc --aws-sigv4 aws:amz:${AWS_REGION}:lambda --no-buffer`

You should see responses from the Anthropic Claude V2 model streamed back to your terminal.

## Cleanup

1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0