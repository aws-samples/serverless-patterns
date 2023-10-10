# AWS Step Functions Express Workflow to Amazon Comprehend for Sentiment Analysis  

The Step Functions Express Workflow can be started using the AWS CLI or from another service (e.g. API Gateway) to run an express workflow and return the result.

The SAM template deploys a Step Functions Express workflow that invokes Amazon Comprehend and returns the sentiment analysis done by Comprehend in the response. The SAM template contains the required resouces with IAM permission to run the application with logging enabled.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-comprehend-sam

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
2. Change directory to the pattern directory:
    ```
    cd sfn-comprehend-sam
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

* Start the Express Workflow using the `start-sync-execution` api command with a "message" string in English for sentiment analysis in the input payload.
* The Express Workflow invokes Amazon Comprehend.
* Comprehend returns the sentiment of the input text. 
* If the integration works fine, the sentiment analysis outcome is returned in Step Function execution results within a `output` object
* If the integration fails, the Step Functions workflow will retry up to 5 times before exiting with a `status:FAILED` response.

Please refer to the architecture diagram below:

![End to End Architecture](image/architecture.png)


## Testing

Run the following AWS CLI command to send a 'start-sync-execution` comand to start the Step Functions workflow. Note, you must edit the {StateMachineExpressSyncToComprehend} placeholder with the ARN of the deployed Step Functions workflow. This is provided in the stack outputs.

```bash
aws stepfunctions start-sync-execution  --name "test" --state-machine-arn "{StateMachineExpressSyncToComprehend}" --input "{\"message\":\"I am very happy today.\"}"
```

### Example output:

```bash
{
    "executionArn": "arn:aws:states:us-east-1:796495736600:express:StateMachineExpressSyncToComprehend-cqmUxRLjlvq7:test:8b75495d-cb96-4933-ac25-1f908050e33d",
    "stateMachineArn": "arn:aws:states:us-east-1:796495736600:stateMachine:StateMachineExpressSyncToComprehend-cqmUxRLjlvq7",
    "name": "test",
    "startDate": "2023-10-08T07:35:55.257000+05:30",
    "stopDate": "2023-10-08T07:35:55.358000+05:30",
    "status": "SUCCEEDED",
    "input": "{\"message\":\"I am very happy today.\"}",
    "inputDetails": {
        "included": true
    },
    "output": "{\"message\":\"I am very happy today.\",\"Sentiment\":{\"Sentiment\":\"POSITIVE\",\"SentimentScore\":{\"Mixed\":1.4907288E-4,\"Negative\":1.3237515E-4,\"Neutral\":3.8026855E-4,\"Positive\":0.9993383}}}",
    "outputDetails": {
        "included": true
    },
    "billingDetails": {
        "billedMemoryUsedInMB": 64,
        "billedDurationInMilliseconds": 200
    }
}
```
## Cleanup
 
Delete the stack
    ```bash
    sam delete
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
