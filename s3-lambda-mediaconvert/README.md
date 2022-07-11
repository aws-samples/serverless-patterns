# Amazon S3 to AWS Elemental MediaCovert via AWS Lambda

This pattern automates the creation of transcoding jobs in [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/) once a new video file lands on S3.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/s3-lambda-mediaconvert).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Python 3.9](https://wiki.python.org/moin/BeginnersGuide/Download)  or higher installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd s3-lambda-mediaconvert
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.


## How it works

This pattern deploys two S3 buckets, one AWS Lambda function and the required IAM Roles for making AWS Lambda capable of creating AWS Elemental MediaConvert jobs and write logs in Amazon CloudWatch Logs. AWS Lambda function is written in Python 3.9. Each time you upload a video file to the input S3 bucket, a Lambda function is triggered. The function gets invocation event, process it, and creates a job in AWS Elemental MediaConverter. The settings of the job are in the `job.json` file which is part of the lambda deployment package. The output of the job is a transcoded video which is saved in the output S3 bucket.  

## Testing
Once the application is deployed, navigate to Amazon S3 bucket and locate the `videoinput` bucket. Upload a video to root of the bucket. Then go to AWS CloudWatch Logs and locate the logs of the Lambda function. If the S3 event and the call top AWS Elemental MediaConverter worked, you should see the output of the Lambda function.

Example of AWS Elemental MediaConvert Response to the call made by Lambda:
```
{
    "ResponseMetadata": {
        "RequestId": "9585a60c-707e-4a95-b0a0-71645d78b6e0",
        "HTTPStatusCode": 201,
        "HTTPHeaders": {
            "date": "Sat, 02 Jul 2022 22:55:50 GMT",
            "content-type": "application/json",
            "content-length": "3661",
            "connection": "keep-alive",
            "x-amzn-requestid": "9585a60c-707e-4a95-b0a0-71645d78b6e0",
            "x-amz-apigw-id": "UqT2cFnXIAMFRmw=",
            "x-amzn-trace-id": "Root=1-62c0ccf5-4ab5f9f3718ddea30c739ae0"
        },
        "RetryAttempts": 0
    },
    "Job": {
        ...
        "Status": "SUBMITTED",
        "StatusUpdateInterval": "SECONDS_60",
        "Timing": {
            "SubmitTime": "2022-07-02 22:55:50+00:00"
        },
        "UserMetadata": {
            "assetID": "e880c291-f7a4-4f3b-878e-c252db375c96"
        }
    }
}
```
Additionally, you can go AWS Elemental MediaCovert to see the jop in either SUBMITTED or COMPLETE status. Make sure your are in  the correct region.
Finally, go to the `videooutput` bucket, navigate through the folder structure, and you will find the transcoded video in HLS format.

## Documentation
- [AWS Elemental MediaConvert IAM Service Role](https://docs.aws.amazon.com/mediaconvert/latest/ug/creating-the-iam-role-in-iam.html)
- [Resolving circular dependencies with AWS SAM templates](https://aws.amazon.com/es/premiumsupport/knowledge-center/cloudformation-circular-dependency-sam/)
- [Setting up a job in AWS Elemental MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-a-job.html)
- [Best practices for working with AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [Boto3 MediaCovert library](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html)


## Cleanup
1. Empty `videoinput` and `videooutput` through the AWS Console
2. Delete SAM App
   ```bash
   sam delete
   ```
3. Go to AWS CloudWatch Logs and remove the Log Group created by Lambda.

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

