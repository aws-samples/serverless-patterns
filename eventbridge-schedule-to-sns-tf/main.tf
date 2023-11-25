provider "aws" {
  region = "us-east-1"  # Change to your desired region
}

resource "aws_iam_policy" "eventbridge_scheduler_policy" {
  name        = "EventBridgeSchedulerPolicy"
  description = "IAM policy for EventBridge Scheduler"
  
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action   = "sns:Publish",
        Effect   = "Allow",
        Resource = aws_sns_topic.aws_logins.arn,
      },
    ],
  })
}

resource "aws_iam_role" "eventbridge_scheduler_role" {
  name = "EventBridgeSchedulerRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "events.amazonaws.com",
        },
      },
    ],
  })
}

resource "aws_iam_role_policy_attachment" "eventbridge_scheduler_attachment" {
  policy_arn = aws_iam_policy.eventbridge_scheduler_policy.arn
  role       = aws_iam_role.eventbridge_scheduler_role.name
}

resource "aws_sns_topic" "aws_logins" {
  name = "MySNSTopic"
}

resource "aws_sns_topic_policy" "default" {
  arn    = aws_sns_topic.aws_logins.arn
  policy = data.aws_iam_policy_document.sns_topic_policy.json
}

data "aws_iam_policy_document" "sns_topic_policy" {
  statement {
    effect  = "Allow"
    actions = ["SNS:Publish"]

    principals {
      type        = "Service"
      identifiers = ["events.amazonaws.com"]
    }

    resources = [aws_sns_topic.aws_logins.arn]
  }
}  

resource "aws_cloudwatch_event_rule" "eventbridge_scheduler" {
  name                = "EventBridgeScheduler"
  description         = "EventBridge Scheduler Rule"
  schedule_expression = "rate(5 minutes)"
  
  event_pattern = jsonencode({
    source = ["aws.events"],
  })
}  
  
resource "aws_cloudwatch_event_target" "sns" {
  rule      = aws_cloudwatch_event_rule.eventbridge_scheduler.name
  target_id = "SendToSNS"
  arn       =  aws_sns_topic.aws_logins.arn
  }


output "sns_topic_arn" {
  value = aws_sns_topic.aws_logins.arn
}

output "iam_role_arn" {
  value = aws_iam_role.eventbridge_scheduler_role.arn
}

output "cloudwatch_event_rule_name" {
  value = aws_cloudwatch_event_rule.eventbridge_scheduler.name
}

