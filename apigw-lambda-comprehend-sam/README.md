# Amazon API Gateway to AWS Lambda to Amazon Comprehend

This sample project deploys an Amazon API Gateway REST API with an AWS Lambda integration. The Lambda function is written in Python, calls the Amazon Comprehend DetectSentiment API, and returns a response containing the detected sentiment.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-lambda-comprehend-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```bash
   cd apigw-lambda-comprehend-sam
   ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```bash
   sam deploy --guided
   ```
1. During the prompts:

   - Enter a stack name
   - Enter the desired AWS Region
   - Allow SAM CLI to create IAM roles with the required permissions.

   Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

   When asked "`DetectSentimentLambdaFunction` has no authentication. Is this okay? [y/N]", answer explicitly with y for the purposes of this sample application. As a result, anyone will be able to call this example REST API without any form of authentication.

   For production applications, you should [enable authentication for the API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html) using one of several available options and [follow the API Gateway security best practices](https://docs.aws.amazon.com/apigateway/latest/developerguide/security-best-practices.html).

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This sample project uses Amazon Comprehend's DetectSentiment API by exposing it through a serverless REST API.

Here's a breakdown of the steps:

1. **Amazon API Gateway**: Receives the HTTP POST request containing text for sentiment analysis.

1. **AWS Lambda**: Triggered by the API Gateway, this function forwards the text to Amazon Comprehend's DetectSentiment API.

1. **Amazon Comprehend**: Analyzes the text, determining sentiments like "POSITIVE", "NEGATIVE", etc., and returns this analysis to Lambda.

1. **Response**: Lambda processes the Comprehend output and sends it back to the user via the API Gateway.

## Testing

Test the deployed sentiment analysis API by providing an input with a positive sentiment. You can use [curl](https://curl.se/) to send a HTTP POST request to the API. Make sure to replace the API endpoint URL with the one from your AWS SAM outputs:

```bash
curl -d '{"input": "I love strawberry cake!"}' -H 'Content-Type: application/json' https://<API Gateway endpoint>.execute-api.<AWS Region>.amazonaws.com/Prod/detect_sentiment/
```

The API returns a response that contains the detected sentiment and a confidence score for all available sentiments:

```json
{
  "sentiment": "POSITIVE",
  "confidence_scores": {
    "Positive": 0.9991476535797119,
    "Negative": 9.689308353699744e-5,
    "Neutral": 0.0006526037468574941,
    "Mixed": 0.00010290928184986115
  }
}
```

Try testing the API with an input containing a negative sentiment and compare the results:

```bash
curl -d '{"input": "I hate chocolate cake!"}' -H 'Content-Type: application/json' https://<API Gateway endpoint>.execute-api.<AWS Region>.amazonaws.com/dev/detect_sentiment/
```

## Cleanup

To delete the resources deployed to your AWS account via AWS SAM, run the following command:

```bash
sam delete
```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
