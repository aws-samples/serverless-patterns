# Amazon S3 with S3 Object Lambda (return image thumbnails from S3)

This pattern creates an S3 bucket, an S3 Access Point, an S3 Object Lambda Access Point, and Lambda function.

This application uses S3 Object Lambda to return a thumbnail version of an image in S3.

## Getting started with Terraform Serverless Patterns

Read more about general requirements and deployment instructions for Terraform Serverless Patterns [here](https://github.com/aws-samples/serverless-patterns/blob/main/terraform-fixtures/docs/README.md).

## How it works

When a request is made to the S3 Object Lambda Access Point, the Lambda function is invoked. Within the Lambda function code, the `getObjectContext` property contains the following useful information:

1. inputS3Url: a [presigned URL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html) that the function can use to download the original object from the supporting Access Point. In this way, the Lambda function does not need to have S3 read permissions to retrieve the original object and can only access the object processed by each invocation.
1. outputRoute, outputToken: used to send back the modified object using the [WriteGetObjectResponse](https://docs.aws.amazon.com/AmazonS3/latest/API/API_WriteGetObjectResponse.html) API.

The function uses the provided presigned URL to retrieve the requested image from S3 using [axios](https://www.npmjs.com/package/axios). The function resizes the image using [sharp](https://www.npmjs.com/package/sharp). Then the function returns a thumbnail version of the image back to S3 Object Lambda.

## Testing

After deployment, upload sample image to the S3 bucket using this command (replace `<bucket-name>` with the value returned in `s3_bucket_id`):

```shell
aws s3 cp ./images/sample.jpg s3://<bucket-name>
```

Download a thumbnail version of the uploaded image from the S3 Object Lambda Access Point using this command (replace `<lambda-access-point>` with the value returned in `s3_lambda_access_point`):

```shell
aws s3api get-object --bucket <lambda-access-point> --key sample.jpg ./thumbs/sample-thumbnail.jpg

open ./thumbs/sample-thumbnail.jpg
```

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | >= 4.9 |
| <a name="requirement_random"></a> [random](#requirement\_random) | >= 2.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | >= 4.9 |
| <a name="provider_random"></a> [random](#provider\_random) | >= 2.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_lambda_function"></a> [lambda\_function](#module\_lambda\_function) | terraform-aws-modules/lambda/aws | ~> 4.0 |
| <a name="module_s3_bucket"></a> [s3\_bucket](#module\_s3\_bucket) | terraform-aws-modules/s3-bucket/aws | ~> 3.0 |

## Resources

| Name | Type |
|------|------|
| [aws_s3_access_point.this](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_access_point) | resource |
| [aws_s3control_object_lambda_access_point.this](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3control_object_lambda_access_point) | resource |
| [aws_s3control_object_lambda_access_point_policy.this](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3control_object_lambda_access_point_policy) | resource |
| [random_pet.this](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/pet) | resource |
| [aws_caller_identity.this](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/caller_identity) | data source |
| [aws_iam_policy_document.bucket_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.object_lambda_access_point_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |

## Inputs

No inputs.

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_lambda_function_arn"></a> [lambda\_function\_arn](#output\_lambda\_function\_arn) | The ARN of the Lambda Function |
| <a name="output_lambda_function_invoke_arn"></a> [lambda\_function\_invoke\_arn](#output\_lambda\_function\_invoke\_arn) | The Invoke ARN of the Lambda Function |
| <a name="output_lambda_function_name"></a> [lambda\_function\_name](#output\_lambda\_function\_name) | The name of the Lambda Function |
| <a name="output_lambda_function_qualified_arn"></a> [lambda\_function\_qualified\_arn](#output\_lambda\_function\_qualified\_arn) | The ARN identifying your Lambda Function Version |
| <a name="output_lambda_function_version"></a> [lambda\_function\_version](#output\_lambda\_function\_version) | Latest published version of Lambda Function |
| <a name="output_lambda_role_arn"></a> [lambda\_role\_arn](#output\_lambda\_role\_arn) | The ARN of the IAM role created for the Lambda Function |
| <a name="output_s3_bucket_arn"></a> [s3\_bucket\_arn](#output\_s3\_bucket\_arn) | The ARN of the bucket. Will be of format arn:aws:s3:::bucketname. |
| <a name="output_s3_bucket_id"></a> [s3\_bucket\_id](#output\_s3\_bucket\_id) | The name of the bucket. |
| <a name="output_s3_lambda_access_point"></a> [s3\_lambda\_access\_point](#output\_s3\_lambda\_access\_point) | The ARN of the S3 Object Lambda access point. |
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
