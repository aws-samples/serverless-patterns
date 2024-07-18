variable "region" {}
provider "aws" {
  region = var.region
}
variable "prefix" {
  description = "Prefix to associate with the resources"
  type        = string
}
resource "aws_s3_bucket" "upload_bucket" {
  bucket = "${lower(var.prefix)}-s3-upload"
}
resource "aws_sns_topic" "sns_topic" {
  name = "${lower(var.prefix)}-sns-topic"
}
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
      },
      {
        Effect = "Allow",
        Action = "sns:Publish",
        Resource = aws_sns_topic.sns_topic.arn
      },
      {
        Effect = "Allow",
        Action = "rekognition:DetectModerationLabels",
        Resource = "*"
      }
    ]
  })
}
resource "aws_cloudwatch_log_group" "lambda_log_group" {
  count = 2
  name = "/aws/lambda/${lower(var.prefix)}-${element(["generate-presigned-url", "process-s3-event"], count.index)}"
  retention_in_days = 14
}
resource "aws_lambda_function" "generate_presigned_url" {
  filename      = "generate_presigned_url.zip"
  function_name = "${lower(var.prefix)}-generate-presigned-url"
  role          = aws_iam_role.lambda_role.arn
  handler       = "generate_presigned_url.lambda_handler"
  runtime       = "python3.12"
  timeout       = 30
  environment {
    variables = {
      BUCKET_NAME = aws_s3_bucket.upload_bucket.bucket
    }
  }
}
resource "aws_lambda_function" "process_s3_event" {
  filename      = "process_s3_event.zip"
  function_name = "${lower(var.prefix)}-process-s3-event"
  role          = aws_iam_role.lambda_role.arn
  handler       = "process_s3_event.lambda_handler"
  runtime       = "python3.12"
  timeout       = 60
  environment {
    variables = {
      SNS_TOPIC_ARN = aws_sns_topic.sns_topic.arn
    }
  }
}
resource "aws_s3_bucket_notification" "s3_bucket_notification" {
  bucket = aws_s3_bucket.upload_bucket.id
  lambda_function {
    lambda_function_arn = aws_lambda_function.process_s3_event.arn
    events              = ["s3:ObjectCreated:*"]
  }
}
resource "aws_lambda_permission" "allow_s3" {
  statement_id  = "${lower(var.prefix)}-allow-s3-invoke-lambda"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.process_s3_event.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.upload_bucket.arn
}
resource "aws_api_gateway_rest_api" "api" {
  name        = "${lower(var.prefix)}-presigned-url-api"
  description = "API for generating presigned URLs"
}
resource "aws_api_gateway_resource" "resource" {
  rest_api_id = aws_api_gateway_rest_api.api.id
  parent_id   = aws_api_gateway_rest_api.api.root_resource_id
  path_part   = "generate-presigned-url"
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
output "api_id" {
  description = "The ID of the API Gateway REST API"
  value       = aws_api_gateway_rest_api.api.id
}
output "region" {
  description = "The AWS region where resources are deployed"
  value       = var.region
}
output "s3_bucket_name" {
  description = "The name of the S3 bucket"
  value       = aws_s3_bucket.upload_bucket.bucket
}
output "sns_topic_arn" {
  description = "The ARN of the SNS topic"
  value       = aws_sns_topic.sns_topic.arn
}
output "lambda_generate_presigned_url_arn" {
  description = "The ARN of the generate_presigned_url Lambda function"
  value       = aws_lambda_function.generate_presigned_url.arn
}
output "lambda_process_s3_event_arn" {
  description = "The ARN of the process_s3_event Lambda function"
  value       = aws_lambda_function.process_s3_event.arn
}
output "lambda_generate_presigned_url_log_group" {
  description = "The name of the CloudWatch log group for the generate_presigned_url Lambda function"
  value       = aws_cloudwatch_log_group.lambda_log_group[0].name
}
output "lambda_process_s3_event_log_group" {
  description = "The name of the CloudWatch log group for the process_s3_event Lambda function"
  value       = aws_cloudwatch_log_group.lambda_log_group[1].name
}