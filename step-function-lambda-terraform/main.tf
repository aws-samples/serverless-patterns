# terraform and AWS configurations
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}
provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

# Modules
module "aws_lambda_function" {
  source          = "./modules/terraform-aws-lambda"
}
module "aws_sfn_state_machine" {
  source              = "./modules/terraform-aws-step-function"
  lambda_function_arn = module.aws_lambda_function.lambda_role_arn
}

module "aws_cloudwatch_event" {
  source = "./modules/terraform-aws-cloudwatch"
  stf_function_arn =module.aws_sfn_state_machine.stf_arn
  stf_function_name = module.aws_sfn_state_machine.stf_name
}

# Outputs
output "aws_lambda_function_arn" {
  value = module.aws_lambda_function.lambda_role_arn
}

output "aws_step_function_arn" {
  value = module.aws_sfn_state_machine.stf_role_arn
}

output "aws_cloudwatch_event_rule_arn" {
value = module.aws_cloudwatch_event.aws_cloudwatch_event_rule_arn
}