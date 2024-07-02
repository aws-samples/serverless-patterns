variable "region" {}

provider "aws" {
  region  = "${var.region}"
}
data "aws_partition" "current" {}
# IAM Role for Lambda Execution
resource "aws_iam_role" "lambda_execution_role" {
  name               = "lambda-execution-role-for-sfn"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}
# SQS Policy for Lambda Execution Role
resource "aws_iam_role_policy" "sqs_receive_message_policy" {
  name   = "SQSReceiveMessagePolicy"
  role   = aws_iam_role.lambda_execution_role.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect   = "Allow",
      Action   = [
        "sqs:ReceiveMessage",
        "sqs:DeleteMessage",
        "sqs:GetQueueAttributes",
        "sqs:ChangeMessageVisibility"
      ],
      Resource = aws_sqs_queue.sqs_queue.arn
    }]
  })
}
# CloudWatch Logs Policy for Lambda Execution Role
resource "aws_iam_role_policy" "cloudwatch_logs_policy" {
  name   = "CloudWatchLogsPolicy"
  role   = aws_iam_role.lambda_execution_role.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect   = "Allow",
      Action   = [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      Resource = "arn:${data.aws_partition.current.partition}:logs:*:*:*"
    }]
  })
}
# States Execution Policy for Lambda Execution Role
resource "aws_iam_role_policy" "states_execution_policy" {
  name   = "StatesExecutionPolicy"
  role   = aws_iam_role.lambda_execution_role.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect   = "Allow",
      Action   = [
        "states:SendTaskSuccess",
        "states:SendTaskFailure"
      ],
      Resource = aws_sfn_state_machine.state_machine.arn
    }]
  })
}
# SQS Queue
resource "aws_sqs_queue" "sqs_queue" {
  name                      = "sqs-queue"
  delay_seconds             = 0
  max_message_size          = 2048
  message_retention_seconds = 345600
  visibility_timeout_seconds = 30
}
# Lambda Function
resource "aws_lambda_function" "callback_lambda" {
  function_name = "callback-lambda"
  handler       = "index.lambda_handler"
  runtime       = "python3.12"
  role          = aws_iam_role.lambda_execution_role.arn
  timeout       = 25
  # Lambda function code
  filename         = "${path.module}/lambda_function_payload.zip"
  source_code_hash = filebase64sha256("${path.module}/lambda_function_payload.zip")
}
# Event Source Mapping: SQS to Lambda
resource "aws_lambda_event_source_mapping" "event_source_mapping" {
  event_source_arn = aws_sqs_queue.sqs_queue.arn
  function_name    = aws_lambda_function.callback_lambda.arn
  batch_size       = 10
}
# IAM Role for Step Functions Execution
resource "aws_iam_role" "step_functions_execution_role" {
  name               = "step-functions-execution-role-task-token"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "states.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}
# SQS SendMessage Policy for Step Functions Execution Role
resource "aws_iam_role_policy" "sqs_send_message_policy" {
  name   = "SQSSendMessagePolicy"
  role   = aws_iam_role.step_functions_execution_role.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect   = "Allow",
      Action   = [
        "sqs:SendMessage"
      ],
      Resource = aws_sqs_queue.sqs_queue.arn
    }]
  })
}
# Step Functions State Machine
resource "aws_sfn_state_machine" "state_machine" {
  name          = "wait-for-callback-state-machine"
  role_arn      = aws_iam_role.step_functions_execution_role.arn
  definition    = jsonencode({
    Comment = "An example of the Amazon States Language for starting a task and waiting for a callback.",
    StartAt = "Start Task And Wait For Callback",
    States = {
      "Start Task And Wait For Callback" = {
        Type       = "Task",
        Resource   = "arn:${data.aws_partition.current.partition}:states:::sqs:sendMessage.waitForTaskToken",
        Parameters = {
          QueueUrl    = aws_sqs_queue.sqs_queue.url,
          MessageBody = {
            "MessageTitle" = "Task started by Step Functions. Waiting for callback with task token.",
            "TaskToken.$"   = "$$.Task.Token"
          }
        },
        Catch = [{
          ErrorEquals = ["States.ALL"],
          Next        = "Fail"
        }],
        Next = "Success",
        TimeoutSeconds = 10
      },
      "Fail" = {
        Type = "Fail"
      },
      "Success" = {
        Type = "Succeed"
      }
    }
  })
}
# Output
output "state_machine_arn" {
  value = aws_sfn_state_machine.state_machine.arn
}