# Amazon API Gateway to AWS Lambda to Amazon Transcribe using AWS SAM

This pattern facilitates audio transcription by using Amazon Transcribe service through a serverless API endpoint. When audio files are uploaded to S3, they can be transcribed using Amazon Transcribe via an API Gateway endpoint backed by Lambda.

This pattern enables speech-to-text transcription use cases by providing a serverless API endpoint that can process audio files stored in S3. The pattern uses AWS Lambda to coordinate with Amazon Transcribe service, making it easy to integrate transcription capabilities into your applications.

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
    cd apigw-lambda-transcribe-sam-js
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

2. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The pattern creates an API Gateway endpoint that accepts POST requests with JSON payloads containing an S3 URL of an audio file. When a request is received:

1. API Gateway forwards the request to AWS Lambda
2. Lambda function starts a transcription job using Amazon Transcribe
3. Amazon Transcribe processes the audio file and generates the transcription
4. The transcription results are stored in the specified S3 bucket

## Testing

To test the deployed API endpoint:

1. Upload an audio file to the created S3 bucket:
```
aws s3 cp audio.mp3 s3://your-bucket-name/
```
2. Get the S3 URL of the uploaded audio file
3. Make a POST request to the API Gateway endpoint with the following JSON payload:

```bash
curl -X POST https://your-api-endpoint/Prod/transcribe \
  -H "Content-Type: application/json" \
  -d '{"audio_url": "s3://your-bucket-name/audio.mp3"}'
```
4. The API will return a response with the transcription job name and status
```json
{
    "job_name": "transcribe-12345678-1234-5678-1234-567812345678",
    "status": "IN_PROGRESS"
}
```
5. You can check the transcription results in the S3 bucket once the job is complete:

```bash
aws transcribe get-transcription-job --transcription-job-name "job-name-from-response"
```
## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0