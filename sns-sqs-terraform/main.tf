# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }

  required_version = ">= 1.0.0"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

data "aws_caller_identity" "current" {}

resource "aws_sns_topic" "sns_sqs_demo_topic" {
  name              = "sns-sqs-demo-${data.aws_caller_identity.current.account_id}"
  kms_master_key_id = "alias/aws/sns"
}

resource "aws_sqs_queue" "sns_sqs_demo_queue" {
  name = "sns-sqs-demo-${data.aws_caller_identity.current.account_id}"
}

resource "aws_sqs_queue_policy" "sns_sqs_demo_sqspolicy" {
  queue_url = aws_sqs_queue.sns_sqs_demo_queue.id
  policy    = <<EOF
{
  "Version": "2012-10-17",
  "Id": "sns_sqs_policy",
  "Statement": [
    {
      "Sid": "Allow SNS publish to SQS",
      "Effect": "Allow",
      "Principal": {
        "Service": "sns.amazonaws.com"
      },
      "Action": "sqs:SendMessage",
      "Resource": "${aws_sqs_queue.sns_sqs_demo_queue.arn}",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "${aws_sns_topic.sns_sqs_demo_topic.arn}"
        }
      }
    }
  ]
}
EOF
}

resource "aws_sns_topic_subscription" "sns_sqs_demo_snssubscription" {
  topic_arn = aws_sns_topic.sns_sqs_demo_topic.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.sns_sqs_demo_queue.arn
}

output "sqs_queue_name" {
  value = aws_sqs_queue.sns_sqs_demo_queue.name
}
output "sqs_queue_url" {
  value = aws_sqs_queue.sns_sqs_demo_queue.url
}

output "sns_topic_name" {
  value = aws_sns_topic.sns_sqs_demo_topic.name
}
output "sns_topic_arn" {
  value = aws_sns_topic.sns_sqs_demo_topic.arn
}