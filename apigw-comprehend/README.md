# Amazon API Gateway REST API to Amazon Comprehend

In this use case, we have API Gateway REST API as a proxy to Amazon Comprehend's [DetectSentiment](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectSentiment.html) API operation.
Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-comprehend.

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
    cd serverless-patterns/apigw-comprehend
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

To test the endpoint first send data using the following command. Be sure to update the API Endpoint from the Cloudformation Stack Output.

```
curl --location --request POST '[YOUR API ENDPOINT]' --header 'Content-Type: application/json' \
--data-raw '{
        "LanguageCode": "String",
        "Text": "String"
    }'
```
You will observe a complete sentiment analysis of the 'Text' inputs that are passed as payload to your API endpoint as follows:

1. Test payload 1 -
```{
   "LanguageCode": "en",
   "Text": "Comprehend is great to use."
    }
```
 Output:
```
{
    "Sentiment": "POSITIVE",
    "SentimentScore": {
        "Mixed": 3.2229068892775103E-5,
        "Negative": 2.691979352675844E-5,
        "Neutral": 1.229004265042022E-4,
        "Positive": 0.9998179078102112
    }
}
```
1. Test payload 2 -
```{
   "LanguageCode": "en",
   "Text": "It is not good to skip using Comprehend."
    }
```
 Output:
```
{
    "Sentiment": "NEGATIVE",
    "SentimentScore": {
        "Mixed": 0.03624984249472618,
        "Negative": 0.9486008286476135,
        "Neutral": 0.004839026369154453,
        "Positive": 0.010310239158570766
    }
}
```
1. Test payload 3 -
```{
   "LanguageCode": "en",
   "Text": "It's normal to use Comprehend."
    }
```
 Output:
```
{
    "Sentiment": "NEUTRAL",
    "SentimentScore": {
        "Mixed": 0.002466087695211172,
        "Negative": 0.0034168041311204433,
        "Neutral": 0.8172720074653625,
        "Positive": 0.17684519290924072
    }
}
```

You can also run the following commands on a terminal prompt to get the API Endpoint -

**API Endpoint**
```
aws cloudformation describe-stacks --stack-name [YOUR STACK NAME] --query "Stacks[0].Outputs[?OutputKey=='ComprehendApiEndpoint'].OutputValue" --output text
```

## Cleanup
 
1. Delete the stack
    ```
    sam delete
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0