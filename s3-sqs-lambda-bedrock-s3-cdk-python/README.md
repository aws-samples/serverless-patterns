# GenAI conversation summarization using Amazon S3, Amazon SQS, AWS Lambda, and Amazon Bedrock

This pattern creates an Amazon S3 bucket that sends 'OBJECT_CREATED' events to an Amazon SQS queue. An AWS Lambda function receives the messages from the queue and invokes Amazon Bedrock to extract a summary and sentiment from the file. The result is stored in a different S3 bucket for consumption. This setup is particularly useful for obtaining a summary of conversations between customers and support associates.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)
* [Python, pip, virtualenv](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html) installed

## Prerequisite
Amazon Bedrock users need to request access to models before they are available for use. If you want to add additional models for text, chat, and image generation, you need to request access to models in Amazon Bedrock. For this pattern need access to 'Titan Text G1 - Express' model. Please refer to the link below for instruction:
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
6. Generate the CloudFormation template with the following AWS CDK CLI command:
   ```
   cdk synth
   ```
7. If needed, bootstrap your account:
    ```
    cdk bootstrap
    ```
8. From the command line, use CDK to deploy the AWS resources for the pattern. You'll be prompted to approve security related changes during the deployment.
    ```
    cdk deploy
    ```

## How it works

* Upload a support conversation history input file to the input S3 Bucket, triggering an 'OBJECT_CREATED' event notification to an SQS Queue. A Lambda function receives the message from the queue and fetches the content  using the Bucket and Object key information in the event. The function constructs a prompt containing the support conversation and invokes Amazon Titan Text Express from Bedrock to generate a conversation summary and sentiment in JSON format. Finally, the Lambda function uploads the output to the summary S3 Bucket.


## Testing

1. Navigate to the S3 bucket with a name containing 's3sqslambdabedrocks3cdkpythons-inputbucket**' along with your stack name and a hash key
2. Upload input file containing conversation history to the bucket (sample input files are available under ./lambda folder)
3. Wait for Amazon Bedrock to produce the sentiment and summary of the conversation. The Response will be uploaded to 's3sqslambdabedrocks3cdkpytho-summarybucket' using the same name of the input file uploaded earlier.
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
