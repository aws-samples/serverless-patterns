# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# Variables
variable "lambda_name" {}
variable "lambda_handler" {}
variable "lambda_file" {}
variable "lambda_runtime" {}
variable "role_name" {}
variable "policy_name" {}
variable "env_variables" {}
variable "firehose_arn" {}
variable "queue_arn" {}
variable "tags" {}

data "aws_region" "current" {}

data "archive_file" "lambda_zip_file" {
  type = "zip"
  source_file = var.lambda_file
  output_path = "${trimsuffix(var.lambda_file,".py")}.zip"
}

# Resources
resource "aws_lambda_function" "lambda" {
  filename         = data.archive_file.lambda_zip_file.output_path
  function_name    = var.lambda_name
  handler          = var.lambda_handler
  tags             = var.tags
  source_code_hash = filebase64sha256(data.archive_file.lambda_zip_file.output_path)
  publish          = "true"
  runtime          = var.lambda_runtime
  role             = aws_iam_role.role.arn
  layers = ["arn:aws:lambda:${data.aws_region.current.name}:017000801446:layer:AWSLambdaPowertoolsPython:13"]

  environment {
    variables = var.env_variables
  }
}

data "aws_iam_policy_document" "lambda_policy" {

  statement {
    effect = "Allow"
    actions = [
      "firehose:PutRecord",
      "firehose:PutRecordBatch"
    ]
    resources = [
      var.firehose_arn
    ]
  }

  statement {
    effect = "Allow"
    actions = [
      "sqs:ReceiveMessage",
      "sqs:DeleteMessage",
      "sqs:GetQueueAttributes"
    ]
    resources = [
      var.queue_arn
    ]
  }

  statement {
    effect = "Allow"
    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]
    resources = [
      "${aws_cloudwatch_log_group.group.arn}:*"
    ]
  }
}

data "aws_iam_policy_document" "lambda_role" {
  statement {
    effect = "Allow"
    actions = [
      "sts:AssumeRole"
    ]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}


resource "aws_iam_policy" "policy" {
  name   = var.policy_name
  policy = data.aws_iam_policy_document.lambda_policy.json
  tags   = var.tags
}


resource "aws_iam_role" "role" {
  name               = var.role_name
  tags               = var.tags
  assume_role_policy = data.aws_iam_policy_document.lambda_role.json
}

resource "aws_iam_role_policy_attachment" "lambda_role_policy_attachement" {
  role       = aws_iam_role.role.name
  policy_arn = aws_iam_policy.policy.arn
}


resource "aws_lambda_event_source_mapping" "mapping" {
  event_source_arn = var.queue_arn
  function_name    = aws_lambda_function.lambda.arn
}


resource "aws_cloudwatch_log_group" "group" {
  name              = "/aws/lambda/${var.lambda_name}"
  retention_in_days = 30
  tags              = var.tags
}


# Outputs
output "aws_lambda_arn" {
  value = aws_lambda_function.lambda.arn
}

output "aws_lambda_version" {
  value = aws_lambda_function.lambda.version
}

output "aws_cloudwatch_log_group_arn" {
  value = aws_cloudwatch_log_group.group.arn
}

output "aws_iam_policy_name" {
  value = aws_iam_policy.policy.name
}

output "aws_iam_policy_arn" {
  value = aws_iam_policy.policy.arn
}

output "aws_iam_role_name" {
  value = aws_iam_role.role.name
}

output "aws_iam_role_arn" {
  value = aws_iam_role.role.arn
}
