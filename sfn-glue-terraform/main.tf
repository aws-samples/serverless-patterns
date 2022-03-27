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

# Variables
variable "job_temp_dir" {
  default = ""
}

# Modules
module "amazon_s3" {
  source = "./modules/terraform-amazon-s3"
}

module "aws_glue" {
  source          = "./modules/terraform-aws-glue"
  script_location = "s3://${module.amazon_s3.bucket_name}/${module.amazon_s3.glue_script_name}"
  temp_dir        = var.job_temp_dir
  s3_bucket_arn   = module.amazon_s3.bucket_arn
  s3_bucket_name  = module.amazon_s3.bucket_name
}

module "aws_sfn_state_machine" {
  source        = "./modules/terraform-aws-step-function"
  glue_job_arn  = module.aws_glue.glue_job_arn
  glue_job_name = module.aws_glue.glue_job_name
}

module "aws_cloudwatch_event" {
  source            = "./modules/terraform-aws-cloudwatch"
  stf_function_arn  = module.aws_sfn_state_machine.stf_arn
  stf_function_name = module.aws_sfn_state_machine.stf_name
}

# Outputs
output "aws_s3_bucket_arn" {
  value = module.amazon_s3.bucket_arn
}

output "aws_cloudwatch_event_rule_arn" {
  value = module.aws_cloudwatch_event.aws_cloudwatch_event_rule_arn
}

output "aws_step_function_arn" {
  value = module.aws_sfn_state_machine.stf_role_arn
}

output "aws_glue_job_arn" {
  value = module.aws_glue.glue_job_arn
}

