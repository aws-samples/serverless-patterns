# Bedrock foundational model inference with AWS Lambda with CDK

This pattern demonstrates how to infere a foundational model in Bedrock via a Lambda function.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-bedrock-cdk
    ```

2. Change directory to CDK stack:
    ```
    cd lambda-layer
    ```

3. Run below command to install required dependancies:
    ```
    npm install
    ```
4. If you never used CDK in this account run:
    ```
    cdk bootstrap
    ```

5. From the command line, run:
    ```
    cdk deploy
    ```

## Testing

Verify deployment in the AWS Console and copy function name.

`cd tests`

Grant execution permissions to the `test.sh` script:

`sudo chmod +x test.sh`

Invoke the script with the following parameters:
- `-f [FunctionName]`
- `-m [model]`
- `-e [event]`

Four example payloads are provided for `ClaudeV2` (/tests/events/claude) and `Jurassic-2 Mid` (/test/events/ai21) with the following prompt:

1. "Define 'function' in this context:A Javascript function can be ran asynchronously"
2. "Define 'function' in this context:the promotion required more responsibilities in his job function"
3. "Define 'function' in this context:the engine ran out of fuel and stopped to function"
4. "Define 'function' in this context:the math teacher wrote a function on the blackboard"

Inoke the Lamdba function by passing a numeric value for the event i.e. `-e 1` and desired model, i.e. `-m ai21` and function name, i.e. `-f LambdaLayerStack-LambdaFunctionBF21E41F-XzRF7ZvYq6Kj`

## Invocation example

Lets invoke `Jurassic-2 Mid` with the first event payload:

`./test.sh -f LambdaLayerStack-LambdaFunctionBF21E41F-XzRF7ZvYq6Kj -m ai21 -e 1`

The file `ai21-event1.json` will be created with the response.

A successful response will return:

```
{"statusCode": 200, "model_id": "ai21.j2-mid-v1", "execution_time": [execution time in ms], "body": "[model repsonse]"
```

If an error occures it will return:

```
{"statusCode": 500, "request_body": "[request_body event payload]", "models": "[list of foundational models enabled in Bedrock]"
```

## Cleanup
 
1. To delete the stack, run:
    ```bash
    cdk destroy --all
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0