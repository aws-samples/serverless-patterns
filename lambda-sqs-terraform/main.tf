terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.22"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_sqs_queue" "sqs_queue" {}

resource "aws_lambda_function" "lambda_function" {
  function_name    = "QueuePublisherFunction"
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = data.archive_file.lambda_zip_file.output_base64sha256
  handler          = "app.handler"
  role             = aws_iam_role.lambda_iam_role.arn
  runtime          = "nodejs14.x"
  environment {
    variables = {
      SQSqueueName = aws_sqs_queue.sqs_queue.url
    }
  }
}

data "archive_file" "lambda_zip_file" {
  type        = "zip"
  source_file = "${path.module}/src/app.js"
  output_path = "${path.module}/lambda.zip"
}

data "aws_iam_policy" "lambda_basic_execution_role_policy" {
  name = "AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role" "lambda_iam_role" {
  name_prefix         = "LambdaSQSRole-"
  managed_policy_arns = [
    data.aws_iam_policy.lambda_basic_execution_role_policy.arn,
    aws_iam_policy.lambda_policy.arn
  ]

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

data "aws_iam_policy_document" "lambda_policy_document" {
  statement {
  
    effect = "Allow"
  
    actions = [
      "sqs:SendMessage*"
    ]

    resources = [
      aws_sqs_queue.sqs_queue.arn
    ]
  }
}

resource "aws_iam_policy" "lambda_policy" {
  name_prefix = "lambda_policy"
  path        = "/"
  policy      = data.aws_iam_policy_document.lambda_policy_document.json
  lifecycle {
    create_before_destroy = true
  }
}

output "QueuePublisherFunction" {
  value       = aws_lambda_function.lambda_function.arn
  description = "QueuePublisherFunction function name"
}

output "SQSqueueARN" {
  value       = aws_sqs_queue.sqs_queue.arn
  description = "SQS queue ARN"
}

output "SQSqueueURL" {
  value       = aws_sqs_queue.sqs_queue.url
  description = "SQS queue URL"
}
