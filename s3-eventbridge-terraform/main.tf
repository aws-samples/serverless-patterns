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
  bucket = "serverlessland-terraform-s3-eventbridge-${data.aws_caller_identity.current.account_id}"
}

# Send notifications to EventBridge for all events in the bucket
resource "aws_s3_bucket_notification" "MyS3BucketNotification" {
  bucket      = aws_s3_bucket.MyS3Bucket.id
  eventbridge = true
}

# Create an EventBridge rule
resource "aws_cloudwatch_event_rule" "MyEventRule" {
  description   = "Object create events on bucket s3://${aws_s3_bucket.MyS3Bucket.id}"
  event_pattern = <<EOF
{
  "detail-type": [
    "Object Created"
  ],
  "source": [
    "aws.s3"
  ],
  "detail": {
    "bucket": {
      "name": ["${aws_s3_bucket.MyS3Bucket.id}"]
    }
  }
}
EOF
}

# Set the SNS topic as a target of the EventBridge rule
resource "aws_cloudwatch_event_target" "MyEventRuleTarget" {
  rule      = aws_cloudwatch_event_rule.MyEventRule.name
  arn       = aws_sns_topic.MySNSTopic.arn
}

# Create a new SNS topic
resource "aws_sns_topic" "MySNSTopic" {
}

# Allow EventBridge to publish to the SNS topic
resource "aws_sns_topic_policy" "MySNSTopicPolicy" {
  arn    = aws_sns_topic.MySNSTopic.arn
  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AWSEventsPermission",
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Action": "sns:Publish",
      "Resource": "${aws_sns_topic.MySNSTopic.arn}",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "${aws_cloudwatch_event_rule.MyEventRule.arn}"
        }
      }
    }
  ]
}
POLICY
}

# Display the EventBridge rule, S3 bucket and SNS topic
output "EventBridge-Rule-Name" {
  value       = aws_cloudwatch_event_rule.MyEventRule.name
  description = "The EventBridge Rule Name"
}
output "S3-Bucket" {
  value       = aws_s3_bucket.MyS3Bucket.id
  description = "The S3 Bucket"
}
output "SNS-Topic-ARN" {
  value       = aws_sns_topic.MySNSTopic.arn
  description = "The SNS Topic ARN"
}
