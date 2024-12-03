# Streaming Amazon Bedrock response with Amazon API Gateway WebSocket API and AWS Lambda

This CDK application demonstrates a simple, serverless approach to integrating Amazon Bedrock with AWS Lambda and Amazon API Gateway. Written in Rust, it showcases how to efficiently stream responses from Amazon Bedrock to a client via WebSocket connections. The example serves as a practical illustration of implementing real-time, serverless communication between Bedrock's GenAI capabilities and a client application.

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
* [wscat](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-wscat.html) installed for CLI WebSocket capabilities


## Amazon Bedrock Setup Instructions

You must request access to the Bedrock LLM model before you can use it. This example uses `Claude 3 Sonnet`, so make sure you have `Access granted` to this model. For more information, see [Model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern's CDK directory:
    ```bash
    cd apigw-websocket-api-bedrock-streaming-rust-cdk/cdk
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

    After the deployment completes, note the URL in the `Outputs` section at the end. The `BedrockStreamerStack.WebSocketURL` followed by the WebSocket URL will be used to connect to API Gateway. It should look something like `wss://{YOUR_API_ID_HERE}.execute-api.{YOUR_REGION_HERE}.amazonaws.com/prod`

## How it works

This pattern establishes a WebSocket connection to Amazon API Gateway. When requests are made to this API, API Gateway routes them to an AWS Lambda function. The Lambda function then initiates a streaming request to Amazon Bedrock using the [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) API. This allows the response from the LLM in Bedrock to start streaming back to the Lambda function as soon as generation begins, without waiting for the entire response to be ready.

Generating Bedrock responses often takes a long time. By using a streaming approach, the Lambda function can immediately start processing the incoming response and writing the data chunks to the API Gateway WebSocket. The WebSocket then delivers these chunks in real-time to the connected client, providing an extremely interactive user experience.

## Testing

1. From your terminal, use `wscat` to connect to API Gateway using the WebSocket API and generate a short story about `CATS` by entering the `{"storyType": "CATS"}` line after `wscat` startup.
    ```bash
    # Connect to the API Gateway via WebSocket
    wscat -c <API_GATEWAY_URL_FROM_CDK_OUTPUT>

    Connected (press CTRL+C to quit)
    > {"storyType": "CATS"} <--- ENTER THIS...PRESS RETURN
    < {"type":"other","message":null}
    < {"type":"text","message":"Here"}
    < {"type":"text","message":" is"}
    < {"type":"text","message":" a"}
    < {"type":"text","message":" very"}
    < {"type":"text","message":" short"}
    < {"type":"text","message":" story"}
    < {"type":"text","message":" about"}
    < {"type":"text","message":" cats"}
    < {"type":"text","message":":"}
    < {"type":"text","message":"\n\nMitt"}
    < {"type":"text","message":"ens"}
    < {"type":"text","message":" cur"}
    < {"type":"text","message":"le"}
    < {"type":"text","message":"d up"}
    < {"type":"text","message":" on"}
    < {"type":"text","message":" the"}
    < {"type":"text","message":" window"}
    < {"type":"text","message":"s"}
    < {"type":"text","message":"ill"}
    < {"type":"text","message":","}
    .
    .
    < {"type":"other","message":null}
    < {"type":"other","message":null}
    < {"type":"other","message":null}
    > ⏎ <--- CTRL+C HERE>
    ```
2. As the `wscat` CLI says, press `CTRL+C` to disconnect

## Cleanup
 
You can use the following commands to destroy the AWS resources created during deployment. This assumes you're currently at the `apigw-websocket-api-bedrock-streaming-rust-cdk/cdk` directory in your terminal:

```bash
cdk destroy
```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
