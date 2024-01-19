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
  profile = "default"
  region  = "us-east-1"
}

data "aws_caller_identity" "current" {}

# Create new IAM Policy and Role for EventBridge Scheduler
resource "aws_iam_policy" "eb_access_policy" {
  name        = "eb-access-policy"
  description = "Policy for EventBridge Scheduler to trigger Step Functions"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "states:StartExecution"
        ],
        Effect   = "Allow"
        Resource = "${aws_sfn_state_machine.sfn_state_machine.arn}"
      }
    ]
  })
}

resource "aws_iam_role" "eventbridge_scheduler_iam_role" {
  name_prefix         = "eb-scheduler-role-"
  managed_policy_arns = [aws_iam_policy.eb_access_policy.arn]
  path = "/"
  assume_role_policy  = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "scheduler.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF
}

# Create new IAM Policy and Role for Step Function 

resource "aws_iam_role" "sfn_iam_role" {
  name = "sfn-iam-role"
  managed_policy_arns = ["arn:aws:iam::aws:policy/AWSStepFunctionsFullAccess"]
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "states.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

# resource "aws_iam_role_policy_attachment" "step_function_role_attachment" {
#   role       = aws_iam_role.sfn_iam_role.name
#   policy_arn = "arn:aws:iam::aws:policy/service-role/AWSStepFunctionsFullAccess"
# }

# Create new Step Function State Machine
resource "aws_sfn_state_machine" "sfn_state_machine" {
  name     = "my-state-machine"
  role_arn = aws_iam_role.sfn_iam_role.arn

  definition = <<EOF
{
  "Comment": "A Hello World example of the Amazon States Language",
  "StartAt": "HelloWorld",
  "States": {
    "HelloWorld": {
      "Type": "Pass",
      "End": true
    }
  }
}
EOF
}

# Create new Eventbridge Scheduler
resource "aws_scheduler_schedule" "my_scheduler" {
  name = "my-scheduler"

  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "rate(1 minutes)"

  target {
    arn      = aws_sfn_state_machine.sfn_state_machine.arn
    role_arn = aws_iam_role.eventbridge_scheduler_iam_role.arn

    input = jsonencode({
      Payload = "Hello, ServerlessLand!"
    })
  }
}

output "EventBridgeSchedulerArn" {
  value       = aws_scheduler_schedule.my_scheduler.arn
  description = "EventBridge my-scheduler ARN"
}

output "StateMachineArn" {
      value       = aws_sfn_state_machine.sfn_state_machine.arn
  description = "Step Function my-state-machine ARN"
}
