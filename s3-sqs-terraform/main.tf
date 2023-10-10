terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

data "aws_caller_identity" "current" {}

# Create a new S3 bucket
resource "aws_s3_bucket" "MyS3Bucket" {
  bucket = "serverlessland-terraform-s3-sqs-${data.aws_caller_identity.current.account_id}"
}

# Create a new SQS queue
resource "aws_sqs_queue" "MySQSqueue" {
}

# Allow the S3 bucket to write to the SQS queue
resource "aws_sqs_queue_policy" "test" {
  queue_url = aws_sqs_queue.MySQSqueue.id
  policy    = <<POLICY
{
  "Version": "2012-10-17",
  "Id": "sqspolicy",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": "sqs:SendMessage",
      "Resource": "${aws_sqs_queue.MySQSqueue.arn}",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "${aws_s3_bucket.MyS3Bucket.arn}"
        }
      }
    }
  ]
}
POLICY
}

# Create a new notification for the SQS queue when a new object is created and set the SQS as target
resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.MyS3Bucket.id
  queue {
    queue_arn = aws_sqs_queue.MySQSqueue.arn
    events    = ["s3:ObjectCreated:*"]
  }
}

# Display the S3 bucket and the SQS queue URL
output "S3-Bucket" {
  value       = aws_s3_bucket.MyS3Bucket.id
  description = "The S3 Bucket"
}
output "SQS-QUEUE" {
  value       = aws_sqs_queue.MySQSqueue.id
  description = "The SQS Queue URL"
}