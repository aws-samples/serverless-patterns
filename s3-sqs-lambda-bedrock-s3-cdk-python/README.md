# Conversation Summarization: Leveraging Amazon S3, SQS, Lambda, and Bedrock\

This pattern creates an Amazon S3 bucket that sends 'OBJECT_CREATED' events to an SQS queue. These events are then processed by a Lambda function that utilizes Amazon Bedrock to extract the summary and sentiment of the input file. The summary is subsequently stored in a different S3 bucket for consumption. This setup is particularly useful for obtaining a summary of conversations between customers and support associates.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)
* [Python, pip, virtualenv](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html) installed

## Prerequisite
Amazon Bedrock users need to request access to models before they are available for use. If you want to add additional models for text, chat, and image generation, you need to request access to models in Amazon Bedrock. Please refer to the link below for instruction:
[Model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd s3-sqs-lambda-bedrock-s3-cdk-python
    ```
3. Create a virtual environment for Python:
   ```
   python3 -m venv .venv
   ```
4. Activate the virtual environment
   ```
   source .venv/bin/activate
   ```
   For a Windows platform, activate the virtualenv like this:
   ```
   .venv\Scripts\activate.bat
5. Install the Python required dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Review the CloudFormation template the cdk generates for you stack using the following AWS CDK CLI command:
   ```
   cdk synth
   ```
7. Run the command below to bootstrap your account CDK needs it to deploy
    ```
    cdk bootstrap
    ```
8. From the command line, use CDK to deploy the AWS resources for the pattern. You'll be prompted to approve security related changes during the deployment.
    ```
    cdk deploy
    ```

## How it works

* Upload a support conversation history input file to the input S3 Bucket, triggering an 'OBJECT_CREATED' event notification to an SQS Queue. Upon receipt, the SQS Queue triggers a Lambda function which will fetch the content of the file using Bucket and Object key info in the event. The Lambda constructs a prompt containing the support conversation and invokes Amazon Titan Text Express from Bedrock to generate conversation summary and sentiment in JSON format. Finally, the Lambda uploads this summary to the summary S3 Bucket.


## Testing

1. Navigate to the S3 bucket containing key 's3sqslambdabedrocks3cdkpythons-inputbucket**' along with your stack name and a hash key
2. Upload input file containing conversation history to the bucket (sample input files are available under ./lambda folder)
3. Wait for the AWS Lambda function to invoke the Amazon Bedrock model to get the sentiment and summary of the conversation. The Response will be uploaded to 's3sqslambdabedrocks3cdkpytho-summarybucket' using the same name of the input file uploaded earlier.
4. The response will look like the sample shown below:
```
{
    "sentiment" : "Positive",
    "issues" : [
        {
            "topic" : "Room booking",
            "summary" : "Customer wants to book a room for two adults and one child for three nights starting from the 15th of May with a sea view and family-friendly amenities. Agent checks availability and offers a Deluxe Suite with a sea view and amenities suitable for families. Total cost is $750, but there are no discounts or promotions available. Agent offers a complimentary breakfast for each day of the stay as a gesture of appreciation. Customer agrees to book the Deluxe Suite and receives a confirmation email with all the details."
        }
    ]
}
```


### Making changes

You can customize the AWS Lambda Functions by editing the code at `./lambda/index.py`. To deploy changes, use the `cdk deploy` command.

## Cleanup
 
1. Delete the stack
    ```
    cdk destroy
    ```

2. Confirm the stack has been deleted. Login to the AWS console and navigate to the AWS Cloudformation service page "CdkServerlessInfraStack" is deleted or run the below 
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'S3SqsLambdaBedrockS3CdkPythonStack')].StackStatus"
    ```

You should expect to see a message confirming `DELETE_COMPLETE`.

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0