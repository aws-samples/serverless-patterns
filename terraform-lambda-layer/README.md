# Complete AWS Lambda examples

Configuration in this directory creates AWS Lambda Function, Layers, Alias, and so on with the large variety of supported features showing this module in action.


## Usage

To run this example you need to execute:

```bash
$ terraform init
$ terraform plan
$ terraform apply
```

Note that this example may create resources which cost money. Run `terraform destroy` when you don't need these resources.

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 0.13.1 |
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
| <a name="module_disabled_lambda"></a> [disabled\_lambda](#module\_disabled\_lambda) | ../../ | n/a |
| <a name="module_lambda_at_edge"></a> [lambda\_at\_edge](#module\_lambda\_at\_edge) | ../../ | n/a |
| <a name="module_lambda_function"></a> [lambda\_function](#module\_lambda\_function) | ../../ | n/a |
| <a name="module_lambda_function_existing_package_local"></a> [lambda\_function\_existing\_package\_local](#module\_lambda\_function\_existing\_package\_local) | ../../ | n/a |
| <a name="module_lambda_function_for_each"></a> [lambda\_function\_for\_each](#module\_lambda\_function\_for\_each) | ../../ | n/a |
| <a name="module_lambda_function_with_package_deploying_externally"></a> [lambda\_function\_with\_package\_deploying\_externally](#module\_lambda\_function\_with\_package\_deploying\_externally) | ../../ | n/a |
| <a name="module_lambda_layer_local"></a> [lambda\_layer\_local](#module\_lambda\_layer\_local) | ../../ | n/a |
| <a name="module_lambda_layer_s3"></a> [lambda\_layer\_s3](#module\_lambda\_layer\_s3) | ../../ | n/a |
| <a name="module_lambda_layer_with_package_deploying_externally"></a> [lambda\_layer\_with\_package\_deploying\_externally](#module\_lambda\_layer\_with\_package\_deploying\_externally) | ../../ | n/a |
| <a name="module_lambda_with_mixed_trusted_entities"></a> [lambda\_with\_mixed\_trusted\_entities](#module\_lambda\_with\_mixed\_trusted\_entities) | ../../ | n/a |
| <a name="module_lambda_with_provisioned_concurrency"></a> [lambda\_with\_provisioned\_concurrency](#module\_lambda\_with\_provisioned\_concurrency) | ../../ | n/a |
| <a name="module_s3_bucket"></a> [s3\_bucket](#module\_s3\_bucket) | terraform-aws-modules/s3-bucket/aws | n/a |

## Resources

| Name | Type |
|------|------|
| [aws_sqs_queue.dlq](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sqs_queue) | resource |
| [random_pet.this](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/pet) | resource |
| [aws_caller_identity.current](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/caller_identity) | data source |

## Inputs

No inputs.

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_lambda_cloudwatch_log_group_arn"></a> [lambda\_cloudwatch\_log\_group\_arn](#output\_lambda\_cloudwatch\_log\_group\_arn) | The ARN of the Cloudwatch Log Group |
| <a name="output_lambda_function_arn"></a> [lambda\_function\_arn](#output\_lambda\_function\_arn) | The ARN of the Lambda Function |
| <a name="output_lambda_function_invoke_arn"></a> [lambda\_function\_invoke\_arn](#output\_lambda\_function\_invoke\_arn) | The Invoke ARN of the Lambda Function |
| <a name="output_lambda_function_kms_key_arn"></a> [lambda\_function\_kms\_key\_arn](#output\_lambda\_function\_kms\_key\_arn) | The ARN for the KMS encryption key of Lambda Function |
| <a name="output_lambda_function_last_modified"></a> [lambda\_function\_last\_modified](#output\_lambda\_function\_last\_modified) | The date Lambda Function resource was last modified |
| <a name="output_lambda_function_name"></a> [lambda\_function\_name](#output\_lambda\_function\_name) | The name of the Lambda Function |
| <a name="output_lambda_function_qualified_arn"></a> [lambda\_function\_qualified\_arn](#output\_lambda\_function\_qualified\_arn) | The ARN identifying your Lambda Function Version |
| <a name="output_lambda_function_source_code_hash"></a> [lambda\_function\_source\_code\_hash](#output\_lambda\_function\_source\_code\_hash) | Base64-encoded representation of raw SHA-256 sum of the zip file |
| <a name="output_lambda_function_source_code_size"></a> [lambda\_function\_source\_code\_size](#output\_lambda\_function\_source\_code\_size) | The size in bytes of the function .zip file |
| <a name="output_lambda_function_url"></a> [lambda\_function\_url](#output\_lambda\_function\_url) | The URL of the Lambda Function URL |
| <a name="output_lambda_function_url_id"></a> [lambda\_function\_url\_id](#output\_lambda\_function\_url\_id) | The Lambda Function URL generated id |
| <a name="output_lambda_function_version"></a> [lambda\_function\_version](#output\_lambda\_function\_version) | Latest published version of Lambda Function |
| <a name="output_lambda_layer_arn"></a> [lambda\_layer\_arn](#output\_lambda\_layer\_arn) | The ARN of the Lambda Layer with version |
| <a name="output_lambda_layer_created_date"></a> [lambda\_layer\_created\_date](#output\_lambda\_layer\_created\_date) | The date Lambda Layer resource was created |
| <a name="output_lambda_layer_layer_arn"></a> [lambda\_layer\_layer\_arn](#output\_lambda\_layer\_layer\_arn) | The ARN of the Lambda Layer without version |
| <a name="output_lambda_layer_source_code_size"></a> [lambda\_layer\_source\_code\_size](#output\_lambda\_layer\_source\_code\_size) | The size in bytes of the Lambda Layer .zip file |
| <a name="output_lambda_layer_version"></a> [lambda\_layer\_version](#output\_lambda\_layer\_version) | The Lambda Layer version |
| <a name="output_lambda_role_arn"></a> [lambda\_role\_arn](#output\_lambda\_role\_arn) | The ARN of the IAM role created for the Lambda Function |
| <a name="output_lambda_role_name"></a> [lambda\_role\_name](#output\_lambda\_role\_name) | The name of the IAM role created for the Lambda Function |
| <a name="output_local_filename"></a> [local\_filename](#output\_local\_filename) | The filename of zip archive deployed (if deployment was from local) |
| <a name="output_s3_object"></a> [s3\_object](#output\_s3\_object) | The map with S3 object data of zip archive deployed (if deployment was from S3) |
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
