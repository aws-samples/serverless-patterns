terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.31.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# ──────────────────────────────────────────────
# Variables — Terraform will prompt for prefix and region
# ──────────────────────────────────────────────

variable "aws_region" {
  description = "AWS region for resources (e.g. us-east-1, us-west-2)"
  type        = string

  validation {
    condition     = can(regex("^[a-z]{2}-[a-z]+-[0-9]+$", var.aws_region))
    error_message = "Must be a valid AWS region (e.g. us-east-1, eu-west-2)."
  }
}

variable "prefix" {
  description = "Unique prefix for all resource names — avoids collisions (e.g. your initials or team name)"
  type        = string

  validation {
    condition     = can(regex("^[a-z0-9][a-z0-9\\-]{1,20}$", var.prefix))
    error_message = "Prefix must be 2-21 lowercase alphanumeric characters or hyphens, starting with a letter or number."
  }
}

variable "environment" {
  description = "Environment name for resource naming"
  type        = string
  default     = "dev"
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "log_retention_days" {
  description = "CloudWatch log retention in days (0 = never expire)"
  type        = number
  default     = 14
}

# ──────────────────────────────────────────────
# Locals — single place that builds the name prefix
# ──────────────────────────────────────────────

locals {
  name_prefix = "${var.prefix}-tenant-iso"
}

# Data sources
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

# ──────────────────────────────────────────────
# DynamoDB Tables
# ──────────────────────────────────────────────

resource "aws_dynamodb_table" "shared_counter_table" {
  name         = "${local.name_prefix}-shared-counters"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "pk"

  attribute {
    name = "pk"
    type = "S"
  }

  tags = {
    Environment = var.environment
    Prefix      = var.prefix
    Purpose     = "Shared counter - demonstrates lack of tenant isolation"
  }
}

resource "aws_dynamodb_table" "isolated_counter_table" {
  name         = "${local.name_prefix}-isolated-counters"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "tenant_id"

  attribute {
    name = "tenant_id"
    type = "S"
  }

  tags = {
    Environment = var.environment
    Prefix      = var.prefix
    Purpose     = "Per-tenant counters with tenant isolation"
  }
}

# ──────────────────────────────────────────────
# IAM
# ──────────────────────────────────────────────

resource "aws_iam_role" "lambda_execution_role" {
  name = "${local.name_prefix}-lambda-role"

  force_detach_policies = true

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })

  tags = {
    Environment = var.environment
    Prefix      = var.prefix
  }
}

resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role       = aws_iam_role.lambda_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# ──────────────────────────────────────────────
# CloudWatch Log Groups (Terraform-managed, destroyed on terraform destroy)
# ──────────────────────────────────────────────

resource "aws_cloudwatch_log_group" "counter_standard_log_group" {
  name              = "/aws/lambda/${local.name_prefix}-counter-standard"
  retention_in_days = var.log_retention_days
  skip_destroy      = false

  tags = {
    Environment = var.environment
    Prefix      = var.prefix
  }
}

resource "aws_cloudwatch_log_group" "counter_isolated_log_group" {
  name              = "/aws/lambda/${local.name_prefix}-counter-isolated"
  retention_in_days = var.log_retention_days
  skip_destroy      = false

  tags = {
    Environment = var.environment
    Prefix      = var.prefix
  }
}

# ──────────────────────────────────────────────
# Scoped CloudWatch Logs Write Policy
# ──────────────────────────────────────────────

resource "aws_iam_role_policy" "cloudwatch_logs_policy" {
  name = "${local.name_prefix}-cw-logs"
  role = aws_iam_role.lambda_execution_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = [
          "${aws_cloudwatch_log_group.counter_standard_log_group.arn}:*",
          "${aws_cloudwatch_log_group.counter_isolated_log_group.arn}:*"
        ]
      }
    ]
  })
}

resource "aws_iam_role_policy" "dynamodb_policy" {
  name = "${local.name_prefix}-dynamodb"
  role = aws_iam_role.lambda_execution_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowSharedTable"
        Effect = "Allow"
        Action = [
          "dynamodb:GetItem",
          "dynamodb:PutItem",
          "dynamodb:UpdateItem"
        ]
        Resource = aws_dynamodb_table.shared_counter_table.arn
      },
      {
        Sid    = "AllowIsolatedTable"
        Effect = "Allow"
        Action = [
          "dynamodb:GetItem",
          "dynamodb:PutItem",
          "dynamodb:UpdateItem"
        ]
        Resource = aws_dynamodb_table.isolated_counter_table.arn
      }
    ]
  })
}

