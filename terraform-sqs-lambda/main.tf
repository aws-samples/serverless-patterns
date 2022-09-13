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
      service  = "sqs"
      source_arn = aws_sqs_queue.this.arn
    }
  }

  event_source_mapping = {
    sqs = {
      event_source_arn        = aws_sqs_queue.this.arn
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

resource "aws_sqs_queue" "this" {
  name = random_pet.this.id

  tags = {
    Pattern = "terraform-sqs-lambda"
    Module  = "aws_sqs_queue"
  }
}

##################
# Extra resources
##################

resource "random_pet" "this" {
  length = 2
}
