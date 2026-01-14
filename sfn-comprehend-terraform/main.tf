provider "aws" {
  region = "us-east-1"  # Change to your preferred region
}
# ---------------------------
# IAM Role for Step Functions
# ---------------------------
resource "aws_iam_role" "states_execution_role" {
  name = "StatesExecutionRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = {
        Service = "states.amazonaws.com"
      },
      Action = "sts:AssumeRole"
    }]
  })
}
# ---------------------------
# IAM Policies
# ---------------------------
resource "aws_iam_role_policy" "cwlogs" {
  name = "CWLogs"
  role = aws_iam_role.states_execution_role.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Action = [
        "logs:CreateLogDelivery",
        "logs:CreateLogStream",
        "logs:GetLogDelivery",
        "logs:UpdateLogDelivery",
        "logs:DeleteLogDelivery",
        "logs:ListLogDeliveries",
        "logs:PutLogEvents",
        "logs:PutResourcePolicy",
        "logs:DescribeResourcePolicies",
        "logs:DescribeLogGroups"
      ],
      Resource = "*"
    }]
  })
}
resource "aws_iam_role_policy" "comprehend_access" {
  name = "ComprehendAccess"
  role = aws_iam_role.states_execution_role.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Action = [
        "comprehend:BatchDetectKeyPhrases",
        "comprehend:DetectDominantLanguage",
        "comprehend:DetectEntities",
        "comprehend:BatchDetectEntities",
        "comprehend:DetectKeyPhrases",
        "comprehend:DetectSentiment",
        "comprehend:BatchDetectDominantLanguage",
        "comprehend:BatchDetectSentiment"
      ],
      Resource = "*"
    }]
  })
}
# ---------------------------
# CloudWatch Log Group
# ---------------------------
resource "aws_cloudwatch_log_group" "state_machine_logs" {
  name              = "/stepfunctions/StateMachineExpressSyncToComprehend"
  retention_in_days = 14
}
# ---------------------------
# Step Function State Machine
# ---------------------------
resource "aws_sfn_state_machine" "detect_sentiment_state_machine" {
  name     = "StateMachineExpressSyncToComprehend"
  role_arn = aws_iam_role.states_execution_role.arn
  type     = "STANDARD"
  logging_configuration {
    level                  = "ALL"
    include_execution_data = false
    log_destination = "${aws_cloudwatch_log_group.state_machine_logs.arn}:*"
      }
    
  definition = file("${path.module}/statemachine/detectSentiment.asl.json")
}
# ---------------------------
# Output
# ---------------------------
output "state_machine_arn" {
  description = "ARN of the Step Function"
  value       = aws_sfn_state_machine.detect_sentiment_state_machine.arn
}