# ──────────────────────────────────────────────
# Lambda Functions
# ──────────────────────────────────────────────

resource "aws_lambda_function" "counter_standard_function" {
  filename      = "standard_lambda_function.zip"
  function_name = "${local.name_prefix}-counter-standard"
  role          = aws_iam_role.lambda_execution_role.arn
  handler       = "standard_lambda_function.lambda_handler"
  runtime       = "python3.14"
  timeout       = 30
  memory_size   = 128
  description   = "[${var.prefix}] Lambda without tenant isolation — shared DynamoDB counter"

  logging_config {
    log_group  = aws_cloudwatch_log_group.counter_standard_log_group.name
    log_format = "Text"
  }

  environment {
    variables = {
      LOG_LEVEL  = "INFO"
      TABLE_NAME = aws_dynamodb_table.shared_counter_table.name
    }
  }

  tags = {
    Environment = var.environment
    Prefix      = var.prefix
  }

  depends_on = [
    aws_cloudwatch_log_group.counter_standard_log_group,
    aws_iam_role_policy_attachment.lambda_basic_execution,
    aws_iam_role_policy.cloudwatch_logs_policy,
    aws_iam_role_policy.dynamodb_policy
  ]
}

resource "aws_lambda_function" "counter_isolated_function" {
  filename      = "isolated_lambda_function.zip"
  function_name = "${local.name_prefix}-counter-isolated"
  role          = aws_iam_role.lambda_execution_role.arn
  handler       = "isolated_lambda_function.lambda_handler"
  runtime       = "python3.14"
  timeout       = 30
  memory_size   = 128
  description   = "[${var.prefix}] Lambda with tenant isolation — per-tenant DynamoDB counter"

  tenancy_config {
    tenant_isolation_mode = "PER_TENANT"
  }

  logging_config {
    log_group  = aws_cloudwatch_log_group.counter_isolated_log_group.name
    log_format = "Text"
  }

  environment {
    variables = {
      LOG_LEVEL  = "INFO"
      TABLE_NAME = aws_dynamodb_table.isolated_counter_table.name
    }
  }

  tags = {
    Environment = var.environment
    Prefix      = var.prefix
  }

  depends_on = [
    aws_cloudwatch_log_group.counter_isolated_log_group,
    aws_iam_role_policy_attachment.lambda_basic_execution,
    aws_iam_role_policy.cloudwatch_logs_policy,
    aws_iam_role_policy.dynamodb_policy
  ]
}

# ──────────────────────────────────────────────
# API Gateway REST API
# ──────────────────────────────────────────────

resource "aws_api_gateway_rest_api" "api_gateway" {
  name        = "${local.name_prefix}-api"
  description = "[${var.prefix}] API Gateway for Lambda tenant isolation demonstration"

  endpoint_configuration {
    types = ["REGIONAL"]
  }

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = "*"
        Action    = "execute-api:Invoke"
        Resource  = "*"
      }
    ]
  })

  tags = {
    Environment = var.environment
    Prefix      = var.prefix
  }
}

# Request Validator
resource "aws_api_gateway_request_validator" "request_validator" {
  name                        = "${local.name_prefix}-request-validator"
  rest_api_id                 = aws_api_gateway_rest_api.api_gateway.id
  validate_request_parameters = true
  validate_request_body       = false
}

# Error Model
resource "aws_api_gateway_model" "error_model" {
  rest_api_id  = aws_api_gateway_rest_api.api_gateway.id
  name         = "ErrorModel"
  content_type = "application/json"

  schema = jsonencode({
    "$schema" = "http://json-schema.org/draft-04/schema#"
    title     = "Error Schema"
    type      = "object"
    properties = {
      error = {
        type = "string"
      }
      message = {
        type = "string"
      }
      statusCode = {
        type = "integer"
      }
    }
  })
}

# ──────────────── Standard endpoint ────────────────

resource "aws_api_gateway_resource" "standard_resource" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  parent_id   = aws_api_gateway_rest_api.api_gateway.root_resource_id
  path_part   = "standard"
}

resource "aws_api_gateway_method" "standard_method" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.standard_resource.id
  http_method   = "GET"
  authorization = "NONE"

  request_parameters = {
    "method.request.header.tenant-id" = false
  }
}

