# Serverless Image Analysis and Auto-Tagging with Amazon Bedrock Nova Lite

![architecture](architecture/architecture.png)

This pattern implements a serverless image analysis and auto-tagging service using Amazon S3, AWS Lambda and Amazon Bedrock's Nova Lite model. When images are uploaded to an S3 bucket, it automatically triggers a Lambda function that analyzes the image content using Amazon Nova Lite and applies descriptive tags as S3 metadata.

The Lambda function processes the uploaded image by sending it to Amazon Bedrock's Nova Lite model for analysis. Nova Lite generates 10 descriptive words based on the image content, and these words are automatically applied as S3 object tags, enabling powerful search and organization capabilities for your image collection.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-lambda-bedrock-nova

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed
* [Amazon Bedrock Nova Lite Foundation Model Access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html#add-model-access)

Note: The Lambda function uses Python 3.13 runtime.

## Deployment Instructions

For this pattern, you need access to Amazon Nova Lite foundation model (Model ID: amazon.nova-lite-v1:0). The default deployment region is us-east-1, but you can customize this using the aws_region variable.

You must request access to the Nova Lite model before you can use it. If you try to use the model before you have requested access to it, you will receive an error message.

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd s3-lambda-bedrock-tf
    ```
1. From the command line, initialize terraform to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, review the planned changes before applying:
    ```
    terraform plan
    ```
    
    Optionally, you can specify a custom AWS region (default is us-east-1):
    ```
    terraform plan -var="aws_region=us-west-2"
    ```

1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```

1. Confirm the deployment by typing `yes` when prompted.

## Configuration Variables

The pattern supports the following Terraform variables:

| Variable | Description | Type | Default |
|----------|-------------|------|---------|
| `aws_region` | AWS region for deployment | string | "us-east-1" |
| `prefix` | Prefix to associate with the resources | string | "s3-lambda-bedrock-tf" |

### Region Support

**Important:** Please check documentation for lastest Bedrock models availability
    Amazon Bedrock -> User Guide -> Model support by AWS Region in Amazon Bedrock
    https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html
    Amazon Nova Lite is currently available in the following regions:

Make sure Nova Lite is available in your chosen region before deployment.

## Testing

1. Upload an image to the S3 bucket using the AWS CLI. Replace `S3_BUCKET_NAME` with the generated `s3_image_bucket` from Terraform (refer to the Terraform Outputs section):

    ```
    aws s3 cp your-image.jpg s3://S3_BUCKET_NAME/images/
    ```

    For example:
    ```
    aws s3 cp sample-photo.jpg s3://s3-lambda-bedrock-tf-image-analysis-bucket-abc12345/images/
    ```

2. Monitor the Lambda function execution in CloudWatch Logs:

    ```
    aws logs tail "/aws/lambda/s3-lambda-bedrock-tf-image-analysis" --follow --format json
    ```

    You should see concise log entries like:
    ```
    SUCCESS: images/sample-photo.jpg | Model: amazon.nova-lite-v1:0 | Nova Response: landscape, mountains, sunset, clouds, nature, scenic, outdoor, beautiful, peaceful, horizon | Tags Applied: 10
    ```

3. Check the applied tags on your uploaded image:

    ```
    aws s3api get-object-tagging --bucket S3_BUCKET_NAME --key images/your-image.jpg
    ```

    Example response:
    ```json
    {
        "TagSet": [
            {
                "Key": "ai-tag-1",
                "Value": "landscape"
            },
            {
                "Key": "ai-tag-2",
                "Value": "mountains"
            },
            {
                "Key": "ai-tag-3",
                "Value": "sunset"
            }
        ]
    }
    ```

4. You can also view the tags in the AWS S3 Console by navigating to your bucket and selecting the uploaded image.

### Supported Image Formats
- JPEG (.jpg, .jpeg)
- PNG (.png)

## Architecture Details

The solution automatically creates:
- S3 bucket with `images/` folder for organized storage
- Lambda function configured with Nova Lite model access
- CloudWatch log group with 14-day retention
- IAM roles and policies with least-privilege access
- S3 event notifications for automatic triggering

## Cleanup

1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/s3-lambda-bedrock-claude-image-analysis
    ```

2. Delete all objects from the S3 bucket first:
    ```
    aws s3 rm s3://YOUR_BUCKET_NAME --recursive
    ```

3. Delete all created resources
    ```
    terraform destroy
    ```
    
    Or with custom region:
    ```
    terraform destroy -var="aws_region=us-west-2"
    ```
    
4. Confirm the destruction by typing `yes` when prompted.

5. Confirm all created resources has been deleted
    ```
    terraform show
    ```

## Troubleshooting

### No CloudWatch Logs Appearing
1. Check if the Lambda function is being triggered:
   ```bash
   aws logs describe-log-groups --log-group-name-prefix "/aws/lambda/s3-lambda-bedrock-tf"
   ```

2. Verify Lambda function permissions:
   ```bash
   aws iam get-role --role-name s3-lambda-bedrock-tf-image-analysis-role-*
   ```

### Nova Lite Access Issues
1. Verify Nova Lite model access in your region:
   ```bash
   aws bedrock list-foundation-models --region YOUR_REGION --query 'modelSummaries[?contains(modelId, `nova-lite`)]'
   ```

2. Check if Nova Lite model is accessible:
   ```bash
   aws bedrock get-foundation-model --model-identifier amazon.nova-lite-v1:0 --region YOUR_REGION
   ```

3. Request model access in AWS Bedrock console if needed:
   - Go to AWS Bedrock Console → Model Access
   - Request access to `amazon.nova-lite-v1:0`
   - Wait for approval (usually immediate)

### Lambda Function Debug Steps

If you see "ValidationException: unsupported input modality" errors:
1. Confirm you're using Nova Lite (not Nova Micro) in the Lambda code
2. Verify model access has been granted in Bedrock console
3. Check that you're deploying in a supported region (us-east-1, us-west-2)

### No Tags Being Added to S3 Objects
1. Check Lambda execution logs for errors:
   ```bash
   aws logs filter-log-events --log-group-name "/aws/lambda/s3-lambda-bedrock-tf-image-analysis" --start-time $(date -d '1 hour ago' +%s)000
   ```

2. Manually test S3 tagging permissions:
   ```bash
   aws s3api put-object-tagging --bucket YOUR_BUCKET --key images/test.jpg --tagging 'TagSet=[{Key=test,Value=manual}]'
   ```

## Log Output Examples

**Successful Processing:**
```
SUCCESS: images/nature-photo.jpg | Model: amazon.nova-lite-v1:0 | Nova Response: forest, trees, green, natural, peaceful, woodland, leaves, branches, sunlight, serene | Tags Applied: 10
```

**Failed Processing:**
```
FAILED: images/corrupted-file.jpg | Model: amazon.nova-lite-v1:0 | Error: An error occurred (ValidationException) when calling the InvokeModel operation
```

**Skipped Files:**
```
SKIPPED: documents/readme.txt - Unsupported file type: txt
```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0