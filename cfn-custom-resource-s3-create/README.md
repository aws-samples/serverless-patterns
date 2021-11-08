# AWS Lambda to Amazon S3 via a CloudFormation Custom Resource

This pattern creates an Amazon S3 object by using an AWS CloudFormation custom resource and an AWS Lambda function.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-s3-cfn.

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
    cd cfn-custom-resource-s3-create
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter an existing Amazon S3 bucket name, or leave blank to create a new S3 bucket.
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern creates an Amazon S3 object by using an AWS CloudFormation custom resource and an AWS Lambda function. Custom resources enable you to write custom provisioning logic in templates that CloudFormation runs anytime you create, update (if you changed the custom resource), or delete stacks.

This pattern deploys a Lambda function that is responsible for creating (and deleting) S3 objects. The function is given CRUD permissions on objects in the S3 bucket. When the stack is first created, CloudFormation sends a create request to the function. When the stack is deleted, CloudFormation sends a delete request to the function. The function ARN is stored as a CloudFormation Export named "function-s3-create". The function requires the following resource properties:

  - Bucket: The name of the S3 bucket where the object will be located.
  - Key: The name of the S3 object (eg: index.html).
  - ContentType: The content type of the S3 object (eg: application/json, text/css, text/html, text/plain).
  - Body: The content of the S3 object.

The template includes a CloudFormation custom resource with a ServiceToken that references the Lambda function ARN. The custom resource provides the function with the required properties to create a new S3 object.

## Testing

Once the application is deployed, navigate to the S3 bucket in the AWS Management Console. Verify that an "index.html" object was created. Navigate to the Amazon CloudWatch Logs console to view the Lambda function logs. The log group name is "/aws/lambda/cfn-custom-resource-s3-create-FunctionS3Create...". Here you will see an event from CloudFormation that instructs the Lambda function to create a new S3 object. There is also a response that the Lambda function sends back to CloudFormation so that the stack deployment process may continue.

Once the function is deployed, the custom resource can also be used in other CloudFormation templates that need to create S3 objects. If the custom resource is used in another CloudFormation template, modify the ServiceToken property to retrieve the function ARN from CloudFormation Exports (eg: ServiceToken: !ImportValue function-s3-create).

Try creating a new CloudFormation stack using one of the example templates below. Be sure to replace {S3BucketName} with the name of the S3 bucket. If you did not provide an existing S3 bucket name when the application was deployed, refer to CloudFormation Outputs for the name of the new bucket that was created (eg: cfn-custom-resource-s3-create-news3bucket...).

Example CloudFormation template that includes a custom resource to create a text document:

```
AWSTemplateFormatVersion: 2010-09-09
Description: Example use of a CloudFormation Custom Resource.
Resources:
  CustomResourceS3Create:
    Type: 'Custom::S3Create'
    Properties:
      ServiceToken: !ImportValue function-s3-create
      Bucket: {S3BucketName} # <<< Update the S3 bucket name
      Key: example.txt
      ContentType: text/plain
      Body: |
        This object was created by using a CloudFormation custom resource.
        It is an example of how to create a text document.
```

Example CloudFormation template that includes a custom resource to create an html document:

```
AWSTemplateFormatVersion: 2010-09-09
Description: Example use of a CloudFormation Custom Resource.
Resources:
  CustomResourceS3Create:
    Type: 'Custom::S3Create'
    Properties:
      ServiceToken: !ImportValue function-s3-create
      Bucket: {S3BucketName} # <<< Update the S3 bucket name
      Key: example.html
      ContentType: text/html
      Body: | 
        <!DOCTYPE html>
        <head>
          <title>Example</title>
        </head>
        <body>
          <p>This object was created by using a CloudFormation custom resource.</p>
        </body>
        </html>
```

After you delete the CloudFormation stack, confirm that the S3 object is also deleted. If a new S3 bucket was created during stack deployment, the bucket is also deleted when you delete the stack. If you specificed an existing S3 bucket during stack deployment, the existing bucket is not deleted, only the object within the bucket will be deleted.

## Documentation
- [CloudFormation Custom Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html)
- [Custom Resource Request Types](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requesttypes.html)
- [Custom Resource Response](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-lambda-function-code-cfnresponsemodule.html)

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
