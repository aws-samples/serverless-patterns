variable "region" {}

provider "aws" {
  region = var.region
}

variable "prefix" {
  description = "Prefix to associate with the resources"
  type        = string
}

#========================================================================
// S3 setup
#========================================================================
resource "aws_s3_bucket" "upload_bucket" {
  bucket = "${lower(var.prefix)}-s3-upload"
}

resource "aws_s3_bucket_public_access_block" "upload_bucket" {
  bucket = aws_s3_bucket.upload_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "upload_bucket" {
  bucket = aws_s3_bucket.upload_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "AES256"
    }
  }
}


resource "aws_s3_bucket_versioning" "upload_bucket" {
  bucket = aws_s3_bucket.upload_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

#========================================================================
// IAM Policies setup
#========================================================================
resource "aws_iam_role" "lambda_role" {
  name = "${lower(var.prefix)}-lambda-execution-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}
resource "aws_iam_role_policy" "lambda_policy" {
  name   = "${lower(var.prefix)}-lambda-policy"
  role   = aws_iam_role.lambda_role.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        Resource = "*"
      },
      {
        Effect = "Allow",
        Action = [
          "s3:PutObject",
          "s3:GetObject",
          "s3:ListBucket"
        ],
        Resource = [
          aws_s3_bucket.upload_bucket.arn,
          "${aws_s3_bucket.upload_bucket.arn}/*"
        ]
      }
    ]
  })
}

#========================================================================
// API Gateway setup
#========================================================================

resource "aws_api_gateway_rest_api" "api" {
  name        = "${lower(var.prefix)}-presigned-url-api"
  description = "API for generating presigned URLs"
}
resource "aws_api_gateway_resource" "resource" {
  rest_api_id = aws_api_gateway_rest_api.api.id
  parent_id   = aws_api_gateway_rest_api.api.root_resource_id
  path_part   = "invoke"
}
resource "aws_api_gateway_method" "method" {
  rest_api_id   = aws_api_gateway_rest_api.api.id
  resource_id   = aws_api_gateway_resource.resource.id
  http_method   = "POST"
  authorization = "NONE"
}
resource "aws_api_gateway_integration" "integration" {
  rest_api_id             = aws_api_gateway_rest_api.api.id
  resource_id             = aws_api_gateway_resource.resource.id
  http_method             = aws_api_gateway_method.method.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = "arn:aws:apigateway:${var.region}:lambda:path/2015-03-31/functions/${aws_lambda_function.generate_presigned_url.arn}/invocations"
}
resource "aws_lambda_permission" "allow_api_gateway" {
  statement_id  = "${lower(var.prefix)}-allow-api-gateway-invoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.generate_presigned_url.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.api.execution_arn}/*/*"
}
resource "aws_api_gateway_deployment" "deployment" {
  depends_on  = [aws_api_gateway_integration.integration]
  rest_api_id = aws_api_gateway_rest_api.api.id
  stage_name  = "dev"
}


#========================================================================
// Lambda setup
#========================================================================

resource "aws_lambda_function" "generate_presigned_url" {
  filename      = "target/MyS3PreSignedURLGeneratorFunction.zip"
  function_name = "${lower(var.prefix)}-generate-presigned-url"
  role          =  aws_iam_role.lambda_role.arn
  handler       = "com.example.MyS3PreSignedURLGeneratorFunction::handleRequest"
  runtime       = "java21"
  memory_size   = 1024
  timeout       = 30
  environment {
    variables = {
      BUCKET_NAME = aws_s3_bucket.upload_bucket.bucket
    }
  }
}

#========================================================================
// Outputs
#========================================================================

output "api_url" {
  description = "The URL of the API Gateway REST API"
  value       = "https://${aws_api_gateway_rest_api.api.id}.execute-api.${var.region}.amazonaws.com/dev/invoke"
}
