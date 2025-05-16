provider "aws" {
  region = "us-east-1"
}

variable "prefix" {
  description = "Prefix to associate with the resources"
  type        = string
}

resource "random_string" "suffix" {
  length  = 8
  special = false
  upper   = false
}

# Create Lambda layer for Pillow from provided zip file
resource "aws_lambda_layer_version" "pillow_layer" {
  filename            = "pillow.zip"  # Make sure this zip file exists in your terraform directory
  layer_name         = "pillow_layer"
  compatible_runtimes = ["python3.11"]
  description        = "Pillow library layer for image processing"
}

# IAM Policy for invoking Bedrock model
resource "aws_iam_policy" "invoke_model_policy" {
  name        = "${lower(var.prefix)}-InvokeModelPolicy-${random_string.suffix.result}"
  path        = "/"
  description = "Policy to invoke Bedrock model"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "bedrock:InvokeModel",
        ]
        Effect = "Allow"
        Resource = [
          "arn:aws:bedrock:${data.aws_region.current.name}::foundation-model/amazon.nova-canvas-v1:0"
        ]
      },
    ]
  })
}

# S3 bucket for storing images
resource "aws_s3_bucket" "image_bucket" {
  bucket = "${lower(var.prefix)}-image-bucket-${random_string.suffix.result}"
  force_destroy = true
}

# Create CloudWatch Log Group for Lambda
resource "aws_cloudwatch_log_group" "lambda_log_group" {
  name              = "/aws/lambda/${lower(var.prefix)}-invoke-bedrock"
  retention_in_days = 14
  
  lifecycle {
    prevent_destroy = false
  }
}

# Lambda function
resource "aws_lambda_function" "invoke_bedrock_function" {
  filename      = "index.zip"  # Replace with your Lambda code zip file
  function_name = "${lower(var.prefix)}-invoke-bedrock"
  role          = aws_iam_role.lambda_role.arn
  handler       = "index.handler"
  runtime       = "python3.11"
  timeout       = 30

  layers = [
    aws_lambda_layer_version.pillow_layer.arn
  ]

  environment {
    variables = {
      BUCKET = aws_s3_bucket.image_bucket.id
    }
  }

  depends_on = [aws_cloudwatch_log_group.lambda_log_group]
}

# IAM role for Lambda function
resource "aws_iam_role" "lambda_role" {
  name = "${lower(var.prefix)}-lambda_role-${random_string.suffix.result}"

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

# Attach policies to Lambda role
resource "aws_iam_role_policy_attachment" "lambda_invoke_model_policy" {
  policy_arn = aws_iam_policy.invoke_model_policy.arn
  role       = aws_iam_role.lambda_role.name
}

resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = aws_iam_role.lambda_role.name
}

resource "aws_iam_role_policy_attachment" "lambda_s3_access" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
  role       = aws_iam_role.lambda_role.name
}

# API Gateway
resource "aws_api_gateway_rest_api" "bedrock_api" {
  name = "${lower(var.prefix)}-BedrockImageAPI-${random_string.suffix.result}"
}

resource "aws_api_gateway_resource" "image_gen" {
  rest_api_id = aws_api_gateway_rest_api.bedrock_api.id
  parent_id   = aws_api_gateway_rest_api.bedrock_api.root_resource_id
  path_part   = "image_gen"
}

resource "aws_api_gateway_method" "image_gen_post" {
  rest_api_id   = aws_api_gateway_rest_api.bedrock_api.id
  resource_id   = aws_api_gateway_resource.image_gen.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "lambda_integration" {
  rest_api_id = aws_api_gateway_rest_api.bedrock_api.id
  resource_id = aws_api_gateway_resource.image_gen.id
  http_method = aws_api_gateway_method.image_gen_post.http_method

  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.invoke_bedrock_function.invoke_arn
}

# API Gateway Deployment
resource "aws_api_gateway_deployment" "api_deployment" {
  rest_api_id = aws_api_gateway_rest_api.bedrock_api.id
  
  depends_on = [
    aws_api_gateway_integration.lambda_integration
  ]
}

# API Gateway Stage
resource "aws_api_gateway_stage" "api_stage" {
  deployment_id = aws_api_gateway_deployment.api_deployment.id
  rest_api_id   = aws_api_gateway_rest_api.bedrock_api.id
  stage_name    = "dev"
}

# Lambda permission for API Gateway
resource "aws_lambda_permission" "api_gateway_lambda" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.invoke_bedrock_function.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.bedrock_api.execution_arn}/*/*"
}

# Outputs
output "lambda_function" {
  description = "The ARN of the Lambda function"
  value       = aws_lambda_function.invoke_bedrock_function.arn
}

output "api_endpoint" {
  description = "The API Gateway endpoint URL "
  value = "${aws_api_gateway_stage.api_stage.invoke_url}/image_gen"
}

output "s3_image_bucket" {
  description = "The Output S3 bucket is "
  value = aws_s3_bucket.image_bucket.id
}

# Data source for current region
data "aws_region" "current" {}
