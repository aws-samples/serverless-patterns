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
  bucket = "serverlessland-terraform-s3-sns-${data.aws_caller_identity.current.account_id}"
}

# Create a new SNS topic
resource "aws_sns_topic" "MySNSTopic" {
}

# Allow the S3 bucket to publish to the SNS topic
resource "aws_sns_topic_policy" "MySNSTopicPolicy" {
  arn    = aws_sns_topic.MySNSTopic.arn
  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": "sns:Publish",
      "Resource": "${aws_sns_topic.MySNSTopic.arn}",
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

# Create a new notification for the SNS topic when a new object is created and set the SNS as target
resource "aws_s3_bucket_notification" "MyS3BucketNotification" {
  bucket = aws_s3_bucket.MyS3Bucket.id
  topic {
    topic_arn = aws_sns_topic.MySNSTopic.arn
    events    = ["s3:ObjectCreated:*"]
  }
}

# Display the S3 bucket and the SNS topic
output "S3-Bucket" {
  value       = aws_s3_bucket.MyS3Bucket.id
  description = "The S3 Bucket"
}
output "SNS-Topic-ARN" {
  value       = aws_sns_topic.MySNSTopic.arn
  description = "The SNS Topic ARN"
}