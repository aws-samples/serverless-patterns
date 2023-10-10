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

variable "event_bus_name" {
  type = string
  default = "default"
}

data "aws_cloudwatch_event_bus" "event_bus" {
  name = var.event_bus_name
}

resource "aws_lambda_function" "publisher_function" {
  function_name    = "PublisherFunction"
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = data.archive_file.lambda_zip_file.output_base64sha256
  handler          = "app.handler"
  role             = aws_iam_role.iam_for_lambda.arn
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

resource "aws_iam_role" "iam_for_lambda" {
  name_prefix         = "PublisherFunctionRole-"
  managed_policy_arns = [
    data.aws_iam_policy.lambda_basic_execution_role_policy.arn,
    aws_iam_policy.event_bridge_put_events_policy.arn
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

data "aws_iam_policy_document" "event_bridge_put_events_policy_document" {
  statement {
  
    effect = "Allow"
  
    actions = [
      "events:PutEvents"
    ]

    resources = [
      data.aws_cloudwatch_event_bus.event_bus.arn
    ]
  }
}

resource "aws_iam_policy" "event_bridge_put_events_policy" {
  name_prefix = "event_bridge_put_events_policy-"
  path        = "/"
  policy      = data.aws_iam_policy_document.event_bridge_put_events_policy_document.json
  lifecycle {
    create_before_destroy = true
  }
}

output "publisher_function" {
  value       = aws_lambda_function.publisher_function.arn
  description = "PublisherFunction function name"
}
