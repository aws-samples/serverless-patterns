# Resizing images uploaded to Amazon S3 with AWS Lambda

The AWS SAM template deploys:
 - A Java-based Lambda function:
   - Powered by [Amazon Q Developer](https://aws.amazon.com/q/developer/)
   - [**NEW**] [Lambda SnapStart enabled for ARM64](https://aws.amazon.com/about-aws/whats-new/2024/07/aws-lambda-snapstart-java-functions-arm64-architecture/) based architecture
 - A source S3 bucket 
 - A destination S3 bucket
 - The IAM resources required to run the application. 

The Lambda function consumes `ObjectCreated` events from an Amazon S3 bucket. 
The Lambda code checks the uploaded file is an image and creates a lower resolution version of the image in the destination bucket.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/s3-lambda](https://serverlessland.com/patterns/s3-lambda)

Important: this application uses various AWS services, and there are costs associated with these services after the Free Tier usage.
Please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. 
You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements
* [Java 21](https://docs.aws.amazon.com/corretto/latest/corretto-21-ug/downloads-list.html)
* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have enough permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

-  Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ``` 
   git clone https://github.com/aws-samples/serverless-patterns
   ```
- Change directory to the pattern directory:
    ```
    cd s3-lambda-resizing-java
    ```
- From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the `template.yml` file:
    ```
    sam build && sam deploy --guided
    ```
- During the prompts:
  * Enter a stack name
  * Enter the desired AWS Region
  * Enter names for your source and destination S3 buckets. Make sure these are unique as S3 bucket names share a global namespace.
  * Allow SAM CLI to create IAM roles with the required permissions.

Once you have run above once and saved arguments to a configuration file (`samconfig.toml`), 
you can use `sam deploy` in future to use these defaults.

Note the outputs from the AWS SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

* Use the AWS CLI to upload an image to S3
* If the object is a .jpeg file, the code creates a 800x600 resolution image and saves it to the destination bucket.

## Testing

Run the following S3 CLI command to upload an image to the S3 bucket.
Note, you must edit the {SourceBucketName} and {DestinationBucketName} placeholders with the name of the S3 Bucket which are provided in the stack outputs.

```bash
aws s3 cp './data/white_dog.jpeg'  s3://{SourceBucketName}
```

Run the following command to check that a new version of the image has been created in the destination bucket.

```bash
aws s3 ls s3://{DestinationBucketName}
```

## Running JUnit 5 test
To run the JUnit test `AppTest.java`, you need to make few changes:

- Modify the [events/s3_event.json](./ResizerFunction/src/test/resources) file to reflect the source bucket name. Replace the value in the placeholder.
- Replace the destination bucket name placeholder in the surefire plugin's environment variable placeholder in the `pom.xml` file.
- Enable the test [`AppTest.java`](./ResizerFunction/src/test/java/resizer/AppTest.java) by removing the `@Disabled` annotation.
- Change directory to `./ResizerFunction`.
- Run `mvn clean test`

You should see the test passing. 
The test uses [aws-lambda-java-tests](https://github.com/aws/aws-lambda-java-libs/tree/main/aws-lambda-java-tests) library.

## Cleanup

- Delete the objects created in the source and the destination bucket.
- Delete the stack
    ```bash
    sam delete --stack-name STACK_NAME
    ```
- Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----

Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
