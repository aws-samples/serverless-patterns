terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>5.41"
    }
  }

  required_version = ">=1.2.0"
}

provider "aws" {
  region = "ap-south-1"
}

data "archive_file" "lambda_handler_zip_file" {
  type        = "zip"
  source_file = "${path.module}/handler.py"
  output_path = "${path.module}/sqs-lambda-s3.zip"
}

# Lambda function
resource "aws_lambda_function" "event-processor" {
  function_name    = "event-processor"
  filename         = data.archive_file.lambda_handler_zip_file.output_path
  source_code_hash = filebase64sha256(data.archive_file.lambda_handler_zip_file.output_path)
  handler          = "handler.lambda_handler"
  runtime          = "python3.12"
  role             = aws_iam_role.event-processor-exec-role.arn
}

# Lambda execution role
resource "aws_iam_role" "event-processor-exec-role" {
  name = "event-processor-exec-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action = [
          "sts:AssumeRole"
        ]
      }
    ]
  })
}

# Lambda exec role policy
resource "aws_iam_policy" "event-processor-policy" {
  name = "event-processor-policy"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "sts:AssumeRole"
        ]
        Resource = [aws_lambda_function.event-processor.arn]
      },
      {
        Effect = "Allow"
        Action = [
          "sqs:ReceiveMessage",
          "sqs:GetQueueAttributes",
          "sqs:DeleteMessage"
        ]
        Resource = aws_sqs_queue.event-collector.arn
      },
      {
        Effect = "Allow"
        Action = [
          "s3:PutObject"
        ]
        Resource = [
          "${aws_s3_bucket.event-storage.arn}",
          "${aws_s3_bucket.event-storage.arn}/*",
        ]
      }
    ]
  })
}

# Attach policy to Lambda execution role for SQS permissions
resource "aws_iam_role_policy_attachment" "lambda-exec-role-policy" {
  policy_arn = aws_iam_policy.event-processor-policy.arn
  role       = aws_iam_role.event-processor-exec-role.name
}

# Attach policy to Lambda exec role for CloudWatch permissions
resource "aws_iam_role_policy_attachment" "lambda-policy" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = aws_iam_role.event-processor-exec-role.name
}

# Event source mapping to create a trigger for Lambda to read from SQS queue
resource "aws_lambda_event_source_mapping" "event-processor-event-src-map" {
  function_name    = aws_lambda_function.event-processor.arn
  event_source_arn = aws_sqs_queue.event-collector.arn
  enabled          = true
  depends_on = [
    aws_lambda_function.event-processor,
    aws_sqs_queue.event-collector,
    aws_sqs_queue_policy.event-collector-policy,
    aws_iam_policy.event-processor-policy
  ]
}

# SQS Queue
resource "aws_sqs_queue" "event-collector" {
  name             = "event-collector-queue"
  max_message_size = 2048
}

# SQS queue policy
resource "aws_sqs_queue_policy" "event-collector-policy" {
  queue_url = aws_sqs_queue.event-collector.url
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action = [
          "sqs:ReceiveMessage",
          "sqs:GetQueueAttributes",
          "sqs:DeleteMessage"
        ]
        Resource = aws_sqs_queue.event-collector.arn
        Condition = {
          ArnEquals = {
            "aws:SourceArn" = aws_lambda_function.event-processor.arn
          }
        }
      }
    ]
  })

  depends_on = [
    aws_sqs_queue.event-collector,
    aws_lambda_function.event-processor
  ]
}

# S3 bucket
resource "aws_s3_bucket" "event-storage" {
  bucket        = "my-bucket-20250329"
  force_destroy = true
  tags = {
    Name = "event-storage"
  }
}

# Bucket policy document
data "aws_iam_policy_document" "bucket-policy" {
  statement {
    effect  = "Allow"
    actions = ["s3:PutObject"]
    principals {
      type = "Service"
      identifiers = [
        "lambda.amazonaws.com"
      ]
    }
    resources = [
      "${aws_s3_bucket.event-storage.arn}",
      "${aws_s3_bucket.event-storage.arn}/*",
    ]
    condition {
      test     = "ArnEquals"
      variable = "aws:SourceArn"
      values   = ["${aws_lambda_function.event-processor.arn}"]
    }
  }
}

# Bucket policy
resource "aws_s3_bucket_policy" "event-storage-bucket-policy" {
  bucket = aws_s3_bucket.event-storage.id
  policy = data.aws_iam_policy_document.bucket-policy.json
}
