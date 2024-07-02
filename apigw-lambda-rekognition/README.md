# Content safety with Image Moderation using AWS API Gateway and AWS Lambda

Using this sample pattern, users can access AWS API Gateway to generate a pre-signed URL through an AWS Lambda function, using which they can upload images to an Amazon S3 bucket. This URL allows secure and temporary access for uploading files directly to S3.

Once an image is uploaded, an S3 event triggers another Lambda function that uses the DetectModerationLabels API to analyze the content. If the image is identified as inappropriate, a notification is sent via Amazon SNS, ensuring automated content moderation and alerting.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-lambda-rekognition

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.cxom/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-lambda-rekognition
    ```
1. From the command line, initialize terraform to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts
    #var.prefix
    - Enter a value: {enter any prefix to associate with resources}

    #var.region
    - Enter a value: {enter the region for deployment}

## Testing

1. After deploying the stack, create a Subscriber for your Amazon SNS topic (For ex, your email) and confirm the subscription.
    https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html

1. Make a POST request to the API using the following cURL command:

    curl --location 'https://<api-id>.execute-api.<region>.amazonaws.com/dev/generate-presigned-url' --header 'Content-Type: text/plain' --data '{"object_name": "image.png", "content_type": "image/png"}'

    Note: Replace 'api-id' with the generated API ID from Terraform, 'region' with the region where the API is deployed, 'object_name' with your desired name for the S3 object and 'content_type' with the content type of the image, for ex, png or jpeg

1. Get the pre-signed URL from the previous step and use the following cURL command to upload the object in S3:

    curl --location --request PUT '<presigned-url>' --header 'Content-Type: image/png' --data '<path-of-the-object>.png'

    Note: Replace 'presigned-url' with pre-signed URL generated in the previous step. 'Content-Type' should match the content type used to generate the pre-signed URL in the previous step. Make sure you are passing the correct path of the object in the --data parameter.

1. Once the object is uploaded successfully, the Lambda function will be invoked and if the image is inappropirate, a message is sent to the SNS Topic, which is then received by the subscriber.

## Cleanup
 
1. Delete the SNS Subscription:
    Go to SNS > Subsciptions > Select your Subscription and click on Delete

    https://docs.aws.amazon.com/sns/latest/dg/sns-delete-subscription-topic.html

1. Delete all the objects from S3:
    Go to S3 > Select all the objects > Click on Delete

    https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-objects.html
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-multiple-objects.html

1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-lambda-rekognition
    ```

1. Delete all created resources
    ```
    terraform destroy
    ```
    
1. During the prompts:
    ```
    Enter all details as entered during creation.
    ```

1. Confirm all created resources has been deleted
    ```
    terraform show
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0