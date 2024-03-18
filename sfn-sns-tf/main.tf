provider "aws" {
  region = "us-east-1"
}

variable "region" {
  description = "AWS region"
  default     = "us-east-1"  # Provide your default region if needed
}

variable "sns_endpoint" {
  description = "Email endpoint for SNS subscription"
  # Add a default if you have a specific endpoint to use universally
}

resource "aws_sns_topic" "state_machine_sns_topic" {
  name = "StateMachineSNSTopic"
}

resource "aws_iam_role" "states_execution_role" {
  name = "StatesExecutionRole"
  assume_role_policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = {
          Service = "states.${var.region}.amazonaws.com"
        }
        Action    = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy" "sns_access_policy" {
  name        = "SNSAccessPolicy"
  description = "IAM policy for SNS access"
  
  policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Action    = "sns:Publish"
        Resource  = aws_sns_topic.state_machine_sns_topic.arn
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "sns_access_attachment" {
  policy_arn = aws_iam_policy.sns_access_policy.arn
  role       = aws_iam_role.states_execution_role.name
}

resource "aws_sns_topic_subscription" "state_machine_sns_topic_subscription" {
  topic_arn = aws_sns_topic.state_machine_sns_topic.arn
  protocol  = "email"
  endpoint  = var.sns_endpoint
}

resource "aws_sfn_state_machine" "state_machine_to_sns" {
  name     = "StateMachinetoSNS"
  role_arn = aws_iam_role.states_execution_role.arn

  definition = <<EOF
{
  "StartAt": "HandleInputAndMessage",
  "States": {
    "HandleInputAndMessage": {
      "Type": "Pass",
      "Result": {
        "Input": "You just received a message from the state machine!",
        "Message": "hello"
      },
      "ResultPath": "$.InputAndMessage",
      "Next": "PublishMessage"
    },
    "PublishMessage": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sns:publish",
      "Parameters": {
        "TopicArn": "${aws_sns_topic.state_machine_sns_topic.arn}",
        "Message.$": "$.InputAndMessage"
      },
      "End": true
    }
  }
}
EOF
}


output "state_machine_to_sns" {
  value       = aws_sfn_state_machine.state_machine_to_sns.arn
  description = "StateMachinetoSNS Arn"
}

output "state_machine_sns_topic_name" {
  value       = aws_sns_topic.state_machine_sns_topic.name
  description = "SNS topic name"
}

output "state_machine_sns_topic_arn" {
  value       = aws_sns_topic.state_machine_sns_topic.arn
  description = "SNS topic ARN"
}
