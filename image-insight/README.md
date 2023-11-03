# ImageInsight

![Workflow](/ImageInsightsWorkflow.png)

## Overview
This project is a serverless application that uses AWS services to provide image description based on AWS Rekognition and Bedrock services. It's designed to help you analyze and describe the content of images.

## Features
- Automatic image description using AWS Rekognition.
- Serverless architecture for cost-efficiency and scalability.
- API Gateway for easy integration with other services.

## Prerequisites
Before you begin, ensure you have the following prerequisites:
- An AWS account.
- AWS CLI configured with necessary access permissions.
- AWS Serverless Application Model (AWS SAM) installed.
- Python installed for local development.

## Getting Started
1. Clone this repository.
```bash
git clone https://github.com/your-username/image-vision-project.git
cd image-vision-project
```
2. Deploy the serverless application using AWS SAM.
```bash
sam build
sam deploy --guided --stack-name image-description-stack --capabilities CAPABILITY_NAMED_IAM
```
3. Your application is now deployed, and the API Gateway endpoint is available.

## Usage
You can use the provided API endpoint to get image descriptions. Send a PUT request to the endpoint with an image file as input. Replace `<api-gateway-url>` with the actual URL.
Example using `curl`:
```bash
curl -X PUT -H "Content-Type: image/jpeg" --data-binary @your-image.jpg <api-gateway-url/bucket-name/object-name>
```

Upon making the GET request to the same <api-gateway-url> you will be able to fetch the results.
```bash
curl -X GET <api-gateway-url/bucket-name/object-name>
```

## Additional Configuration
- Modify the Lambda function code to handle image description based on your specific use case.
- Modify the code to use a custom bedrock model according to your requirements.

## Copyright
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

## Acknowledgments
- This project was made possible by the AWS Serverless ecosystem and community contributions.

Happy image describing!
```