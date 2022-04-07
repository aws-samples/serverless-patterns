# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# Terraform and AWS configurations
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }

  required_version = ">= 1.0.0"
}

provider "aws" {
  profile = var.profile
  region  = var.region
}

# Local variables
locals {
  tags = merge({
    pattern     = "fifo-sns-sqs-lambda-firehose-s3"
    deployed_by = "terraform"
    repository  = "https://github.com/aws-samples/serverless-patterns/tree/main/fifo-sns-sqs-lambda-firehose-s3"
  }, var.tags)
  prefix = "fifo-sns-sqs-lambda-firehose-s3"
}

# Variables
variable "region" {
  type        = string
  default     = "us-east-1"
  description = "The region to deploy to."
}

variable "profile" {
  type        = string
  default     = "default"
  description = "The aws profile to use for the deployment"
}

variable "tags" {
  type        = map(string)
  default     = {}
  description = "Resource tags."
}


# resources
resource "random_id" "seed" {
  byte_length = 4
}

module "aws_s3_bucket" {
  source      = "./modules/terraform-aws-s3"
  bucket_name = "${local.prefix}-bucket-${random_id.seed.hex}"
  tags        = local.tags
}

module "aws_sqs_queue" {
  source     = "./modules/terraform-aws-sqs"
  queue_name = "${local.prefix}-queue-${random_id.seed.hex}.fifo"
  topic_arn  = module.aws_sns_topic.aws_sns_topic_arn
  tags       = local.tags
}

module "aws_sns_topic" {
  source     = "./modules/terraform-aws-sns"
  topic_name = "${local.prefix}-topic-${random_id.seed.hex}.fifo"
  queue_arn  = module.aws_sqs_queue.aws_sqs_queue_arn
  tags       = local.tags
}


module "aws_firehose_delivery_stream" {
  source      = "./modules/terraform-aws-firehose"
  stream_name = "${local.prefix}-stream-${random_id.seed.hex}"
  destination = "extended_s3"
  bucket_arn  = module.aws_s3_bucket.aws_s3_bucket_arn
  role_name   = "${local.prefix}-firehose-role-${random_id.seed.hex}"
  policy_name = "${local.prefix}-firehose-policy-${random_id.seed.hex}"
  tags        = local.tags
}


module "aws_lambda" {
  source         = "./modules/terraform-aws-lambda"
  lambda_name    = "${local.prefix}-lambda-${random_id.seed.hex}"
  lambda_handler = "lambdaFirehoseLogger.lambdaFirehoseLogger"
  lambda_file    = "./assets/lambda/lambdaFirehoseLogger.py"
  lambda_runtime = "python3.8"
  env_variables  = {
    "FIREHOSE_STREAM_NAME" : "${local.prefix}-stream-${random_id.seed.hex}"
  }

  policy_name  = "${local.prefix}-lambda-policy-${random_id.seed.hex}"
  role_name    = "${local.prefix}-lambda-role-${random_id.seed.hex}"
  queue_arn    = module.aws_sqs_queue.aws_sqs_queue_arn
  firehose_arn = module.aws_firehose_delivery_stream.aws_firehose_delivery_stream_arn
  tags         = local.tags
}


# Outputs
output "s3_bucket" {
  value = {
    arn = module.aws_s3_bucket.aws_s3_bucket_arn
  }
}

output "sqs_fifo_queue" {
  value = {
    name = module.aws_sqs_queue.aws_sqs_queue_name,
    arn  = module.aws_sqs_queue.aws_sqs_queue_arn
  }
}

output "sns_fifo_topic" {
  value = {
    name = module.aws_sns_topic.aws_sns_topic_name,
    arn  = module.aws_sns_topic.aws_sns_topic_arn
  }
}

output "lambda_function" {
  value = {
    arn                      = module.aws_lambda.aws_lambda_arn,
    version                  = module.aws_lambda.aws_lambda_version,
    cloudwatch_log_group_arn = module.aws_lambda.aws_cloudwatch_log_group_arn,
    policy_name              = module.aws_lambda.aws_iam_policy_name,
    policy_arn               = module.aws_lambda.aws_iam_policy_arn,
    role_name                = module.aws_lambda.aws_iam_role_name,
    role_arn                 = module.aws_lambda.aws_iam_role_arn
  }
}

output "firehose_delivery_stream" {
  value = {
    arn         = module.aws_firehose_delivery_stream.aws_firehose_delivery_stream_arn,
    policy_name = module.aws_firehose_delivery_stream.aws_firehose_policy_name,
    policy_arn  = module.aws_firehose_delivery_stream.aws_firehose_policy_arn,
    role_name   = module.aws_firehose_delivery_stream.aws_firehose_role_name,
    role_arn    = module.aws_firehose_delivery_stream.aws_firehose_role_arn
  }
}


