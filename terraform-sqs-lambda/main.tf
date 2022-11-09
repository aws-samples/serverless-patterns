provider "aws" {
  region = "eu-west-1"
}

####################################################
# Lambda Function (building from source)
####################################################

module "lambda_function" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "~> 4.0"

  function_name = "${random_pet.this.id}-lambda"
  description   = "My awesome lambda function"
  handler       = "index.lambda_handler"
  runtime       = "python3.8"
  publish       = true

  source_path = "${path.module}/../terraform-fixtures/python"

  allowed_triggers = {
    sqs = {
      service    = "sqs"
      source_arn = module.sqs.sqs_queue_arn
    }
  }

  event_source_mapping = {
    sqs = {
      event_source_arn        = module.sqs.sqs_queue_arn
      function_response_types = ["ReportBatchItemFailures"]
    }
  }

  attach_policies    = true
  number_of_policies = 1

  policies = [
    "arn:aws:iam::aws:policy/service-role/AWSLambdaSQSQueueExecutionRole",
  ]

  tags = {
    Pattern = "terraform-sqs-lambda"
    Module  = "lambda_function"
  }
}

############
# SQS Queue
############

module "sqs" {
  source  = "terraform-aws-modules/sqs/aws"
  version = "~> 3.0"

  name = random_pet.this.id

  tags = {
    Pattern = "terraform-sqs-lambda"
    Module  = "sqs"
  }
}

##################
# Extra resources
##################

resource "random_pet" "this" {
  length = 2
}
