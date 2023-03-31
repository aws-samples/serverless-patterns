# AWS Lambda and Cloudtrail data events

This pattern demonstrates how customers can monitor manual invocations of their sensitive lambda functions through slack with the help of Cloudtrail and Cloudwatch Subscription filter.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cloudtrail-lambda-slack

## Getting started with Terraform Serverless Patterns
Read more about general requirements and deployment instructions for Terraform Serverless Patterns [here](https://github.com/aws-samples/serverless-patterns/blob/main/terraform-fixtures/docs/README.md). 

## Testing

Invoke the lambda function manually from the console and after 5 minutes you should see the message in your slack channel showing the user invocation.

```

#sample message:
User 'arn:aws:iam::<account-id>:user/RogueUser' performed Invoke on function 'arn:aws:lambda:us-east-1:<account-id>:function:testfunction' at 2023-03-27T13:04:09Z


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


## Inputs

| Name | Input Value |
|------|---------|
| <a name="provider_random"></a> [random](#provider\_random) | >= 2.0 |

