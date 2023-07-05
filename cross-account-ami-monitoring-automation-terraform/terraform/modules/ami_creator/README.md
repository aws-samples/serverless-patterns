## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | >= 4.20.1 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_archive"></a> [archive](#provider\_archive) | n/a |
| <a name="provider_aws"></a> [aws](#provider\_aws) | >= 4.20.1 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_consume_ami_in_creator_account"></a> [consume\_ami\_in\_creator\_account](#module\_consume\_ami\_in\_creator\_account) | ../ami_consumer | n/a |

## Resources

| Name | Type |
|------|------|
| [aws_cloudwatch_event_rule.modify_image_attribute_event](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_rule) | resource |
| [aws_cloudwatch_event_target.ami_share_event_target](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_target) | resource |
| [aws_dynamodb_table.ami_share_dynamodb_table](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dynamodb_table) | resource |
| [aws_iam_policy.dynamodb_external_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_policy_attachment.external_ddb_role_attachment](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy_attachment) | resource |
| [aws_iam_role.ami_share_lambda_role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role.external_ddb_role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role_policy.ami_share_lambda_role_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy) | resource |
| [aws_iam_role_policy_attachment.ami_share_role_policy_attachment](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_lambda_function.ami_share_lambda](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function) | resource |
| [aws_lambda_permission.allow_eventbridge_to_invoke_lambda](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_permission) | resource |
| [aws_ses_email_identity.this](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ses_email_identity) | resource |
| [aws_ssm_parameter.emails](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ssm_parameter) | resource |
| [archive_file.ami_share_lambda_function](https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file) | data source |
| [aws_caller_identity.creation_account](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/caller_identity) | data source |
| [aws_iam_policy_document.ami_share_assume_role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.ami_share_lambda_policy_document](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.external_assume_role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.external_dynamodb_access_policy_document](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_region.creation_account](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/region) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_account_email_mapping"></a> [account\_email\_mapping](#input\_account\_email\_mapping) | Account id and email id mapping of AWS Account's | <pre>list(object({<br>    account = string<br>    email   = string<br>  }))</pre> | n/a | yes |
| <a name="input_ami_share_function_name"></a> [ami\_share\_function\_name](#input\_ami\_share\_function\_name) | AWS Lambda function name of AMI share function | `string` | `"ami-share-function"` | no |
| <a name="input_consumer"></a> [consumer](#input\_consumer) | Enable AMI Consumption in the creator account | `bool` | `false` | no |
| <a name="input_iam_policy_arn"></a> [iam\_policy\_arn](#input\_iam\_policy\_arn) | Additional IAM Policy to be attached to role | `list(string)` | `[]` | no |
| <a name="input_lambda_memory_size"></a> [lambda\_memory\_size](#input\_lambda\_memory\_size) | AWS Lambda function memory size | `number` | `128` | no |
| <a name="input_lambda_runtime"></a> [lambda\_runtime](#input\_lambda\_runtime) | AWS Lambda function execution runtime | `string` | `"python3.9"` | no |
| <a name="input_lambda_timeout"></a> [lambda\_timeout](#input\_lambda\_timeout) | AWS Lambda function execution timeout | `number` | `300` | no |
| <a name="input_ssm_prefix"></a> [ssm\_prefix](#input\_ssm\_prefix) | Prefix for SSM parameter store | `string` | `"/cross-account-ami"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_configurations_details"></a> [configurations\_details](#output\_configurations\_details) | n/a |