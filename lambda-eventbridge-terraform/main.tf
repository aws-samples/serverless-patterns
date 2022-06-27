terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.20.1"
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
  name = "PublisherFunctionRole"
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
  name   = "event_bridge_put_events_policy"
  path   = "/"
  policy = data.aws_iam_policy_document.event_bridge_put_events_policy_document.json
}

resource "aws_iam_policy_attachment" "attach_event_bus_policy" {
  name       = "event-bus-policy-attachment"
  roles      = [aws_iam_role.iam_for_lambda.name]
  policy_arn = aws_iam_policy.event_bridge_put_events_policy.arn
}

output "publisher_function" {
  value       = aws_lambda_function.publisher_function.arn
  description = "PublisherFunction function name"
}