resource "aws_api_gateway_integration" "standard_integration" {
  rest_api_id             = aws_api_gateway_rest_api.api_gateway.id
  resource_id             = aws_api_gateway_resource.standard_resource.id
  http_method             = aws_api_gateway_method.standard_method.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.counter_standard_function.invoke_arn

  request_parameters = {
    "integration.request.header.X-Amz-Tenant-Id" = "method.request.header.tenant-id"
  }
}

resource "aws_api_gateway_method_response" "standard_response_200" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.standard_resource.id
  http_method = aws_api_gateway_method.standard_method.http_method
  status_code = "200"

  response_models = {
    "application/json" = "Empty"
  }
}

resource "aws_api_gateway_method_response" "standard_response_405" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.standard_resource.id
  http_method = aws_api_gateway_method.standard_method.http_method
  status_code = "405"

  response_models = {
    "application/json" = aws_api_gateway_model.error_model.name
  }
}

resource "aws_api_gateway_method_response" "standard_response_500" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.standard_resource.id
  http_method = aws_api_gateway_method.standard_method.http_method
  status_code = "500"

  response_models = {
    "application/json" = aws_api_gateway_model.error_model.name
  }
}

# Standard OPTIONS (CORS)
resource "aws_api_gateway_method" "standard_options_method" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.standard_resource.id
  http_method   = "OPTIONS"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "standard_options_integration" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.standard_resource.id
  http_method = aws_api_gateway_method.standard_options_method.http_method
  type        = "MOCK"

  request_templates = {
    "application/json" = "{\"statusCode\": 200}"
  }
}

resource "aws_api_gateway_method_response" "standard_options_response_200" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.standard_resource.id
  http_method = aws_api_gateway_method.standard_options_method.http_method
  status_code = "200"

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = true
    "method.response.header.Access-Control-Allow-Methods" = true
    "method.response.header.Access-Control-Allow-Origin"  = true
  }
}

resource "aws_api_gateway_integration_response" "standard_options_integration_response" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.standard_resource.id
  http_method = aws_api_gateway_method.standard_options_method.http_method
  status_code = aws_api_gateway_method_response.standard_options_response_200.status_code

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'"
    "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS'"
    "method.response.header.Access-Control-Allow-Origin"  = "'*'"
  }

  response_templates = {
    "application/json" = ""
  }
}

# ──────────────── Isolated endpoint ────────────────

resource "aws_api_gateway_resource" "isolated_resource" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  parent_id   = aws_api_gateway_rest_api.api_gateway.root_resource_id
  path_part   = "isolated"
}

resource "aws_api_gateway_method" "isolated_method" {
  rest_api_id          = aws_api_gateway_rest_api.api_gateway.id
  resource_id          = aws_api_gateway_resource.isolated_resource.id
  http_method          = "GET"
  authorization        = "NONE"
  request_validator_id = aws_api_gateway_request_validator.request_validator.id

  request_parameters = {
    "method.request.header.x-tenant-id" = true
  }
}

resource "aws_api_gateway_integration" "isolated_integration" {
  rest_api_id             = aws_api_gateway_rest_api.api_gateway.id
  resource_id             = aws_api_gateway_resource.isolated_resource.id
  http_method             = aws_api_gateway_method.isolated_method.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.counter_isolated_function.invoke_arn

  request_parameters = {
    "integration.request.header.X-Amz-Tenant-Id" = "method.request.header.x-tenant-id"
  }
}

resource "aws_api_gateway_method_response" "isolated_response_200" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.isolated_resource.id
  http_method = aws_api_gateway_method.isolated_method.http_method
  status_code = "200"

  response_models = {
    "application/json" = "Empty"
  }
}

resource "aws_api_gateway_method_response" "isolated_response_400" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.isolated_resource.id
  http_method = aws_api_gateway_method.isolated_method.http_method
  status_code = "400"

  response_models = {
    "application/json" = aws_api_gateway_model.error_model.name
  }
}

resource "aws_api_gateway_method_response" "isolated_response_405" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.isolated_resource.id
  http_method = aws_api_gateway_method.isolated_method.http_method
  status_code = "405"

  response_models = {
    "application/json" = aws_api_gateway_model.error_model.name
  }
}

resource "aws_api_gateway_method_response" "isolated_response_500" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.isolated_resource.id
  http_method = aws_api_gateway_method.isolated_method.http_method
  status_code = "500"

  response_models = {
    "application/json" = aws_api_gateway_model.error_model.name
  }
}

