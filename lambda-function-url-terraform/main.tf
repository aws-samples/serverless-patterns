terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.21"
    }
  }

  required_version = "~> 1.2"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_lambda_function" "lambda_function" {
  function_name    = "FURLFunction"
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = data.archive_file.lambda_zip_file.output_base64sha256
  handler          = "app.handler"
  role             = aws_iam_role.lambda_iam_role.arn
  runtime          = "nodejs14.x"
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
  name_prefix = "LambdaFunctionRole-"
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

resource "aws_lambda_function_url" "function_url" {
  function_name      = aws_lambda_function.lambda_function.function_name
  authorization_type = "AWS_IAM"

  cors {
    allow_origins     = ["*"]
  }
}

output "FunctionARN" {
  value       = aws_lambda_function.lambda_function.arn
  description = "Lambda function name"
}

output "FunctionUrlEndpoint" {
  value       = aws_lambda_function_url.function_url.function_url
  description = "Lambda function url"
}