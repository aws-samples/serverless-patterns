# Travel Service with AI Agent, OpenSearch, and Lambda using AWS CDK .NET

This pattern demonstrates how to create a serverless travel service using Amazon Bedrock Agent, Amazon OpenSearch for vector search, AWS Lambda for processing, and Amazon S3 for data storage. The pattern includes a flight search feature and is implemented using AWS CDK with .NET.

Learn more about this pattern at Serverless Land Patterns: [Add your pattern link here]

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Architecture
![Architecture](./alb-ecs-bedrock-agents-cdk-dotnet-arch.png)

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
* [.NET](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) (.NET 8.0 or later) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change the working directory to this pattern's directory:
    ```
    cd alb-ecs-bedrock-agents-cdk-dotnet
    ```
3. Build the .NET CDK project:
    ```
    dotnet build src
    ```
4. Deploy the stack to your default AWS account and region.

**Please be aware that the deploy command will take about 5-15 minutes to complete**

The output of this command should give you the API Gateway endpoint URL:
    ```
    cdk deploy
    ```
5. Other useful commands:
    ```
    cdk diff         compare deployed stack with current state    
    cdk synth        emits the synthesized CloudFormation template
    ```

## How it works

This pattern creates a serverless travel service:

1. An agent powered by Amazon Bedrock interacts with customers and handles their travel-related queries.
2. Knowledge base documents are stored in Amazon S3 and indexed in Amazon OpenSearch for quick retrieval.
3. When a flight search is requested, an AWS Lambda function is triggered from Bedrock Agent Action-Group. The Lambda function processes the request and returns mock flight data.
4. When policy related questions are asked, Bedrock knowledge based is used to answer the questions.
5. All components are secured with appropriate IAM roles and permissions.

The AWS CDK is used to define and deploy all the necessary AWS resources, including the Bedrock Agent, Bedrock KnowledgeBase, OpenSearch Serverless Collection, Lambda functions, S3 bucket and associated IAM roles and permissions.

## Testing

1. Use the agent to interact with the travel service:
   - You can use the AWS Console to interact with the Bedrock agent and test various travel-related queries.

2. Testing the solution
    - Install `jq` for formatted output. (you can omit it from command-line)
        - On Ubuntu/Debian
        ```
        sudo apt install jq
        ```
        - On CentOS/RHEL
        ```
        sudo yum install jq
        ```
        - On macOS
        ```
        brew install jq
        ```

    - Test the flight search feature:
        - Use the `curl` to send a request to the ALB endpoint (replace `<AlbEndpoint>` with the actual URL from the CDK output).
        - Update `<session-id>` to a meaningful value.        

        ```bash
        curl -X POST \
        http://<AlbEndpoint>/message \
        -H "Accept: application/json" \
        -H "Content-Type: application/json" \
        -d '{
            "SessionId": "<session-id>",
            "Message": "I am looking for a flight for 2 people from SEA to JFK on coming 31st of December 2024 and coming back on 7th of January.",
            "EndSession": false,
            "EnableTrace": false,
            "SessionAttributes": {},
            "PromptSessionAttributes": {}
        }' \
        -v | jq .
        ```
    - You can also test the agent's ability to answer questions about travel policies by asking it various policy-related questions.
        - Use the `curl` to send a request to the ALB endpoint (replace `<AlbEndpoint>` with the actual URL from the CDK output).
        - Update `<session-id>` to a meaningful value.

        ```bash
        curl -X POST \
        http://<AlbEndpoint>/message \
        -H "Accept: application/json" \
        -H "Content-Type: application/json" \
        -d '{
            "SessionId": "<session-id>",
            "Message": "I am looking for reservation policy and transportation policy.",
            "EndSession": false,
            "EnableTrace": false,
            "SessionAttributes": {},
            "PromptSessionAttributes": {}
        }' \
        -v | jq .
        ```

    - Test using test application.
        - You can also use test application to chat with Bedrock Agent.
        - Go to `Test` directory from command prompt.
        ```
        cd ./src/Test
        ```
        - Update `<AlbEndpoint>` in `appsettings.json` file.
        - Update `enableTrace` to `true` if need to check request traces from Bedrock Agents. Traces will be written to a file.
        - Run Test application.
        ```
        dotnet run
        ```
        - Press `CTRL+C` to exit the application.

3. Check the CloudWatch Logs for the Lambda function to see the processing details and any potential errors.

## Cleanup
 
1. Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
    ```
    cdk destroy
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0