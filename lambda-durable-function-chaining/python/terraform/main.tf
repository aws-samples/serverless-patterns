############################################################
# Terraform Configuration
############################################################

terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.32.1"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.7"
    }
  }
}

############################################################
# Provider
############################################################

provider "aws" {
  region = var.aws_region
}

############################################################
# Variables
############################################################

variable "aws_region" {
  description = "AWS region for resources (e.g. us-east-1, us-west-2)"
  type        = string

  validation {
    condition     = can(regex("^[a-z]{2}-[a-z]+-[0-9]+$", var.aws_region))
    error_message = "Must be a valid AWS region (e.g. us-east-1, eu-west-2)."
  }
}

variable "prefix" {
  description = "Unique prefix for all resource names"
  type        = string

  validation {
    condition     = can(regex("^[a-z0-9][a-z0-9\\-]{1,20}$", var.prefix))
    error_message = "Prefix must be 2-21 lowercase alphanumeric characters or hyphens."
  }
}

variable "log_retention_days" {
  description = "CloudWatch log retention in days (0 = never expire)"
  type        = number
  default     = 14
}

############################################################
# IAM Role – Worker Lambda Functions (non-durable)
############################################################

resource "aws_iam_role" "worker_role" {
  name = "${var.prefix}-worker-role"

  force_detach_policies = true

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Action    = "sts:AssumeRole"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "worker_basic_execution" {
  role       = aws_iam_role.worker_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

############################################################
# IAM Role – Durable Orchestrator Lambda Function
############################################################

resource "aws_iam_role" "orchestrator_role" {
  name = "${var.prefix}-durable-orchestrator-role"

  force_detach_policies = true

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Action    = "sts:AssumeRole"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "durable_execution" {
  role       = aws_iam_role.orchestrator_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicDurableExecutionRolePolicy"
}

############################################################
# CloudWatch Log Groups (Terraform-managed)
############################################################

resource "aws_cloudwatch_log_group" "step1" {
  name              = "/aws/lambda/${var.prefix}-step1-add"
  retention_in_days = var.log_retention_days
  skip_destroy      = false
}

resource "aws_cloudwatch_log_group" "step2" {
  name              = "/aws/lambda/${var.prefix}-step2-transform"
  retention_in_days = var.log_retention_days
  skip_destroy      = false
}

resource "aws_cloudwatch_log_group" "step3" {
  name              = "/aws/lambda/${var.prefix}-step3-finalize"
  retention_in_days = var.log_retention_days
  skip_destroy      = false
}

resource "aws_cloudwatch_log_group" "orchestrator" {
  name              = "/aws/lambda/${var.prefix}-durable-orchestrator"
  retention_in_days = var.log_retention_days
  skip_destroy      = false
}

############################################################
# Worker Lambda Functions
############################################################

resource "aws_lambda_function" "step1" {
  function_name = "${var.prefix}-step1-add"
  filename      = "step1_add.zip"
  handler       = "step1_add.lambda_handler"
  runtime       = "python3.14"
  memory_size   = 512
  timeout       = 30
  role          = aws_iam_role.worker_role.arn

  logging_config {
    log_group  = aws_cloudwatch_log_group.step1.name
    log_format = "Text"
  }

  depends_on = [
    aws_cloudwatch_log_group.step1
  ]
}

resource "aws_lambda_function" "step2" {
  function_name = "${var.prefix}-step2-transform"
  filename      = "step2_transform.zip"
  handler       = "step2_transform.lambda_handler"
  runtime       = "python3.14"
  memory_size   = 512
  timeout       = 30
  role          = aws_iam_role.worker_role.arn

  logging_config {
    log_group  = aws_cloudwatch_log_group.step2.name
    log_format = "Text"
  }

  depends_on = [
    aws_cloudwatch_log_group.step2
  ]
}

resource "aws_lambda_function" "step3" {
  function_name = "${var.prefix}-step3-finalize"
  filename      = "step3_finalize.zip"
  handler       = "step3_finalize.lambda_handler"
  runtime       = "python3.14"
  memory_size   = 512
  timeout       = 30
  role          = aws_iam_role.worker_role.arn

  logging_config {
    log_group  = aws_cloudwatch_log_group.step3.name
    log_format = "Text"
  }

  depends_on = [
    aws_cloudwatch_log_group.step3
  ]
}

############################################################
# Allow Orchestrator to Invoke Worker Functions
############################################################

resource "aws_iam_role_policy" "invoke_workers" {
  name = "${var.prefix}-invoke-worker-functions"
  role = aws_iam_role.orchestrator_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = ["lambda:InvokeFunction"]
      Resource = [
        aws_lambda_function.step1.arn,
        aws_lambda_function.step2.arn,
        aws_lambda_function.step3.arn,
        "${aws_lambda_function.step1.arn}:*",
        "${aws_lambda_function.step2.arn}:*",
        "${aws_lambda_function.step3.arn}:*"
      ]
    }]
  })
}

