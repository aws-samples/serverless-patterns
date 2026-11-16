# This template uses publishes an EventBridge event every minute using Amazon EventBridge Scheduler.

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


# Create custom event bus

resource "aws_cloudwatch_event_bus" "scheduler-custom-event-bus" {
    name = "scheduler-event-bus"
}

#Configuring dead-letter queues: https://docs.aws.amazon.com/scheduler/latest/UserGuide/configuring-schedule-dlq.html
# Use cmd for troubleshooting "aws sqs get-queue-attributes --queue-url your-dlq-url --attribute-names QueueArn"

resource "aws_sqs_queue" "scheduler-dlq" {
    name = "scheduler-dlq"
}

# This section configures an EventBridge Rule that uses a CloudWatch Log Group as a target

resource "aws_cloudwatch_event_rule" "rule" {
    name = "schedule-rule"
    event_bus_name = aws_cloudwatch_event_bus.scheduler-custom-event-bus.name

    event_pattern = jsonencode({
        detail-type = ["message"]
    })
}

# Create CloudWatch Log Group

resource "aws_cloudwatch_log_group" "example" {
    name = "/aws/events/schedulerApplication"
    retention_in_days = 1
}

data "aws_iam_policy_document" "example_log_policy" {
  statement {
    effect = "Allow"
    actions = [
      "logs:CreateLogStream"
    ]

    resources = [
      "${aws_cloudwatch_log_group.example.arn}:*"
    ]

    principals {
      type = "Service"
      identifiers = [
        "events.amazonaws.com",
        "delivery.logs.amazonaws.com"
      ]
    }
  }
  statement {
    effect = "Allow"
    actions = [
      "logs:PutLogEvents"
    ]

    resources = [
      "${aws_cloudwatch_log_group.example.arn}:*:*"
    ]

    principals {
      type = "Service"
      identifiers = [
        "events.amazonaws.com",
        "delivery.logs.amazonaws.com"
      ]
    }

    condition {
      test     = "ArnEquals"
      values   = [aws_cloudwatch_event_rule.rule.arn]
      variable = "aws:SourceArn"
    }
  }
}

resource "aws_cloudwatch_log_resource_policy" "example" {
  policy_document = data.aws_iam_policy_document.example_log_policy.json
  policy_name     = "schedulerApplication-log-publishing-policy"
}

resource "aws_cloudwatch_event_target" "example" {
  rule = aws_cloudwatch_event_rule.rule.name
  arn  = aws_cloudwatch_log_group.example.arn
  event_bus_name = aws_cloudwatch_event_bus.scheduler-custom-event-bus.name
}


# Create EventBridge Schedule

resource "aws_scheduler_schedule" "eventbridge-schedule" {
  name = "eventbridge-schedule"
  
  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "rate(1 minutes)" # 
  schedule_expression_timezone = "US/Eastern" # Default is UTC
  description = "Rate schedule to EventBridge custom bus"

  target {
    arn = aws_cloudwatch_event_bus.scheduler-custom-event-bus.arn
    role_arn = aws_iam_role.scheduler-role.arn

    dead_letter_config {
        arn = aws_sqs_queue.scheduler-dlq.arn
    }

    eventbridge_parameters {
      detail_type = "message"
      source = "scheduledEvents"
    }

    input = jsonencode(
      {"msg": "Hello from EventBridge Scheduler!"}
    )
  }
}

resource "aws_iam_policy" "scheduler_policy" {
  name = "scheduler_policy"

  policy = jsonencode(
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "events:putEvents",
                    "sqs:SendMessage"
                ],
                "Resource": "*"
            }
        ]
    }
  )
}

resource "aws_iam_role" "scheduler-role" {
  name = "scheduler-role"
  managed_policy_arns = [aws_iam_policy.scheduler_policy.arn]

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
