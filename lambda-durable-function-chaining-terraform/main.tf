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
# IAM Role for All Lambda Functions
############################################################

resource "aws_iam_role" "lambda_role" {
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

resource "aws_iam_role_policy_attachment" "basic_execution" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy_attachment" "durable_execution" {
  role       = aws_iam_role.lambda_role.name
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
# Scoped CloudWatch Logs Write Policy
############################################################

resource "aws_iam_role_policy" "lambda_logging" {
  name = "${var.prefix}-lambda-cloudwatch-logging"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ]
      Resource = [
        "${aws_cloudwatch_log_group.step1.arn}:*",
        "${aws_cloudwatch_log_group.step2.arn}:*",
        "${aws_cloudwatch_log_group.step3.arn}:*",
        "${aws_cloudwatch_log_group.orchestrator.arn}:*"
      ]
    }]
  })
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
  role          = aws_iam_role.lambda_role.arn

  logging_config {
    log_group  = aws_cloudwatch_log_group.step1.name
    log_format = "Text"
  }

  depends_on = [
    aws_cloudwatch_log_group.step1,
    aws_iam_role_policy.lambda_logging
  ]
}

resource "aws_lambda_function" "step2" {
  function_name = "${var.prefix}-step2-transform"
  filename      = "step2_transform.zip"
  handler       = "step2_transform.lambda_handler"
  runtime       = "python3.14"
  memory_size   = 512
  timeout       = 30
  role          = aws_iam_role.lambda_role.arn

  logging_config {
    log_group  = aws_cloudwatch_log_group.step2.name
    log_format = "Text"
  }

  depends_on = [
    aws_cloudwatch_log_group.step2,
    aws_iam_role_policy.lambda_logging
  ]
}

resource "aws_lambda_function" "step3" {
  function_name = "${var.prefix}-step3-finalize"
  filename      = "step3_finalize.zip"
  handler       = "step3_finalize.lambda_handler"
  runtime       = "python3.14"
  memory_size   = 512
  timeout       = 30
  role          = aws_iam_role.lambda_role.arn

  logging_config {
    log_group  = aws_cloudwatch_log_group.step3.name
    log_format = "Text"
  }

  depends_on = [
    aws_cloudwatch_log_group.step3,
    aws_iam_role_policy.lambda_logging
  ]
}

############################################################
# Allow Orchestrator to Invoke Worker Functions
############################################################

resource "aws_iam_role_policy" "invoke_workers" {
  name = "${var.prefix}-invoke-worker-functions"
  role = aws_iam_role.lambda_role.id

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
# Durable Orchestrator Function
############################################################

resource "aws_lambda_function" "orchestrator" {
  function_name = "${var.prefix}-durable-orchestrator"
  filename      = "orchestrator.zip"
  handler       = "orchestrator.lambda_handler"
  runtime       = "python3.14"
  memory_size   = 512
  timeout       = 90
  role          = aws_iam_role.lambda_role.arn
  publish       = true

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
    aws_cloudwatch_log_group.orchestrator,
    aws_iam_role_policy.lambda_logging
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