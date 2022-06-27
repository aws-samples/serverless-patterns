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

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "aws_partition" "current" {}

resource "aws_sns_topic" "sns_topic" {}

resource "aws_lambda_function" "lambda_function" {
  function_name    = "TopicPublisherFunction"
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = data.archive_file.lambda_zip_file.output_base64sha256
  handler          = "app.handler"
  role             = aws_iam_role.lambda_iam_role.arn
  runtime          = "nodejs14.x"
  environment {
    variables = {
      SNStopic = aws_sns_topic.sns_topic.arn
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
  name = "LambdaSSMParameterRole"
  managed_policy_arns = [data.aws_iam_policy.lambda_basic_execution_role_policy.arn]

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
      "sns:Publish"
    ]

    resources = [
      aws_sns_topic.sns_topic.arn
    ]
  }
}

resource "aws_iam_policy" "lambda_policy" {
  name   = "lambda_policy"
  path   = "/"
  policy = data.aws_iam_policy_document.lambda_policy_document.json
}

resource "aws_iam_policy_attachment" "attach_lambda_iam_policy" {
  name       = "lambda-policy-attachment"
  roles      = [aws_iam_role.lambda_iam_role.name]
  policy_arn = aws_iam_policy.lambda_policy.arn
}

output "TopicPublisherFunction" {
  value       = aws_lambda_function.lambda_function.arn
  description = "TopicPublisherFunction function name"
}

output "SNStopicARN" {
  value       = aws_sns_topic.sns_topic.arn
  description = "SNS topic ARN"
}
