# Access your Lambda Function URLs securely using Amazon CloudFront Origin Access Control

This pattern demonstrates how to enhance security and integrate features between Amazon CloudFront and AWS Lambda by utilizing Origin Access Control (OAC) for Lambda function URLs. This approach secures Lambda functions by restricting access exclusively to designated CloudFront distributions, using AWS Signature Version 4 (SigV4) for authentication.

**Important Note:** 
This application leverages multiple AWS services, and there are associated costs beyond the Free Tier usage. Please refer to the [AWS Pricing page](https://aws.amazon.com/pricing/) for specific details. You are accountable for any incurred AWS costs. This example solution does not imply any warranty.

## Requirements
[Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.  
[AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured  
[Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  
[AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions
Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:  
    
    git clone https://github.com/aws-samples/serverless-patterns/cloudfront-lambdafunctionurl-oac-sam

Change directory to the solution directory:  
    
    cd cloudfront-lambdafunctionurl-oac-sam

From the command line, use AWS SAM to build and deploy the AWS resources as specified in the template.yml file.  

**Build**
```sam build
```
Once build is sucessfull deploy the stack using the deploy command as seen below.

**Deploy**
```sam deploy --guided
```
**During the prompts:**  

**Stack Name:** {Enter your preferred stack name}  
**AWS Region:** {Enter your preferred region}  
**Confirm changes before deploy:** Y  
**Allow SAM CLI IAM role creation:** Y  
**Disable rollback:** N  
**Save arguments to configuration file:** Y  
**SAM configuration file:** {Press enter to use default name}  
**SAM configuration environment:** {Press enter to use default name}  


1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The SAM template sets up a CloudFront Distribution with a Lambda function URL as the origin. An Origin Access Control (OAC) specific to Lambda is created and linked to the CloudFront Distribution, ensuring that only CloudFront can access the Lambda function URL. The template also configures appropriate invoke permissions for the Lambda function. The Origin and Cache Behavior settings in the CloudFront Distribution are optimized for best practices when using a Lambda function URL as the origin.

## Testing

**Access the Lambda Function URL directly**
- Copy the Lambda Function URL value from the SAM deployment process output key 'LambdaFunctionUrl'
- Try accessing the function URL using a web browser
- You should see a page with "Message": "Forbidden" message
**Acccess the Lambda Function URL using CloudFront Distribution domain name**
- Copy the LamCloudFront Distribution Domain Name value from the SAM deployment process output key 'CloudFrontDomainName'
- Try accessing the function URL using the CloudFront domain name.
- You should see a page with success message starting with "Hello from AWS !!! ..."


## Cleanup
 
1. Delete the stack
    ```sam delete
    ```
1. Confirm the stack has been deleted
    ``'aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
