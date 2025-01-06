/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- main.tf ---

# Create SQS Queue
resource "aws_sqs_queue" "source_queue" {
  name = "source-queue"
}

# Create Step Functions State Machine
resource "aws_sfn_state_machine" "target_state_machine" {
  name     = "target-state-machine"
  role_arn = aws_iam_role.step_functions_role.arn

  definition = <<EOF
{
  "StartAt": "StartState",
  "States": {
    "StartState": {
      "Type": "Pass",
      "End": true
    }
  }
}
EOF
}

# IAM Role for Step Functions
resource "aws_iam_role" "step_functions_role" {
  name = "step-functions-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "states.amazonaws.com"
        }
      }
    ]
  })
}

# IAM Role for EventBridge Pipe
resource "aws_iam_role" "pipe_role" {
  name = "eventbridge-pipe-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "pipes.amazonaws.com"
        }
      }
    ]
  })
}

# IAM Policy for SQS access
resource "aws_iam_role_policy" "sqs_policy" {
  name = "sqs-policy"
  role = aws_iam_role.pipe_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "sqs:ReceiveMessage",
          "sqs:DeleteMessage",
          "sqs:GetQueueAttributes"
        ]
        Resource = aws_sqs_queue.source_queue.arn
      }
    ]
  })
}

# IAM Policy for Step Functions access
resource "aws_iam_role_policy" "step_functions_policy" {
  name = "step-functions-policy"
  role = aws_iam_role.pipe_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "states:StartExecution"
        ]
        Resource = aws_sfn_state_machine.target_state_machine.arn
      }
    ]
  })
}

# EventBridge Pipe
resource "aws_pipes_pipe" "sqs_to_step_functions_pipe" {
  name     = "sqs-to-step-functions-pipe"
  role_arn = aws_iam_role.pipe_role.arn
  source   = aws_sqs_queue.source_queue.arn
  target   = aws_sfn_state_machine.target_state_machine.arn

  source_parameters {
    sqs_queue_parameters {
      batch_size = 1
    }
    filter_criteria {
      filter {
        pattern = jsonencode({
          body = {
            status = ["COMPLETE"]
          }
        })
      }
    }
  }

  target_parameters {
    step_function_state_machine_parameters {
      invocation_type = "FIRE_AND_FORGET"
    }
    input_template = jsonencode({
      playerid   = "<$.body.id>"
      teamname   = "<$.body.team>"
      teamstatus = "<$.body.status>"
    })
  }
}


# Outputs
output "sqs_queue_url" {
    description = "The URL of the source SQS queue"
    value       = aws_sqs_queue.source_queue.url
}

output "eventbridge_pipe_arn" {
    description = "The ARN of the EventBridge Pipe"
    value       = aws_pipes_pipe.sqs_to_step_functions_pipe.arn
}

output "state_machine_arn" {
    description = "The ARN of the Step Functions state machine"
    value       = aws_sfn_state_machine.target_state_machine.arn
}

