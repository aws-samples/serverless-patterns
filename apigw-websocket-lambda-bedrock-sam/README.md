# AI Chat Application using Amazon API Gateway (WebSockets), AWS Lambda, and Amazon Bedrock.

This serverless architecture enables real-time AI chat using AWS services. A WebSocket Amazon API Gateway maintains persistent connections between clients and a Node.js AWS Lambda function. The AWS Lambda function handles user connections/disconnections, stores connection IDs in Amazon DynamoDB, and processes messages through an Amazon Bedrock LLM. The system includes error handling, automatic scaling, and pay-per-use pricing. The AWS SAM template provisions all necessary resources and IAM permissions, outputting a WebSocket URL for client connections.


Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/apigw-websockets-lambda-bedrock-sam)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Prerequisites

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [NOTE! Manage Access to Amazon Bedrock Foundation Models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)


## Deployment Instructions 
1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd apigw-websockets-lambda-bedrock-sam
    ```
3. Install dependencies
    ```
    cd src && npm install && cd ..
    ```    
4. From the command line, use AWS SAM build to prepare an application for subsequent steps in the developer workflow, such as local testing or deploying to the AWS Cloud:
    ```
    sam build
    ```    
5. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
6. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the desired BedrockRegion
    * Enter the desired BedrockModelId
    * Allow SAM to create roles with the required permissions if needed.

7. Note the outputs **WebSocket URL** from the SAM deployment process. 
These contain the resource names and/or ARNs which are used for testing.
```bash
wss://<YOUR-WebSocket-URL>.execute-api.<YOUR-AWS-Region>.amazonaws.com/prod
```
 
## Architecture
![apigw-1](images/apigw-ws-lambda-bedrock.png)


## How it Works
WebSocket API Gateway serves as the entry point, enabling bidirectional real-time communication between clients and the backend. It handles three routes:
* $connect - when users join the chat
* $disconnect - when users leave
* $default - for processing chat messages

Lambda Function (Node.js 22.x) acts as the central orchestrator, handling all WebSocket events and business logic. It manages connection lifecycle, processes user messages, and coordinates with other AWS services.
DynamoDB Table stores active WebSocket connection IDs, enabling the system to track which users are currently connected and send responses back to the correct clients.
Amazon Bedrock provides AI capabilities using Claude 3 Sonnet model, processing user messages and generating intelligent responses.

Data Flow:
1. Connection: When a user connects, their connection ID is stored in DynamoDB
2. Message Processing: User sends a message through WebSocket → Lambda receives it → Extracts message content → Sends to Bedrock Claude model
3. AI Response: Bedrock processes the message and returns an AI-generated response
4. Real-time Delivery: Lambda sends the AI response back to the user via WebSocket connection
5. Disconnection: When user disconnects, their connection ID is removed from DynamoDB

## Testing

### Interactive Web Interface
```
To use the test interface:
1. Deploy the application using SAM
2. Copy the WebSocket URL from the deployment outputs
3. Open 'test.html' and update the 'WS_URL' variable with your WebSocket URL and AWS Region
wss://<YOUR-WebSocket-URL>.execute-api.<YOUR-AWS-Region>.amazonaws.com/prod
4. Save 'test.html'
5. Open the HTML file in a browser
6. Click "Connect" to establish a WebSocket connection
7. Type your message and click "Send"
8. When complete Click "Disconnect"
```

### Command Line (wscat)
```bash
npm install -g wscat
wscat -c wss://your-api-id.execute-api.your-region.amazonaws.com/prod
# Then send: {"data": "What is AWS Lambda?"}
```

## Cleanup
1. Delete the stack
    ```bash
    sam delete
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0