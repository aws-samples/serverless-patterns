terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.31.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.0"
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
# Inline Lambda Code → ZIP archives
# ──────────────────────────────────────────────

data "archive_file" "standard_lambda_zip" {
  type        = "zip"
  output_path = "${path.module}/standard_lambda_function.zip"

  source {
    content  = <<-PYTHON
import json
import logging
import os

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TABLE_NAME = os.environ["TABLE_NAME"]
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)

# The single partition key every tenant shares — the core of the problem.
SHARED_KEY = "SHARED"


def lambda_handler(event, context):
    """
    Standard Lambda handler WITHOUT tenant isolation.

    All tenants share a single DynamoDB row, so every call — regardless
    of which tenant makes it — increments the same counter.  This is the
    multi-tenant anti-pattern this demo exists to highlight.
    """
    try:
        if not isinstance(event, dict):
            return _error(400, "Bad Request", "Invalid request format")

        headers = event.get("headers", {}) or {}
        tenant_id_from_header = (
            headers.get("x-tenant-id")
            or headers.get("Tenant-Id")
            or headers.get("TENANT-ID")
        )

        logger.info(
            "Processing standard request — Method: %s, Path: %s, Tenant Header: %s",
            event.get("httpMethod", "UNKNOWN"),
            event.get("path", "UNKNOWN"),
            tenant_id_from_header,
        )

        http_method = event.get("httpMethod", "")
        if not http_method:
            return _error(400, "Bad Request", "Missing HTTP method in request")
        if http_method != "GET":
            return _error(
                405,
                "Method Not Allowed",
                f"HTTP method {http_method} is not supported. Only GET requests are allowed.",
            )

        # ── Atomic increment on the SHARED row ──────────────────────
        response = table.update_item(
            Key={"pk": SHARED_KEY},
            UpdateExpression="SET #c = if_not_exists(#c, :zero) + :inc",
            ExpressionAttributeNames={"#c": "counter"},
            ExpressionAttributeValues={":zero": 0, ":inc": 1},
            ReturnValues="UPDATED_NEW",
        )
        counter = int(response["Attributes"]["counter"])

        if tenant_id_from_header:
            logger.warning(
                "PROBLEM: Tenant '%s' is using SHARED counter value %d! "
                "This demonstrates data leakage between tenants.",
                tenant_id_from_header,
                counter,
            )
        else:
            logger.info("Request without tenant header — shared counter: %d", counter)

        body = {
            "counter": counter,
            "tenant_id": tenant_id_from_header,
            "isolation_enabled": False,
            "message": (
                f"This function does NOT provide tenant isolation and every tenant reads and writes the same DynamoDB row. Incremented counter is shared across all the tenants"
            ),
        }

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Cache-Control": "no-cache",
            },
            "body": json.dumps(body),
        }

    except ClientError as exc:
        logger.error("DynamoDB error: %s", exc.response["Error"]["Message"], exc_info=True)
        return _error(500, "Internal Server Error", "Database error while updating counter")
    except Exception:
        logger.error("Unexpected error processing request", exc_info=True)
        return _error(500, "Internal Server Error", "An unexpected error occurred")


def _error(status_code, error_type, message):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
        },
        "body": json.dumps(
            {"error": error_type, "message": message, "statusCode": status_code}
        ),
    }
    PYTHON
    filename = "standard_lambda_function.py"
  }
}