# Isolated OPTIONS (CORS)
resource "aws_api_gateway_method" "isolated_options_method" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.isolated_resource.id
  http_method   = "OPTIONS"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "isolated_options_integration" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.isolated_resource.id
  http_method = aws_api_gateway_method.isolated_options_method.http_method
  type        = "MOCK"

  request_templates = {
    "application/json" = "{\"statusCode\": 200}"
  }
}

resource "aws_api_gateway_method_response" "isolated_options_response_200" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.isolated_resource.id
  http_method = aws_api_gateway_method.isolated_options_method.http_method
  status_code = "200"

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = true
    "method.response.header.Access-Control-Allow-Methods" = true
    "method.response.header.Access-Control-Allow-Origin"  = true
  }
}

resource "aws_api_gateway_integration_response" "isolated_options_integration_response" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.isolated_resource.id
  http_method = aws_api_gateway_method.isolated_options_method.http_method
  status_code = aws_api_gateway_method_response.isolated_options_response_200.status_code

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,x-tenant-id'"
    "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS'"
    "method.response.header.Access-Control-Allow-Origin"  = "'*'"
  }

  response_templates = {
    "application/json" = ""
  }
}

# ──────────────────────────────────────────────
# Lambda Permissions for API Gateway
# ──────────────────────────────────────────────

resource "aws_lambda_permission" "standard_function_permission" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.counter_standard_function.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.api_gateway.execution_arn}/*/*"
}

resource "aws_lambda_permission" "isolated_function_permission" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.counter_isolated_function.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.api_gateway.execution_arn}/*/*"
}

# ──────────────────────────────────────────────
# API Gateway Deployment & Stage
# ──────────────────────────────────────────────

resource "aws_api_gateway_deployment" "api_gateway_deployment" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id

  triggers = {
    redeployment = sha1(jsonencode([
      aws_api_gateway_resource.standard_resource.id,
      aws_api_gateway_method.standard_method.id,
      aws_api_gateway_integration.standard_integration.id,
      aws_api_gateway_resource.isolated_resource.id,
      aws_api_gateway_method.isolated_method.id,
      aws_api_gateway_integration.isolated_integration.id,
    ]))
  }

  lifecycle {
    create_before_destroy = true
  }

  depends_on = [
    aws_api_gateway_method.standard_method,
    aws_api_gateway_integration.standard_integration,
    aws_api_gateway_method.standard_options_method,
    aws_api_gateway_integration.standard_options_integration,
    aws_api_gateway_method.isolated_method,
    aws_api_gateway_integration.isolated_integration,
    aws_api_gateway_method.isolated_options_method,
    aws_api_gateway_integration.isolated_options_integration,
  ]
}

resource "aws_api_gateway_stage" "api_gateway_stage" {
  deployment_id = aws_api_gateway_deployment.api_gateway_deployment.id
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  stage_name    = var.environment
  description   = "[${var.prefix}] Stage for ${var.environment} environment"

  tags = {
    Environment = var.environment
    Prefix      = var.prefix
  }
}

# ──────────────────────────────────────────────
# Outputs
# ──────────────────────────────────────────────

output "prefix_used" {
  description = "The prefix used for all resources"
  value       = var.prefix
}

output "standard_lambda_function_name" {
  description = "Standard Lambda function name"
  value       = aws_lambda_function.counter_standard_function.function_name
}

output "isolated_lambda_function_name" {
  description = "Isolated Lambda function name"
  value       = aws_lambda_function.counter_isolated_function.function_name
}

output "dyanamodb_shared_counter_table_name" {
  description = "DynamoDB table for shared counters"
  value       = aws_dynamodb_table.shared_counter_table.name
}

output "dynamodb_isolated_counter_table_name" {
  description = "DynamoDB table for isolated per-tenant counters"
  value       = aws_dynamodb_table.isolated_counter_table.name
}

output "api_gateway_id" {
  description = "API Gateway REST API ID"
  value       = aws_api_gateway_rest_api.api_gateway.id
}

output "standard_multi_tenant_api_endpoint_url" {
  description = "URL for the standard Lambda function endpoint"
  value       = "${aws_api_gateway_stage.api_gateway_stage.invoke_url}/standard"
}

output "isolated_tenant_api_endpoint_url" {
  description = "URL for the tenant-isolated Lambda function endpoint"
  value       = "${aws_api_gateway_stage.api_gateway_stage.invoke_url}/isolated"
}