############################################################
# Inline Orchestrator Source Code
#
# The durable execution SDK (@durable_execution decorator and
# DurableContext) is built into the python3.14 runtime when
# durable_config is set — no extra layer is needed.
############################################################

data "archive_file" "orchestrator" {
  type        = "zip"
  output_path = "${path.module}/orchestrator.zip"

  source {
    filename = "orchestrator.py"
    content  = <<-PYTHON
      import json
      import os
      import logging
      import boto3
      from aws_durable_execution_sdk_python import DurableContext, durable_execution

      logger = logging.getLogger()
      logger.setLevel(logging.INFO)

      lambda_client = boto3.client('lambda')


      def call_lambda(function_arn, payload):
          """Invoke a regular Lambda function and return parsed response."""
          response = lambda_client.invoke(
              FunctionName=function_arn,
              InvocationType='RequestResponse',
              Payload=json.dumps(payload)
          )

          if 'FunctionError' in response:
              error_payload = json.loads(response['Payload'].read())
              raise RuntimeError(f"Function {function_arn} failed: {error_payload}")

          return json.loads(response['Payload'].read())


      @durable_execution
      def lambda_handler(event, context: DurableContext):
          step1_arn = os.environ['STEP1_FUNCTION_ARN']
          step2_arn = os.environ['STEP2_FUNCTION_ARN']
          step3_arn = os.environ['STEP3_FUNCTION_ARN']

          logger.info("Orchestrator invoked with event: %s", json.dumps(event, default=str))

          # Step 1 — lambda receives the arg context.step() passes; ignored here
          result1 = context.step(
              lambda _: call_lambda(step1_arn, event),
              name='step1-add'
          )
          logger.info("STEP1 result: %s", json.dumps(result1, default=str))

          # Step 2
          result2 = context.step(
              lambda _: call_lambda(step2_arn, result1),
              name='step2-transform'
          )
          logger.info("STEP2 result: %s", json.dumps(result2, default=str))

          # Step 3
          result3 = context.step(
              lambda _: call_lambda(step3_arn, result2),
              name='step3-finalize'
          )
          logger.info("STEP3 result: %s", json.dumps(result3, default=str))

          response = {
              'workflow': 'completed',
              'input': event,
              'output': result3
          }
          logger.info("Final response: %s", json.dumps(response, default=str))
          return response
    PYTHON
  }
}

############################################################
# Durable Orchestrator Function
############################################################

resource "aws_lambda_function" "orchestrator" {
  function_name    = "${var.prefix}-durable-orchestrator"
  filename         = data.archive_file.orchestrator.output_path
  source_code_hash = data.archive_file.orchestrator.output_base64sha256
  handler          = "orchestrator.lambda_handler"
  runtime          = "python3.14"
  memory_size      = 512
  timeout          = 90
  role             = aws_iam_role.orchestrator_role.arn
  publish          = true

  durable_config {
    execution_timeout = 90
    retention_period  = 7
  }

  logging_config {
    log_group  = aws_cloudwatch_log_group.orchestrator.name
    log_format = "JSON"
  }

  environment {
    variables = {
      STEP1_FUNCTION_ARN = aws_lambda_function.step1.arn
      STEP2_FUNCTION_ARN = aws_lambda_function.step2.arn
      STEP3_FUNCTION_ARN = aws_lambda_function.step3.arn
    }
  }

  timeouts {
    delete = "6m"
  }

  tags = {
    Project     = "${var.prefix}-durable-workflow"
    Environment = "dev"
    Type        = "durable"
  }

  depends_on = [
    aws_cloudwatch_log_group.orchestrator
  ]
}

############################################################
# Alias
############################################################

resource "aws_lambda_alias" "live" {
  name             = "live"
  function_name    = aws_lambda_function.orchestrator.function_name
  function_version = aws_lambda_function.orchestrator.version
}

############################################################
# Outputs
############################################################

output "orchestrator_alias_arn" {
  description = "Invoke this ARN to start the durable workflow"
  value       = aws_lambda_alias.live.arn
}

output "step1_function_arn" {
  value = aws_lambda_function.step1.arn
}

output "step2_function_arn" {
  value = aws_lambda_function.step2.arn
}

output "step3_function_arn" {
  value = aws_lambda_function.step3.arn
}