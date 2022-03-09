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

# Create an IAM role for Eventbridge
resource "aws_iam_role" "EventBridgeRole" {
  assume_role_policy = <<POLICY1
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Principal" : {
        "Service" : "events.amazonaws.com"
      },
      "Action" : "sts:AssumeRole"
    }
  ]
}
POLICY1
}

# Create an IAM role for Step Functions State Machine
resource "aws_iam_role" "StateMachineRole" {
  assume_role_policy = <<POLICY2
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Principal" : {
        "Service" : "states.amazonaws.com"
      },
      "Action" : "sts:AssumeRole"
    }
  ]
}
POLICY2
}

# Create an IAM policy for Eventbridge to be able to start a Step Function execution
resource "aws_iam_policy" "EventBridgePolicy" {
  policy = <<POLICY3
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "states:StartExecution"
      ],
      "Resource" : "${aws_sfn_state_machine.sfn_state_machine.arn}"
    }
  ]
}
POLICY3
}

# Create an IAM policy to enable Step Function State Machine to push logs to CloudWatch logs
resource "aws_iam_policy" "StateMachineLogDeliveryPolicy" {
  policy = <<POLICY4
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "logs:CreateLogDelivery",
        "logs:GetLogDelivery",
        "logs:UpdateLogDelivery",
        "logs:DeleteLogDelivery",
        "logs:ListLogDeliveries",
        "logs:PutResourcePolicy",
        "logs:DescribeResourcePolicies",
        "logs:DescribeLogGroups"
      ],
      "Resource" : "*"
    }
  ]
}
POLICY4
}

# Attach the IAM policies to the equivalent rule
resource "aws_iam_role_policy_attachment" "EventBridgePolicyAttachment" {
  role       = aws_iam_role.EventBridgeRole.name
  policy_arn = aws_iam_policy.EventBridgePolicy.arn
}

resource "aws_iam_role_policy_attachment" "StateMachinePolicyAttachment" {
  role       = aws_iam_role.StateMachineRole.name
  policy_arn = aws_iam_policy.StateMachineLogDeliveryPolicy.arn
}

# Create an Log group for the Step Function
resource "aws_cloudwatch_log_group" "MyLogGroup" {
  name_prefix = "/aws/vendedlogs/states/StateMachine-terraform-"
}

# Create a Step Function State Machine
resource "aws_sfn_state_machine" "sfn_state_machine" {
  name     = "eventbridge-state-machine-demo-${data.aws_caller_identity.current.account_id}"
  role_arn = aws_iam_role.StateMachineRole.arn

  definition = <<SFN
{
  "Comment": "Simple State Machine with Choice",
  "StartAt": "WhichPath?",
  "States": {
    "WhichPath?": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.detail.Path",
          "StringEquals": "A",
          "Next": "PathA"
        },
        {
          "Variable": "$.detail.Path",
          "StringEquals": "B",
          "Next": "PathB"
        }
      ],
      "Default": "Fail"
    },
    "PathA": {
      "Type": "Pass",
      "End": true
    },
    "PathB": {
      "Type": "Pass",
      "End": true
    },
    "Fail": {
      "Type": "Fail"
    }
  }
}
SFN

  logging_configuration {
    log_destination        = "${aws_cloudwatch_log_group.MyLogGroup.arn}:*"
    include_execution_data = true
    level                  = "ALL"
  }
}

# Create an EventBridge Rule
resource "aws_cloudwatch_event_rule" "MyEventRule" {
  event_pattern = <<PATTERN
{
  "account": ["${data.aws_caller_identity.current.account_id}"],
  "source": ["demo.sfn"]
}
PATTERN
}

# Set the Step Function as target to the Eventbridge rule
resource "aws_cloudwatch_event_target" "SFNTarget" {
  rule     = aws_cloudwatch_event_rule.MyEventRule.name
  arn      = aws_sfn_state_machine.sfn_state_machine.arn
  role_arn = aws_iam_role.EventBridgeRole.arn
}

#output the CloudWatch Log Stream Name
output "CW-Logs-Stream-Name" {
  value       = aws_cloudwatch_log_group.MyLogGroup.id
  description = "The CloudWatch Log Group Name"
}

output "StepFunction-Name" {
  value       = aws_sfn_state_machine.sfn_state_machine.name
  description = "The Step Function Name"
}