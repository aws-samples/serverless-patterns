terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.80.0"
    }
  }
  required_version = ">= 1.0"
}

variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
}

variable "prefix" {
  description = "Prefix for resource names"
  type        = string
  default     = "durable-tenant"
}

provider "aws" {
  region = var.aws_region
}

data "aws_caller_identity" "current" {}

# --- IAM Role ---

resource "aws_iam_role" "lambda_role" {
  name = "${var.prefix}-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = "sts:AssumeRole"
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

resource "aws_iam_role_policy" "callback_policy" {
  name = "${var.prefix}-callback-policy"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "lambda:SendDurableExecutionCallbackSuccess",
        "lambda:SendDurableExecutionCallbackFailure",
        "lambda:SendDurableExecutionCallbackHeartbeat"
      ]
      Resource = "*"
    }]
  })
}

# --- Workflow Lambda ---

data "archive_file" "workflow_zip" {
  type        = "zip"
  source_dir  = "${path.module}/src/workflow"
  output_path = "${path.module}/build/workflow.zip"
}

resource "aws_lambda_function" "workflow" {
  function_name    = "${var.prefix}-workflow"
  filename         = data.archive_file.workflow_zip.output_path
  source_code_hash = data.archive_file.workflow_zip.output_base64sha256
  handler          = "workflow.handler"
  runtime          = "nodejs22.x"
  architectures    = ["arm64"]
  role             = aws_iam_role.lambda_role.arn
  timeout          = 900
  memory_size      = 256

  tenancy_config {
    tenant_isolation_mode = "PER_TENANT"
  }

  durable_config {
    execution_timeout = 86400
  }
}

resource "aws_lambda_alias" "workflow_live" {
  name             = "live"
  function_name    = aws_lambda_function.workflow.function_name
  function_version = aws_lambda_function.workflow.version
}

# --- Callback Lambda ---

data "archive_file" "callback_zip" {
  type        = "zip"
  source_dir  = "${path.module}/src/callback"
  output_path = "${path.module}/build/callback.zip"
}

resource "aws_lambda_function" "callback" {
  function_name    = "${var.prefix}-callback"
  filename         = data.archive_file.callback_zip.output_path
  source_code_hash = data.archive_file.callback_zip.output_base64sha256
  handler          = "callback.handler"
  runtime          = "nodejs22.x"
  architectures    = ["arm64"]
  role             = aws_iam_role.lambda_role.arn
  timeout          = 30
  memory_size      = 128
}

# --- API Gateway ---

resource "aws_api_gateway_rest_api" "api" {
  name = "${var.prefix}-api"

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

# /workflow resource (non-proxy, async invocation)
resource "aws_api_gateway_resource" "workflow" {
  rest_api_id = aws_api_gateway_rest_api.api.id
  parent_id   = aws_api_gateway_rest_api.api.root_resource_id
  path_part   = "workflow"
}

resource "aws_api_gateway_method" "workflow_post" {
  rest_api_id   = aws_api_gateway_rest_api.api.id
  resource_id   = aws_api_gateway_resource.workflow.id
  http_method   = "POST"
  authorization = "NONE"

  request_parameters = {
    "method.request.header.x-tenant-id" = true
  }
}

resource "aws_api_gateway_integration" "workflow_integration" {
  rest_api_id             = aws_api_gateway_rest_api.api.id
  resource_id             = aws_api_gateway_resource.workflow.id
  http_method             = aws_api_gateway_method.workflow_post.http_method
  integration_http_method = "POST"
  type                    = "AWS"
  uri                     = aws_lambda_alias.workflow_live.invoke_arn

  request_parameters = {
    "integration.request.header.X-Amz-Tenant-Id"       = "method.request.header.x-tenant-id"
    "integration.request.header.X-Amz-Invocation-Type" = "'Event'"
  }

  request_templates = {
    "application/json" = "$input.body"
  }
}

resource "aws_api_gateway_method_response" "workflow_202" {
  rest_api_id = aws_api_gateway_rest_api.api.id
  resource_id = aws_api_gateway_resource.workflow.id
  http_method = aws_api_gateway_method.workflow_post.http_method
  status_code = "202"
}

resource "aws_api_gateway_integration_response" "workflow_202" {
  rest_api_id = aws_api_gateway_rest_api.api.id
  resource_id = aws_api_gateway_resource.workflow.id
  http_method = aws_api_gateway_method.workflow_post.http_method
  status_code = aws_api_gateway_method_response.workflow_202.status_code

  response_templates = {
    "application/json" = "{\"message\": \"Workflow started\"}"
  }

  depends_on = [aws_api_gateway_integration.workflow_integration]
}

# /callback resource (proxy integration)
resource "aws_api_gateway_resource" "callback" {
  rest_api_id = aws_api_gateway_rest_api.api.id
  parent_id   = aws_api_gateway_rest_api.api.root_resource_id
  path_part   = "callback"
}

resource "aws_api_gateway_method" "callback_post" {
  rest_api_id   = aws_api_gateway_rest_api.api.id
  resource_id   = aws_api_gateway_resource.callback.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "callback_integration" {
  rest_api_id             = aws_api_gateway_rest_api.api.id
  resource_id             = aws_api_gateway_resource.callback.id
  http_method             = aws_api_gateway_method.callback_post.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.callback.invoke_arn
}

# Deploy
resource "aws_api_gateway_deployment" "deployment" {
  rest_api_id = aws_api_gateway_rest_api.api.id

  depends_on = [
    aws_api_gateway_integration.workflow_integration,
    aws_api_gateway_integration_response.workflow_202,
    aws_api_gateway_integration.callback_integration
  ]

  triggers = {
    redeployment = sha1(jsonencode([
      aws_api_gateway_integration.workflow_integration,
      aws_api_gateway_integration_response.workflow_202,
      aws_api_gateway_integration.callback_integration
    ]))
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_stage" "dev" {
  rest_api_id   = aws_api_gateway_rest_api.api.id
  deployment_id = aws_api_gateway_deployment.deployment.id
  stage_name    = "dev"
}

# Lambda permissions for API Gateway
resource "aws_lambda_permission" "workflow_apigw" {
  statement_id  = "AllowAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.workflow.function_name
  qualifier     = aws_lambda_alias.workflow_live.name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.api.execution_arn}/*"
}

resource "aws_lambda_permission" "callback_apigw" {
  statement_id  = "AllowAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.callback.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.api.execution_arn}/*"
}

# --- Outputs ---

output "workflow_endpoint" {
  description = "POST to start a workflow (include x-tenant-id header)"
  value       = "https://${aws_api_gateway_rest_api.api.id}.execute-api.${var.aws_region}.amazonaws.com/dev/workflow"
}

output "callback_endpoint" {
  description = "POST to send a callback (include callbackId and payload in body)"
  value       = "https://${aws_api_gateway_rest_api.api.id}.execute-api.${var.aws_region}.amazonaws.com/dev/callback"
}
