terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.63"
    }
  }

  required_version = ">= 0.14.9"
}

# Fetching current Account ID and AWS region
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

variable "national_team" {
  description = "National Team Name"
  type        = string
  default     = "Argentina"
}

#################################################################
# DynamoDB Table
#################################################################
# Creating the DynamoDB Table
resource "aws_dynamodb_table" "WorldCup-DB" {
  name            = "WorldCup-DB"
  billing_mode    = "PROVISIONED"
  hash_key        = "PlayerName"
  stream_enabled  = true
  stream_view_type = "NEW_AND_OLD_IMAGES"

  attribute {
    name = "PlayerName"
    type = "S"
  }

  read_capacity = 1
  write_capacity = 1
  
}

#################################################################
# Step Functions - State Machine
#################################################################
# Creating the Step Functions Machine
resource "aws_sfn_state_machine" "WorldCup-SF_machine" {
  name        = "WorldCup-SF_machine"
  role_arn    = aws_iam_role.WorldCup-SFRole.arn
  type        = "EXPRESS"
  definition  = file("workflow/ddb-pipes-sfn.asl.json")
  
  logging_configuration {
    log_destination        = "${aws_cloudwatch_log_group.WorldCup-SF_LogGroup.arn}:*"
    include_execution_data = true
    level                  = "ALL"
  }

  tags = {
    Name = "WorldCup-SF_machine"
  }
  
}

# Creating a CloudWatch Log Group for Step Functions logs
resource "aws_cloudwatch_log_group" "WorldCup-SF_LogGroup" {
  name              = "ddb-stream-pipes-sf/WorldCup-StateMachine"
  retention_in_days = 30
}

# Creating necessary IAM roles and policies for the Step Functions
resource "aws_iam_role" "WorldCup-SFRole" {
  name = "WorldCup-SFRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "states.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })

  inline_policy {
    name = "CloudWatchLogs"

    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Effect = "Allow"
          Action = [
            "logs:CreateLogDelivery",
            "logs:GetLogDelivery",
            "logs:UpdateLogDelivery",
            "logs:DeleteLogDelivery",
            "logs:ListLogDeliveries",
            "logs:PutResourcePolicy",
            "logs:DescribeResourcePolicies",
            "logs:DescribeLogGroups"
          ]
          Resource = "*"
        }
      ]
    })
  }
}

#################################################################
# Event Bridge - Pipes
#################################################################
# Creating the Event Bridge - Pipes
resource "aws_pipes_pipe" "WorldCup-ddb_stream_to_sfn" {
  name      = "WorldCup-ddb_stream_to_sfn"
  role_arn  = aws_iam_role.WorldCup-event_bridge_pipes_role.arn
  source    = aws_dynamodb_table.WorldCup-DB.stream_arn

  source_parameters {
    filter_criteria {
      filter {
        pattern = jsonencode({
          dynamodb = {
            NewImage = {
              Nationality = {
                S = [
                  {
                    prefix = var.national_team
                  }
                ]
              }
            }
          }
        })
      }
    }

    dynamodb_stream_parameters {
      starting_position = "LATEST"
      batch_size        = 1
    }
  }

  target = aws_sfn_state_machine.WorldCup-SF_machine.arn

  target_parameters {
    step_function_state_machine_parameters {
      invocation_type = "FIRE_AND_FORGET"
    }
  }
}

# Creating necessary IAM roles and policies for the Step Functions
resource "aws_iam_role" "WorldCup-event_bridge_pipes_role" {
  name = "WorldCup-event_bridge_pipes_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "pipes.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })

  inline_policy {
    name = "WorldCup-CloudWatchLogs"

    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Effect = "Allow"
          Action = [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
          ]
          Resource = "*"
        }
      ]
    })
  }

  inline_policy {
    name = "WorldCup-SourcePolicy"

    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Effect = "Allow"
          Action = [
            "dynamodb:DescribeStream",
            "dynamodb:GetRecords",
            "dynamodb:GetShardIterator",
            "dynamodb:ListStreams"
          ]
          Resource = aws_dynamodb_table.WorldCup-DB.stream_arn
        }
      ]
    })
  }

  inline_policy {
    name = "WorldCup-ExecuteSFN"

    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Effect = "Allow"
          Action = "states:StartExecution"
          Resource = aws_sfn_state_machine.WorldCup-SF_machine.arn
        }
      ]
    })
  }
}

#################################################################
# Outputs
#################################################################
# Displaying the values
output "DynamoDBSourceTableName" {
  description = "DynamoDB Table Name"
  value       = aws_dynamodb_table.WorldCup-DB.name
}

output "SFNLog" {
  description = "StepFunctions LogGroup Name"
  value       = aws_cloudwatch_log_group.WorldCup-SF_LogGroup.name
}
