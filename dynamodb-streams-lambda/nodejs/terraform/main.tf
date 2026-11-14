terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_dynamodb_table" "dynamodb_table_users" {
  name             = "UsersIds"
  billing_mode     = "PROVISIONED"
  read_capacity    = 5
  write_capacity   = 5
  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"
  hash_key         = "UserId"

  attribute {
    name = "UserId"
    type = "S"
  }

  tags = {
    Name        = "dynamodb-test-table"
    Environment = "dev"
  }
}

resource "aws_lambda_function" "lambda_dynamodb_stream_handler" {
  function_name    = "process-usersids-records"
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = data.archive_file.lambda_zip_file.output_base64sha256
  handler          = "index.handler"
  role             = aws_iam_role.iam_for_lambda.arn
  runtime          = "nodejs24.x"
}

data "archive_file" "lambda_zip_file" {
  type        = "zip"
  source_file = "${path.module}/src/index.js"
  output_path = "${path.module}/lambda.zip"
}

resource "aws_lambda_event_source_mapping" "lambda_dynamodb" {
  event_source_arn  = aws_dynamodb_table.dynamodb_table_users.stream_arn
  function_name     = aws_lambda_function.lambda_dynamodb_stream_handler.arn
  starting_position = "LATEST"
}

resource "aws_iam_role" "iam_for_lambda" {
  name = "iam_for_lambda"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role_policy" "dynamodb_lambda_policy" {
  name   = "lambda-dynamodb-policy"
  role   = aws_iam_role.iam_for_lambda.id
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
        "Sid": "AllowLambdaFunctionToCreateLogs",
        "Action": [ 
            "logs:*" 
        ],
        "Effect": "Allow",
        "Resource": [ 
            "arn:aws:logs:*:*:*" 
        ]
    },
    {
        "Sid": "AllowLambdaFunctionInvocation",
        "Effect": "Allow",
        "Action": [
            "lambda:InvokeFunction"
        ],
        "Resource": [
            "${aws_dynamodb_table.dynamodb_table_users.arn}/stream/*"
        ]
    },
    {
        "Sid": "APIAccessForDynamoDBStreams",
        "Effect": "Allow",
        "Action": [
            "dynamodb:GetRecords",
            "dynamodb:GetShardIterator",
            "dynamodb:DescribeStream",
            "dynamodb:ListStreams"
        ],
        "Resource": "${aws_dynamodb_table.dynamodb_table_users.arn}/stream/*"
    }
  ]
}
EOF
}

output "dynamodb_usersIds_arn" {
  value = aws_dynamodb_table.dynamodb_table_users.arn
    description = "The ARN of the DynamoDB Users Ids table"
}

output "lambda_processing_arn" {
  value = aws_lambda_function.lambda_dynamodb_stream_handler.arn
    description = "The ARN of the Lambda function processing the DynamoDB stream"
}
