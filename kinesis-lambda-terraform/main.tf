terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.22"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  region = "us-east-1"  # Change to your desired region
}
resource "aws_kinesis_stream" "sample_stream" {
  name             = "sample-stream"
  shard_count      = 1
  retention_period = 24
}
resource "aws_lambda_function" "sample_lambda" {
  filename         = "sample_lambda.zip"  # Path to your Lambda code ZIP file
  function_name    = "sample-lambda"
  role             = aws_iam_role.lambda_role.arn
  handler          = "index.handler"
  runtime          = "nodejs14.x"  # Change to your preferred runtime
}
resource "aws_iam_role" "lambda_role" {
  name = "lambda-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_lambda_event_source_mapping" "sample_mapping" {
  event_source_arn = aws_kinesis_stream.sample_stream.arn
  function_name    = aws_lambda_function.sample_lambda.arn
  starting_position = "LATEST"
}

output "kinesis_data_stream" {
    value = aws_kinesis_stream.sample_stream.arn
    description = "Kinesis data stream with shards"
}

output "consumer_function" {
  value = aws_lambda_function.sample_function.arn
  description = "Consumer Function function name"
}