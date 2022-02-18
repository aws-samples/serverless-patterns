# AWS Lambda to Amazon Rekognition

This pattern demonstrates how an event can be used to trigger a Lambda function and run Image analysis using Amazon Rekognition.

Learn more about this pattern at the Serverless Land Patterns Collection: https://serverlessland.com/patterns/lambda-rekognition-rust

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Rust](https://www.rust-lang.org/) 1.56.0 or higher
* [cargo-zigbuild](https://github.com/messense/cargo-zigbuild) and [Zig](https://ziglang.org/) for cross-compilation

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository

```
git clone https://github.com/aws-samples/serverless-patterns
```

2. Change directory to the pattern directory:

```
cd lambda-rekognition-rust
```

3. Install dependencies and build (docker and cross build are required):
    ```
    make build
    ```
4. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    make deploy
    ```
5. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.


## How it works

* Upload an object to the deployed S3 bucket.
* The Lambda function is invoked with the event from S3, routed via EventBridge.
* The Lambda function uses Amazon Rekognition


## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to push an image into an S3 bucket.

For testing purposes, we put an event into EventBridge that is similar to S3 put image data event.


1. Run the following S3 CLI command to upload an object to the S3 bucket. Note, you must edit the *SourceBucketName* placeholder with the name of the S3 Bucket. This is provided in the stack outputs

```bash
aws s3 cp './image/helloworld1.png' s3://*SourceBucketName*
```

2. Run the following command to check to get the logs from the deployed Lambda function (use the function name from the stack output):

```bash
sam logs -n *FunctionName* --region *YourRegion*
```

below are snippets from the logs

```
S3Event { bucket: S3Bucket { name: "sam-app-sourcebucket-1111rqp5jlkhz" }, object: S3Object { key: "helloworld1.png", size: 23917 }, reason: "PutObject" }
TextDetection { detected_text: Some("Hello World!"), r#type: Some(Line), id: Some(0), parent_id: None, confidence: Some(99.79834), geometry: Some(Geometry { bounding_box: Some(BoundingBox { width: Some(0.80097616), height: Some(0.095372885), left: Some(0.10155721), top: Some(0.32728526) }), polygon: Some([Point { x: Some(0.10155721), y: Some(0.33077845) }, Point { x: Some(0.90213245), y: Some(0.32728526) }, Point { x: Some(0.90253335), y: Some(0.41916496) }, Point { x: Some(0.10195811), y: Some(0.42265815) }]) }) }
TextDetection { detected_text: Some("02-Dec-2021"), r#type: Some(Line), id: Some(1), parent_id: None, confidence: Some(99.13514), geometry: Some(Geometry { bounding_box: Some(BoundingBox { width: Some(0.2874618), height: Some(0.035), left: Some(0.09378187), top: Some(0.5475) }), polygon: Some([Point { x: Some(0.09378187), y: Some(0.5475) }, Point { x: Some(0.38124365), y: Some(0.5475) }, Point { x: Some(0.38124365), y: Some(0.5825) }, Point { x: Some(0.09378187), y: Some(0.5825) }]) }) }
TextDetection { detected_text: Some("© 2021, Amazon Web Services, Inc. or its Affiliates."), r#type: Some(Line), id: Some(2), parent_id: None, confidence: Some(92.56063), geometry: Some(Geometry { bounding_box: Some(BoundingBox { width: Some(0.54638124), height: Some(0.019999923), left: Some(0.076452605), top: Some(0.9516667) }), polygon: Some([Point { x: Some(0.076452605), y: Some(0.9516667) }, Point { x: Some(0.62283385), y: Some(0.9516667) }, Point { x: Some(0.62283385), y: Some(0.97166663) }, Point { x: Some(0.076452605), y: Some(0.97166663) }]) }) }
```

## Cleanup

1. Delete the stack

    ```bash
    make delete
    ```

1. Confirm the stack has been deleted

    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
