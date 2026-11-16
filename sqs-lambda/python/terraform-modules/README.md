# Amazon SQS Queue to AWS Lambda

This pattern creates an Amazon SQS Queue, AWS Lambda function and setup event sourcing from the Queue to the Lambda function.

## Prerequisites

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [Terraform](https://developer.hashicorp.com/terraform/install) installed
* Python 3, which Terraform uses to build the function package

## Deployment Instructions

1. Clone the GitHub repository and change to the pattern directory:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/sqs-lambda/python/terraform-modules
    ```
1. Download the providers and modules, then deploy. The pattern deploys to `eu-west-1`; change the `provider "aws"` block in `main.tf` to use another Region.
    ```bash
    terraform init
    terraform apply
    ```
1. Enter `yes` at the prompt. Note the outputs, which you use for testing.

## Testing

After deployment, send a message to the SQS queue. Go to the CloudWatch Logs for the deployed Lambda function. You will see the event is logged out containing the item data.

To do this, you can run these commands in the terminal (replace `<queue-id>` with the value returned in `sqs_queue_id`):

```shell
aws sqs send-message --queue-url <queue-id> --message-body "Test message"

# Sample output
{
    "MD5OfMessageBody": "82dfa5549ebc9afc168eb7931ebece5f",
    "MessageId": "362f04c9-ac60-4f7b-be33-05e2dc0af2c2"
}
```

## Cleanup

1. Delete the resources from the pattern directory:
    ```bash
    cd serverless-patterns/sqs-lambda/python/terraform-modules
    terraform destroy
    ```
1. Enter `yes` at the prompt.

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
| <a name="provider_random"></a> [random](#provider\_random) | >= 2.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_lambda_function"></a> [lambda\_function](#module\_lambda\_function) | terraform-aws-modules/lambda/aws | ~> 4.0 |
| <a name="module_sqs"></a> [sqs](#module\_sqs) | terraform-aws-modules/sqs/aws | ~> 3.0 |

## Resources

| Name | Type |
|------|------|
| [random_pet.this](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/pet) | resource |

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
| <a name="output_sqs_queue_arn"></a> [sqs\_queue\_arn](#output\_sqs\_queue\_arn) | The ARN of the SQS queue |
| <a name="output_sqs_queue_id"></a> [sqs\_queue\_id](#output\_sqs\_queue\_id) | The URL for the created Amazon SQS queue |
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
