# Provider configuration
provider "aws" {
  region = "us-east-1"  # Change this to your desired region
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.0"
    }
    null = {
      source  = "hashicorp/null"
      version = "~> 3.0"
    }
  }
}

# Archive the Lambda function code
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "${path.module}/src"
  output_path = "${path.module}/lambda.zip"
}

# API Gateway REST API
resource "aws_api_gateway_rest_api" "main_api" {
  name = "validation-api"
  description = "API Gateway with data validation"

  body = jsonencode({
    openapi = "3.0.1"
    info = {
      title = "validation-api"
      version = "1.0"
    }
    components = {
      schemas = {
        Vehicle = {
          type = "object"
          required = ["make", "model", "year"]
          properties = {
            make = {
              type = "string"
            }
            model = {
              type = "string"
            }
            year = {
              type = "integer"
              minimum = 2010
            }
            color = {
              type = "string"
              enum = ["green", "red", "blue"]
            }
          }
        }
      }
    }
  })
}

# Lambda Function
resource "aws_lambda_function" "process_function" {
  filename         = data.archive_file.lambda_zip.output_path
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  function_name    = "process-function"
  role            = aws_iam_role.lambda_role.arn
  handler         = "app.lambda_handler"
  runtime         = "python3.13"
  architectures   = ["arm64"]
  timeout         = 3

  depends_on = [
    data.archive_file.lambda_zip
  ]
}

# IAM Role for Lambda
resource "aws_iam_role" "lambda_role" {
  name = "process_function_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# Basic Lambda execution policy
resource "aws_iam_role_policy_attachment" "lambda_basic" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = aws_iam_role.lambda_role.name
}

# API Gateway Resource
resource "aws_api_gateway_resource" "api_resource" {
  rest_api_id = aws_api_gateway_rest_api.main_api.id
  parent_id   = aws_api_gateway_rest_api.main_api.root_resource_id
  path_part   = "{id}"
}

# API Gateway Method
resource "aws_api_gateway_method" "api_method" {
  rest_api_id   = aws_api_gateway_rest_api.main_api.id
  resource_id   = aws_api_gateway_resource.api_resource.id
  http_method   = "POST"
  authorization = "NONE"

  request_parameters = {
    "method.request.querystring.order" = true
    "method.request.header.custom-agent" = true
  }

  request_validator_id = aws_api_gateway_request_validator.validator.id
  request_models = {
    "application/json" = aws_api_gateway_model.vehicle_model.name
  }
}

# Request Validator
resource "aws_api_gateway_request_validator" "validator" {
  name                        = "validator"
  rest_api_id                = aws_api_gateway_rest_api.main_api.id
  validate_request_body      = true
  validate_request_parameters = true
}

# Vehicle Model
resource "aws_api_gateway_model" "vehicle_model" {
  rest_api_id  = aws_api_gateway_rest_api.main_api.id
  name         = "Vehicle"
  description  = "Vehicle model for validation"
  content_type = "application/json"

  schema = jsonencode({
    type = "object"
    required = ["make", "model", "year"]
    properties = {
      make = {
        type = "string"
      }
      model = {
        type = "string"
      }
      year = {
        type = "integer"
        minimum = 2010
      }
      color = {
        type = "string"
        enum = ["green", "red", "blue"]
      }
    }
  })
}

# Lambda Integration
resource "aws_api_gateway_integration" "lambda_integration" {
  rest_api_id = aws_api_gateway_rest_api.main_api.id
  resource_id = aws_api_gateway_resource.api_resource.id
  http_method = aws_api_gateway_method.api_method.http_method
  type        = "AWS_PROXY"
  integration_http_method = "POST"
  uri         = aws_lambda_function.process_function.invoke_arn
}

# Lambda Permission
resource "aws_lambda_permission" "api_gateway" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.process_function.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.main_api.execution_arn}/*/*/*"
}

# API Gateway Deployment
resource "aws_api_gateway_deployment" "api_deployment" {
  rest_api_id = aws_api_gateway_rest_api.main_api.id
  depends_on  = [aws_api_gateway_integration.lambda_integration]
}

# API Gateway Stage
resource "aws_api_gateway_stage" "prod" {
  deployment_id = aws_api_gateway_deployment.api_deployment.id
  rest_api_id   = aws_api_gateway_rest_api.main_api.id
  stage_name    = "Prod"
}

# Output
output "api_endpoint" {
  description = "API Gateway endpoint URL for Prod stage"
  value       = "${aws_api_gateway_stage.prod.invoke_url}"
}
