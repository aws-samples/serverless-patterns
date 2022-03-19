# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

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
  profile = "default"
  region  = "us-east-1"
}

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "archive_file" "lambda_zip_file" {
  type = "zip"
  source_file = "${path.module}/src/app.py"
  output_path = "${path.module}/lambda.zip"
}

resource "aws_sqs_queue" "sqs_lambda_demo_queue" {
  name = "sqs-lambda-demo-${data.aws_caller_identity.current.account_id}"
}

# Role to execute lambda
resource "aws_iam_role" "sqs_lambda_demo_functionrole" {
  name               = "sqs_lambda_demo_functionrole"
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

# CloudWatch Log group to store Lambda logs
resource "aws_cloudwatch_log_group" "sqs_lambda_demo_loggroup" {
  name = "/aws/lambda/${aws_lambda_function.sqs_lambda_demo_function.function_name}"
  retention_in_days = 365
}

# Custom policy to read SQS queue and write to CloudWatch Logs with least privileges
resource "aws_iam_policy" "sqs_lambda_demo_lambdapolicy" {
  name        = "sqs-lambda-demo-lambdapolicy"
  path        = "/"
  description = "Policy for sqs to lambda demo"
  policy = <<EOF
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect": "Allow",
      "Action": [
        "sqs:ReceiveMessage",
        "sqs:DeleteMessage",
        "sqs:GetQueueAttributes"
      ],
      "Resource": "${aws_sqs_queue.sqs_lambda_demo_queue.arn}"
    },
    {
      "Effect": "Allow",
      "Action": [
          "logs:CreateLogStream",
          "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${aws_lambda_function.sqs_lambda_demo_function.function_name}:*:*"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_policy_attachment" {
  role = aws_iam_role.sqs_lambda_demo_functionrole.name
  policy_arn = aws_iam_policy.sqs_lambda_demo_lambdapolicy.arn
}

resource "aws_lambda_function" "sqs_lambda_demo_function" {
  function_name = "sqs-lambda-demo-${data.aws_caller_identity.current.account_id}"
  filename = data.archive_file.lambda_zip_file.output_path
  source_code_hash = filebase64sha256(data.archive_file.lambda_zip_file.output_path)
  role = aws_iam_role.sqs_lambda_demo_functionrole.arn
  handler = "app.lambda_handler"
  runtime = "python3.9"
  layers = ["arn:aws:lambda:${data.aws_region.current.name}:017000801446:layer:AWSLambdaPowertoolsPython:13"]
  environment {
    variables = {
      POWERTOOLS_SERVICE_NAME = "sqs-lambda-demo"
    }
  }
}

resource "aws_lambda_event_source_mapping" "sqs_lambda_demo_sourcemapping" {
  event_source_arn = aws_sqs_queue.sqs_lambda_demo_queue.arn
  function_name = aws_lambda_function.sqs_lambda_demo_function.function_name
}


output "sqs_queue_url" {
  value = aws_sqs_queue.sqs_lambda_demo_queue.url
}

output "sqs_queue_arn" {
  value = aws_sqs_queue.sqs_lambda_demo_queue.arn
}

output "lambda_function_name" {
  value = aws_lambda_function.sqs_lambda_demo_function.function_name
}

output "cloudwatch_log_group" {
  value = aws_cloudwatch_log_group.sqs_lambda_demo_loggroup.name
}
