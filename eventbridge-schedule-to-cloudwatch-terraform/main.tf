# This template uses EventBridge Scheduler to insert custom metric data into CloudWatch on a schedule. 

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.64.0"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

data "aws_caller_identity" "current" {}



# This section creates cron schedules using Amazon EventBridge Scheduler, as well as the required IAM roles to interact with CloudWatch

resource "aws_scheduler_schedule" "cloudwatch-schedule" {
  name = "cloudwatch-schedule"
  
  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "rate(1 minutes)"
  schedule_expression_timezone = "US/Eastern" # Default is UTC
  description = "Start putMetric event"

  target {
    arn = "arn:aws:scheduler:::aws-sdk:cloudwatch:putMetricData"
    role_arn = aws_iam_role.scheduler-cloudwatch-role.arn
  
    input = jsonencode(
        {
            "MetricData": [
                {
                    "MetricName": "CustomSchedulerData",
                    "Dimensions": [
                        { "Name": "Type", "Value": "1" }
                    ],
                    "Unit": "Count",
                    "Value": 1
                }
            ],
            "Namespace": "MyData"
        }
    )
  }
}


resource "aws_iam_policy" "scheduler_cloudwatch_policy" {
  name = "scheduler_cloudwatch_policy"

  policy = jsonencode(
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                "cloudwatch:PutMetricData"
                ],
                "Resource": "*"
            }
        ]
    }
  )
}

resource "aws_iam_role" "scheduler-cloudwatch-role" {
  name = "scheduler-cloudwatch-role"
  managed_policy_arns = [aws_iam_policy.scheduler_cloudwatch_policy.arn]

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "scheduler.amazonaws.com"
        }
      },
    ]
  })
}