data "archive_file" "isolated_lambda_zip" {
  type        = "zip"
  output_path = "${path.module}/isolated_lambda_function.zip"

  source {
    content  = <<-PYTHON
import json
import logging
import os
import re

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TABLE_NAME = os.environ["TABLE_NAME"]
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)

# Simple allowlist for tenant IDs — alphanumeric, hyphens, underscores.
TENANT_ID_PATTERN = re.compile(r"^[\w\-]{1,100}$")


def lambda_handler(event, context):
    """
    Tenant-isolated Lambda handler.

    * The Lambda runtime guarantees a dedicated execution environment per
      tenant (`PER_TENANT` isolation mode).
    * Each tenant's counter is stored in its own DynamoDB row keyed by
      ``tenant_id``, so even at the data layer there is no sharing.
    """
    try:
        if not isinstance(event, dict):
            return _error(400, "Bad Request", "Invalid request format")

        logger.info(
            "Processing isolated request — Method: %s, Path: %s",
            event.get("httpMethod", "UNKNOWN"),
            event.get("path", "UNKNOWN"),
        )

        http_method = event.get("httpMethod", "")
        if not http_method:
            return _error(400, "Bad Request", "Missing HTTP method in request")
        if http_method != "GET":
            return _error(
                405,
                "Method Not Allowed",
                f"HTTP method {http_method} is not supported. Only GET requests are allowed.",
            )

        # ── Resolve tenant ID from Lambda context ───────────────────
        tenant_id = getattr(context, "tenant_id", None)

        if not tenant_id:
            logger.error("Missing tenant_id in Lambda context")
            return _error(
                400,
                "Missing Tenant ID",
                "Tenant ID is required. Ensure the x-tenant-id header is provided.",
            )

        tenant_id = tenant_id.strip()

        if not TENANT_ID_PATTERN.match(tenant_id):
            logger.error("Invalid tenant ID format: %s", tenant_id)
            return _error(
                400,
                "Invalid Tenant ID",
                "Tenant ID must be 1-100 alphanumeric, hyphen, or underscore characters.",
            )

        # ── Atomic per-tenant increment ─────────────────────────────
        response = table.update_item(
            Key={"tenant_id": tenant_id},
            UpdateExpression="SET #c = if_not_exists(#c, :zero) + :inc",
            ExpressionAttributeNames={"#c": "counter"},
            ExpressionAttributeValues={":zero": 0, ":inc": 1},
            ReturnValues="UPDATED_NEW",
        )
        counter = int(response["Attributes"]["counter"])

        logger.info("Tenant '%s' — isolated counter now at %d", tenant_id, counter)

        body = {
            "counter": counter,
            "tenant_id": tenant_id,
            "isolation_enabled": True,
            "message": f"Counter incremented for tenant {tenant_id}",
        }

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Cache-Control": "no-cache",
            },
            "body": json.dumps(body),
        }

    except ClientError as exc:
        logger.error("DynamoDB error: %s", exc.response["Error"]["Message"], exc_info=True)
        return _error(500, "Internal Server Error", "Database error while updating counter")
    except Exception:
        logger.error("Unexpected error processing isolated request", exc_info=True)
        return _error(500, "Internal Server Error", "An unexpected error occurred")


def _error(status_code, error_type, message):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
        },
        "body": json.dumps(
            {"error": error_type, "message": message, "statusCode": status_code}
        ),
    }
    PYTHON
    filename = "isolated_lambda_function.py"
  }
}

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
# IAM — Per-function roles with least-privilege DynamoDB access
# ──────────────────────────────────────────────

# ──────────────── Standard Lambda Role ────────────────

resource "aws_iam_role" "standard_lambda_execution_role" {
  name = "${local.name_prefix}-standard-lambda-role"

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

resource "aws_iam_role_policy_attachment" "standard_lambda_basic_execution" {
  role       = aws_iam_role.standard_lambda_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy" "standard_dynamodb_policy" {
  name = "${local.name_prefix}-standard-dynamodb"
  role = aws_iam_role.standard_lambda_execution_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowSharedTableOnly"
        Effect = "Allow"
        Action = [
          "dynamodb:GetItem",
          "dynamodb:PutItem",
          "dynamodb:UpdateItem"
        ]
        Resource = aws_dynamodb_table.shared_counter_table.arn
      }
    ]
  })
}

# ──────────────── Isolated Lambda Role ────────────────

resource "aws_iam_role" "isolated_lambda_execution_role" {
  name = "${local.name_prefix}-isolated-lambda-role"

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

resource "aws_iam_role_policy_attachment" "isolated_lambda_basic_execution" {
  role       = aws_iam_role.isolated_lambda_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy" "isolated_dynamodb_policy" {
  name = "${local.name_prefix}-isolated-dynamodb"
  role = aws_iam_role.isolated_lambda_execution_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowIsolatedTableOnly"
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
# Lambda Functions
# ──────────────────────────────────────────────

resource "aws_lambda_function" "counter_standard_function" {
  filename         = data.archive_file.standard_lambda_zip.output_path
  source_code_hash = data.archive_file.standard_lambda_zip.output_base64sha256
  function_name    = "${local.name_prefix}-counter-standard"
  role             = aws_iam_role.standard_lambda_execution_role.arn
  handler          = "standard_lambda_function.lambda_handler"
  runtime          = "python3.14"
  timeout          = 25
  memory_size      = 128
  description      = "[${var.prefix}] Lambda without tenant isolation — shared DynamoDB counter"

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
    aws_iam_role_policy_attachment.standard_lambda_basic_execution,
    aws_iam_role_policy.standard_dynamodb_policy
  ]
}

resource "aws_lambda_function" "counter_isolated_function" {
  filename         = data.archive_file.isolated_lambda_zip.output_path
  source_code_hash = data.archive_file.isolated_lambda_zip.output_base64sha256
  function_name    = "${local.name_prefix}-counter-isolated"
  role             = aws_iam_role.isolated_lambda_execution_role.arn
  handler          = "isolated_lambda_function.lambda_handler"
  runtime          = "python3.14"
  timeout          = 25
  memory_size      = 128
  description      = "[${var.prefix}] Lambda with tenant isolation — per-tenant DynamoDB counter"

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
    aws_iam_role_policy_attachment.isolated_lambda_basic_execution,
    aws_iam_role_policy.isolated_dynamodb_policy
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

output "dynamodb_shared_counter_table_name" {
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