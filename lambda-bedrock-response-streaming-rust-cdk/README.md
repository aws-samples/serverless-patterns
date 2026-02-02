# AWS Lambda and Amazon Bedrock Response Streaming with Rust

This CDK application demonstrates how to write a Lambda function, expose it as a function URL, use the Bedrock ConverseStream API to invoke the Anthropic Claude 3 Haiku model, and then stream a response back to the client using chunked transfer encoding. Written in Rust, it showcases how to efficiently stream responses from Amazon Bedrock to a client. The example serves as a practical illustration of implementing real-time, serverless communication between Bedrock's GenAI capabilities and a client application.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
* [Docker](https://docs.docker.com/engine/install/) installed and running locally (needed for Rust cross-platform Lambda build)
* [Rust](https://www.rust-lang.org/) 🦀 installed with v1.79.0 or higher
* [Cargo Lambda](https://www.cargo-lambda.info/) installed
* [cross](https://github.com/cross-rs/cross) compilation installed for Cargo Lambda: `cargo install cross --git https://github.com/cross-rs/cross`

## Amazon Bedrock Setup Instructions

You must request access to the Bedrock LLM model before you can use it. This example uses `Claude 3 Haiku`, so make sure you have `Access granted` to this model. For more information, see [Model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern's CDK directory:
    ```bash
    cd lambda-bedrock-response-streaming-rust-cdk/cdk
    ```
3. From the command line, use npm to install the development dependencies:  
    ```bash
    npm install
    ```
4. If you haven't done so previously for this account, run this command to bootstrap CDK:
    ```bash
    cdk bootstrap
    ```
5.  Review the CloudFormation template that CDK generates for your stack using the following AWS CDK CLI command:
    ```bash
    cdk synth
    ```
6. Use AWS CDK to deploy your AWS resources
    ```bash
    cdk deploy
    ```

    After the deployment completes, note the URL in the `Outputs` section at the end. The `BedrockStreamerStack.LambdaFunctionURL` followed by the Lambda Function URL (FURL) will be used to invoke the Lambda function. It should look something like:
    
    `https://{YOUR_ID_HERE}.lambda-url.{YOUR_REGION_HERE}.on.aws/`

## How it works

This pattern exposes a public Lambda Function URL (FURL) endpoint where requests can be made. When a request is made to the FURL, the Lambda function initiates a streaming request to Amazon Bedrock using the [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) API. This allows the response from the LLM in Bedrock to start streaming back to the Lambda function as soon as generation begins, without waiting for the entire response to be ready.

Generating Bedrock responses often takes a long time. By using a streaming approach, the Lambda function can immediately start processing the incoming response and writing the data chunks back to the client. The chunks are delievered in real-time to the connected client, providing an extremely interactive user experience.

## Testing

If you deployed the application without any code changes, you've deployed it with `IAM` authorization. You can see the CDK code for it in `./cdk/lib/bedrock-streamer-lambda/bedrock-streamer-stack.ts`

```ts
// Create a Lambda Function URL
const lambdaUrl = streamingLambda.addFunctionUrl({
    authType: lambda.FunctionUrlAuthType.AWS_IAM,
    invokeMode: lambda.InvokeMode.RESPONSE_STREAM,
});
```
Here you can see `authType: lambda.FunctionUrlAuthType.AWS_IAM` is instructing the Lambda function to use `IAM`. However, if you want to make requests to the FURL without credentials, you can change it to `authType: lambda.FunctionUrlAuthType.NONE`. But **BEWARE**, as doing so exposes the FURL to any unauthenticated user.

To make a request to the FURL, you can use a number of different options. This example will use [curl](https://curl.se/) to make the request.

To make the request using `IAM`, you'll need credentials from an `IAM User` or `IAM Role` to sign the requests. The credentials will need permission for the `lambda:InvokeFunctionUrl` action for the deployed Lambda function.

1. In order to use the curl command with `IAM` auth enabled, you can use the `--user access_key:secret_access_key` option. It's a simple way to do it, but if you don't add the keys to environment variables, you could potentially expose them to your command-line history. So for this example, both `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` should be exported as environment variables to your shell (`Bash` in this example)

    ```bash
    curl -v 'https://{YOUR_ID_HERE}.lambda-url.{YOUR_REGION_HERE}.on.aws' \
         -H "X-Amz-Date: $(date -u '+%Y%m%dT%H%M%SZ')" \
         -H 'Content-Type: application/json' \
         --aws-sigv4 'aws:amz:{YOUR_REGION_HERE}:lambda' \
         --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
         --data-raw '{"storyType": "CATS"}' \
         --no-buffer
    ```
    If you're using a temporary IAM user or role, perhaps through an SSO login, you'll likely need to add the session to your `curl` request, so it looks something like this:

    ```bash
    curl -v 'https://{YOUR_ID_HERE}.lambda-url.{YOUR_REGION_HERE}.on.aws' \
         -H "X-Amz-Security-Token: $AWS_SESSION_TOKEN" \
         -H "X-Amz-Date: $(date -u '+%Y%m%dT%H%M%SZ')" \
         -H 'Content-Type: application/json' \
         --aws-sigv4 'aws:amz:{YOUR_REGION_HERE}:lambda' \
         --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
         --data-raw '{"storyType": "DOGS"}' \
         --no-buffer
    ```
    where `AWS_SESSION_TOKEN` is the token for your AWS session. If you're authenticated with SSO, you can get all of these by running this command:

    ```bash
    aws configure export-credentials --format env
    ```

2. If you're not using `IAM` for your Lambda function, you don't need any access keys or sessions. You can simply use the following as an example

    ```bash
    curl -v 'https://{YOUR_ID_HERE}.lambda-url.{YOUR_REGION_HERE}.on.aws' \
         -H 'Content-Type: application/json' \
         --data-raw '{"storyType": "HORSES"}' \
         --no-buffer
    ```

For any of the commands you use, you should get streaming output as it's generated by the LLM. Here's an example of what you might see if you used a `--data-raw '{"storyType": "CATS"}'` entry

```json
{"type":"other","message":null}{"type":"text","message":"Here"}{"type":"text","message":"'s a very"}{"type":"text","message":" short story about cats"}{"type":"text","message":":"}{"type":"text","message":"\n\nThe"}{"type":"text","message":" Curious"}{"type":"text","message":" F"}{"type":"text","message":"eline"}{"type":"text","message":"\n\nWhis"}{"type":"text","message":"kers t"}{"type":"text","message":"witched, eyes"}{"type":"text","message":" narrow"}{"type":"text","message":"ed,"}{"type":"text","message":" the"}{"type":"text","message":" sle"}{"type":"text","message":"ek tab"}{"type":"text","message":"by cat"}{"type":"text","message":" cr"}{"type":"text","message":"ept"}{"type":"text","message":" forwar"}{"type":"text","message":"d caut"}{"type":"text","message":"iously."}{"type":"text","message":" A"}{"type":"text","message":" new"}{"type":"text","message":" toy"}{"type":"text","message":" ha"}{"type":"text","message":"d caught its"}{"type":"text","message":" attention -"}{"type":"text","message":" a"}{"type":"text","message":" curious"}{"type":"text","message":" contraption that b"}{"type":"text","message":"linked an"}{"type":"text","message":"d whirred."}{"type":"text","message":" With"}{"type":"text","message":" a"}{"type":"text","message":" slight t"}{"type":"text","message":"ilt of the hea"}{"type":"text","message":"d, the"}{"type":"text","message":" feline p"}{"type":"text","message":"ounced,"}{"type":"text","message":" batting"}{"type":"text","message":" at"}{"type":"text","message":" the"}{"type":"text","message":" strange"}{"type":"text","message":" object"}{"type":"text","message":"."}{"type":"text","message":" A"}{"type":"text","message":" flash"}{"type":"text","message":" of light"}{"type":"text","message":","}{"type":"text","message":" a"}{"type":"text","message":" gentle"}{"type":"text","message":" hum"}{"type":"text","message":","}{"type":"text","message":" then silence"}{"type":"text","message":"."}{"type":"text","message":" The"}{"type":"text","message":" cat"}{"type":"text","message":" sat"}{"type":"text","message":" back"}{"type":"text","message":","}{"type":"text","message":" please"}{"type":"text","message":"d with its"}{"type":"text","message":" work,"}{"type":"text","message":" before"}{"type":"text","message":" cur"}{"type":"text","message":"ling up"}{"type":"text","message":" for"}{"type":"text","message":" a well"}{"type":"text","message":"-earned n"}{"type":"text","message":"ap,"}{"type":"text","message":" leaving"}{"type":"text","message":" the"}{"type":"text","message":" dism"}{"type":"text","message":"ant"}{"type":"text","message":"led ga"}{"type":"text","message":"dget behin"}{"type":"text","message":"d."}{"type":"other","message":null}{"type":"other","message":null}{"type":"other","message":null}* Connection #0 to host {YOUR_ID_HERE}.lambda-url.{YOUR_REGION_HERE}.on.aws left intact
```

## Cleanup
 
You can use the following commands to destroy the AWS resources created during deployment. This assumes you're currently at the `lambda-bedrock-response-streaming-rust-cdk/cdk` directory in your terminal:

```bash
cdk destroy
```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
