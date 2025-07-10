# Integration of Amazon API Gateway REST API with Amazon Lambda and Amazon SNS

The SAM template deploys a API Gateway REST API with Lambda function integration, an SNS topic and the IAM permissions required to run the application. Whenever the REST API is invoked, the Lambda function publishes a message to the SNS topic. The AWS SAM template deploys the resources and the IAM permissions required to run the application.

## Features

- **API Gateway REST API** with Lambda integration
- **Lambda function** that publishes messages to SNS
- **SNS topic** for message publishing
- **CloudWatch Alarm** monitoring API errors
- **Amazon CloudWatch Synthetics Canary** for automated API endpoint monitoring
- **AWS X-Ray tracing** enabled for distributed tracing on LAmbda and APIGW (incurs additional costs)
- **S3 bucket** for Synthetics artifacts storage

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-lambda-sns/.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. **Note: AWS X-Ray tracing is enabled which incurs additional charges based on traces recorded and retrieved.** You are responsible for any AWS costs incurred. No warranty is implied in this example.

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
    cd apigw-lambda-sns
    ``` 
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ``` 
    sam deploy --guided
    ``` 
4. During the prompts:
    
         * Enter a stack name
         * Enter the desired AWS Region
         * Allow SAM CLI to create IAM roles with the required permissions.
    
    Once you have run sam deploy -guided mode once and saved arguments to a configuration file (samconfig.toml), you can use sam deploy in future to use these defaults.
    
5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.
    

## Testing

The stack will output the *api endpoint*. You can use Postman or curl to send a GET request to the API Gateway endpoint.

```
curl --location --request GET 'https://<api_id>.execute-api.<region>.amazonaws.com/s1'
```
In order to receive a notification, please make sure to configure subscription in the SNS topic.

### Additional Features

- **CloudWatch Alarm**: Monitor the Synthetics Canary failures. The alarm triggers when the canary fails at least once within a 5-minute period.
- **Synthetics Canary**: Automatically tests the API endpoint every minute to ensure availability. If you want to alarm on this, you must manually create a CloudWatch Alarm or update the template
- **X-Ray Tracing**: Distributed tracing is enabled for both API Gateway and Lambda to help with debugging and performance analysis.


## Cleanup

1. Delete the stack 
    ```
    aws cloudformation delete-stack —stack-name STACK_NAME
    ```
2. **Manually delete the S3 bucket** - The Synthetics artifacts bucket must be manually emptied and deleted after stack deletion
3. Confirm the stack has been deleted 
    ```
    aws cloudformation list-stacks —query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

**Important**: You must manually delete the S3 bucket created for Synthetics artifacts after deleting the CloudFormation stack, as it will contain canary run artifacts.

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
