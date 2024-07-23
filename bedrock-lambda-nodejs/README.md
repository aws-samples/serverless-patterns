# Amazon Bedrock integration in AWS Lambda (NodeJS Runtime)

This pattern shows how to make use of Amazon Bedrock in a Lambda function with NodeJS runtime.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/bedrock-lambda-nodejs](https://serverlessland.com/patterns/bedrock-lambda-nodejs)
Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd bedrock-lambda-nodejs
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern illustrates how to use the Amazon Bedrock Client for NodeJs.  
The business logic is in <code>./src/index.js</code>.  
You can use sample payloads stored in <code>./events</code> to test the function.
  
The following is the prompt used in the function and sent to Bedrock.

```
provide a summary of the following text in 5 bulletpoints; 
extract 5 tags to categorize the article in a CMS;
provide output as a json object with properties :
"summary" as a list of bulletpoints and "tags" as a list of tags;
<text> YOUR TEXT HERE</text>
```

### Expected Output

```json
{
  "summary": [
    "Amazon Bedrock has been announced in preview in April.",
    "A few days ago, it has been made general available.",
    "Bedrock allows you to use foundational models for generative AI, totally managed.",
    "It's the serverless generative AI service.",
    "Bedrock is available in two regions."
  ],
  "tags": [
    "Amazon",
    "Bedrock",
    "Generative AI",
    "Serverless"
  ]
}
```

## Testing
Invoke the Lambda function with the following command
```bash
aws lambda invoke \
    --region ${AWS_REGION} \
    --function-name ${FUNCTION_NAME} \
    --cli-binary-format raw-in-base64-out \
    --payload file://events/event-${EVENT_NUMBER}.json \
    response.json
```

It will write the function response object to `./response.json`

| Variable | Description | Sample Value |
| --- | --- | --- |
| `${AWS_REGION}` | AWS Region in which your stack is deployed. | `us-west-2` |
| `${FUNCTION_NAME}` | Name of your function. You can find it in the exports of the stack. | `MyFunctionName-123` |
| `${EVENT_NUMBER}` | A number between 1 and 6 inclusive. This will select one of the 6 test files available in this repository. | 3 | 

Print the content of `response.json` in a pretty format by running the following
```bash
node -e "console.log(JSON.parse(require('./response').body))"
```

You can create your own test event as follows
```json
{
    "text":"Insert your text here"
}
```
## Cleanup
 
```bash
sam delete
```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
