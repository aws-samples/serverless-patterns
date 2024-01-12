## AWS Lambda and Amazon Bedrock Integration

This pattern will provision Amazon Elastic Container Registry (ECR), push the code into the Container Registry along with AWS Lambda function to execute the container.

As part of the build process, a container will be built, pushed into ECR, and ultimately deployed as an AWS Lambda function. When an AWS Lambda is executed, it makes API calls to Amazon Bedrock and uses the prompt that the user has provided to get a generative answer from the foundation model. Logs will be sent to AWS Cloudwatch once the execution of the AWS lambda function is finished. The security component is likewise handled by KMS Keys and IAM Roles.

## Getting started with Terraform Serverless Patterns

Read more about general requirements and deployment instructions for Terraform Serverless Patterns [here](https://github.com/aws-samples/serverless-patterns/blob/main/terraform-fixtures/docs/README.md).

Before attempting this pattern, you must enable [model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) in your AWS Account. To provide you flexibility with foundation models, you can enable all or some of the foundation models. This pattern employs the anthropic.claude-v2 model by default so that's must be enabled for this pattern to work

You also need [docker](https://www.docker.com/) and md5 to be installed on your testing machine

## Deployment and Testing Instructions

The deployment will require you to provide the AWS VPC id along with the Subnet id(s) where you want this pattern to be deployed. It is expected that the subnets provided have internet access via NAT Gateway (incase of private subnets) or otherwise. Additionally, You can use AWS PrivateLink to create a private connection between your VPC and Amazon Bedrock. You can access Amazon Bedrock as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. You establish this private connection by creating an interface endpoint, powered by AWS PrivateLink. For more information, see [ Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the AWS PrivateLink Guide.

Optionally, you can also specify foundation model name, env and organization (tagging purposes), timeout and memory_size (AWS Lambda function compute purposes) and lastly logging_level to specify the logging level for your function. These values default to entires in the variable.tf file if not provided at deployment.

```shell
# terraform init
terraform init

# terraform plan with sample values for vpc and subnet
terraform plan  -var="aws_vpc_id=vpc-xxxx" -var='aws_subnets=["subnet-xxxx","subnet-xxxx","subnet-xxxx"]' 

# terraform apply
terraform apply -var="aws_vpc_id=vpc-xxxx" -var='aws_subnets=["subnet-xxxx","subnet-xxxx","subnet-xxxx"]' 
```

Once deployed you can execute the Lambda function from the AWS Lambda Console or via AWS CLI. The logs will be published to Amazon Cloudwatch.

```shell
aws lambda invoke \
    --function-name testing-serverlessland-genai-app \
    --cli-binary-format raw-in-base64-out \
    --log-type Tail --query 'LogResult' --output text \
    --payload '{ "prompt_data": "Tell me more about AWS" }' \
    response.json  | base64 --decode
```

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | >= 5.24 |
| <a name="requirement_external"></a> [external](#requirement\_external) | >= 2.3 |
| <a name="requirement_null"></a> [null](#requirement\_null) | >= 3.2 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | >= 5.24 |
| <a name="provider_external"></a> [external](#provider\_external) | >= 2.3 |
| <a name="provider_null"></a> [null](#provider\_null) | >= 3.2 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_cloudwatch_log_group.this_aws_cloudwatch_log_group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_group) | resource |
| [aws_ecr_lifecycle_policy.ecr_lifecycle_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecr_lifecycle_policy) | resource |
| [aws_ecr_repository.this_aws_ecr_repository](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecr_repository) | resource |
| [aws_iam_policy.this_aws_iam_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_policy_attachment.this_aws_iam_policy_attachment](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy_attachment) | resource |
| [aws_iam_role.this_aws_iam_role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_kms_alias.this_aws_kms_alias](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/kms_alias) | resource |
| [aws_kms_key.this_aws_kms_key](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/kms_key) | resource |
| [aws_lambda_function.this_aws_lambda_function](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function) | resource |
| [aws_security_group.this_aws_security_group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group) | resource |
| [null_resource.this_null_resource](https://registry.terraform.io/providers/hashicorp/null/latest/docs/resources/resource) | resource |
| [aws_caller_identity.current](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/caller_identity) | data source |
| [aws_ecr_image.this_aws_ecr_image](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/ecr_image) | data source |
| [aws_region.current](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/region) | data source |
| [external_external.this_external](https://registry.terraform.io/providers/hashicorp/external/latest/docs/data-sources/external) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_aws_subnets"></a> [aws\_subnets](#input\_aws\_subnets) | A list of subnets inside the VPC | `set(any)` | n/a | yes |
| <a name="input_aws_vpc_id"></a> [aws\_vpc\_id](#input\_aws\_vpc\_id) | VPC ID for Lambda Task | `string` | n/a | yes |
| <a name="input_bedrock_foundation_model"></a> [bedrock\_foundation\_model](#input\_bedrock\_foundation\_model) | Bedrock Foundation Model | `string` | `"anthropic.claude-v2"` | no |
| <a name="input_env"></a> [env](#input\_env) | Name of the environment this infrastructure is for | `string` | `"testing"` | no |
| <a name="input_logging_level"></a> [logging\_level](#input\_logging\_level) | Level of logging required for this Lambda function | `string` | `"INFO"` | no |
| <a name="input_memory_size"></a> [memory\_size](#input\_memory\_size) | Memory for Lambda Task | `number` | `512` | no |
| <a name="input_organization"></a> [organization](#input\_organization) | Name of the organization this infrastructure is for | `string` | `"serverlessland"` | no |
| <a name="input_timeout"></a> [timeout](#input\_timeout) | Timeout for Lambda Task | `number` | `900` | no |

## Outputs

No outputs.
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
