terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.32.1"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

############################################################
# Variables
############################################################

variable "aws_region" {
  description = "AWS region for resources (e.g. us-east-1, us-west-2)"
  type        = string

  validation {
    condition     = can(regex("^[a-z]{2}-[a-z]+-[0-9]+$", var.aws_region))
    error_message = "Must be a valid AWS region (e.g. us-east-1, eu-west-2)."
  }
}

variable "prefix" {
  description = "Unique prefix for all resource names"
  type        = string

  validation {
    condition     = can(regex("^[a-z0-9][a-z0-9\\-]{1,20}$", var.prefix))
    error_message = "Prefix must be 2-21 lowercase alphanumeric characters or hyphens."
  }
}

variable "bedrock_model_id" {
  description = "Bedrock foundation model ID for the agent"
  type        = string
  default     = "anthropic.claude-3-haiku-20240307-v1:0"
}

variable "schedule_expression" {
  description = "EventBridge Scheduler expression (e.g. rate(1 hour), cron(0 9 * * ? *))"
  type        = string
  default     = "rate(1 hour)"
}

variable "log_retention_days" {
  description = "CloudWatch log retention in days (0 = never expire)"
  type        = number
  default     = 14
}

############################################################
# Data Sources
############################################################

data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

############################################################
# 1. DYNAMODB TABLE (agent writes execution records here)
############################################################

resource "aws_dynamodb_table" "task_executions" {
  name         = "${var.prefix}-agent-task-executions"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "TaskId"

  attribute {
    name = "TaskId"
    type = "S"
  }

  tags = {
    Project = "${var.prefix}-ai-agent-scheduler"
  }
}

############################################################
# 2. ACTION GROUP LAMBDA (Bedrock Agent calls this to
#    read/write DynamoDB)
############################################################

resource "aws_iam_role" "action_group_role" {
  name = "${var.prefix}-action-group-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "action_group_basic" {
  role       = aws_iam_role.action_group_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy" "action_group_dynamodb" {
  name = "${var.prefix}-action-group-dynamodb"
  role = aws_iam_role.action_group_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "dynamodb:PutItem",
        "dynamodb:GetItem",
        "dynamodb:UpdateItem",
        "dynamodb:Query",
        "dynamodb:Scan"
      ]
      Resource = [
        aws_dynamodb_table.task_executions.arn,
        "${aws_dynamodb_table.task_executions.arn}/index/*"
      ]
    }]
  })
}

resource "aws_cloudwatch_log_group" "action_group_logs" {
  name              = "/aws/lambda/${var.prefix}-agent-action-group"
  retention_in_days = var.log_retention_days
}

resource "aws_lambda_function" "action_group" {
  function_name = "${var.prefix}-agent-action-group"
  role          = aws_iam_role.action_group_role.arn
  handler       = "action_group.lambda_handler"
  runtime       = "python3.14"
  timeout       = 30
  memory_size   = 128
  filename      = "action_group.zip"

  environment {
    variables = {
      DYNAMODB_TABLE = aws_dynamodb_table.task_executions.name
      PREFIX         = var.prefix
    }
  }

  depends_on = [
    aws_cloudwatch_log_group.action_group_logs,
    aws_iam_role_policy_attachment.action_group_basic,
    aws_iam_role_policy.action_group_dynamodb,
  ]
}

############################################################
# 3. BEDROCK AGENT (AI agent with action group)
############################################################

# --- Agent IAM Role ---

resource "aws_iam_role" "bedrock_agent_role" {
  name = "${var.prefix}-bedrock-agent-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "bedrock.amazonaws.com" }
      Condition = {
        StringEquals = {
          "aws:SourceAccount" = data.aws_caller_identity.current.account_id
        }
      }
    }]
  })
}

resource "aws_iam_role_policy" "bedrock_agent_model" {
  name = "${var.prefix}-bedrock-invoke-model"
  role = aws_iam_role.bedrock_agent_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "bedrock:InvokeModel"
      Resource = "arn:aws:bedrock:${var.aws_region}::foundation-model/${var.bedrock_model_id}"
    }]
  })
}

# --- Agent ---

resource "aws_bedrockagent_agent" "task_agent" {
  agent_name                  = "${var.prefix}-scheduled-task-agent"
  agent_resource_role_arn     = aws_iam_role.bedrock_agent_role.arn
  foundation_model            = var.bedrock_model_id
  idle_session_ttl_in_seconds = 600
  prepare_agent               = false # prepared after action group is attached

  instruction = <<-EOT
    You are a Scheduled Task Execution Agent. You run on a schedule via
    Amazon EventBridge Scheduler. Each time you are invoked you must:

    1. PARSE the task payload provided to you (JSON with taskType, scheduleName,
       and scheduledTime).
    2. GENERATE a brief, one-paragraph executive summary describing the task
       execution — include the task type, timestamp, and a note that the
       execution completed successfully.
    3. CALL the recordTaskExecution action to persist the execution record.
       Use the values from the payload for taskId (use scheduleName + timestamp
       combined), taskType, scheduledTime, and pass your generated summary as
       the executionSummary.
    4. CONFIRM success by returning a short completion message.

    Always use the exact values from the payload. Never fabricate timestamps
    or identifiers.
  EOT
}

# --- Action Group ---

resource "aws_bedrockagent_agent_action_group" "task_actions" {
  action_group_name          = "${var.prefix}-task-execution-actions"
  agent_id                   = aws_bedrockagent_agent.task_agent.agent_id
  agent_version              = "DRAFT"
  skip_resource_in_use_check = true

  action_group_executor {
    lambda = aws_lambda_function.action_group.arn
  }

  api_schema {
    payload = file("${path.module}/api_schema.json")
  }
}

# --- Allow Bedrock to invoke Action Group Lambda ---

resource "aws_lambda_permission" "allow_bedrock" {
  statement_id  = "AllowBedrockAgentInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.action_group.function_name
  principal     = "bedrock.amazonaws.com"
  source_arn    = aws_bedrockagent_agent.task_agent.agent_arn
}

# --- Prepare Agent (must happen after action group is attached) ---

resource "terraform_data" "prepare_agent" {
  depends_on = [
    aws_bedrockagent_agent_action_group.task_actions,
    aws_lambda_permission.allow_bedrock,
  ]

  triggers_replace = [
    aws_bedrockagent_agent.task_agent.agent_id,
    aws_bedrockagent_agent_action_group.task_actions.action_group_name,
  ]

  provisioner "local-exec" {
    command = "aws bedrock-agent prepare-agent --agent-id ${aws_bedrockagent_agent.task_agent.agent_id} --region ${var.aws_region} && sleep 15"
  }
}

# --- Agent Alias (points to the prepared version) ---

resource "aws_bedrockagent_agent_alias" "live" {
  agent_alias_name = "${var.prefix}-live"
  agent_id         = aws_bedrockagent_agent.task_agent.agent_id
  description      = "Live alias for scheduled task agent"

  depends_on = [terraform_data.prepare_agent]
}

############################################################
# 4. ORCHESTRATOR LAMBDA (Scheduler invokes this →
#    it invokes the Bedrock Agent)
############################################################

resource "aws_iam_role" "orchestrator_role" {
  name = "${var.prefix}-orchestrator-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "orchestrator_basic" {
  role       = aws_iam_role.orchestrator_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# ── InvokeAgent requires permission on the agent ALIAS ARN ──
# ARN format: arn:aws:bedrock:{region}:{account}:agent-alias/{agent-id}/{alias-id}
# The alias resource exposes this as agent_alias_arn.
# We also grant access to all aliases of this agent so the role
# continues to work if a new alias is created later.

resource "aws_iam_role_policy" "orchestrator_bedrock" {
  name = "${var.prefix}-orchestrator-invoke-agent"
  role = aws_iam_role.orchestrator_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid    = "InvokeBedrockAgentAlias"
      Effect = "Allow"
      Action = "bedrock:InvokeAgent"
      Resource = [
        # Specific alias created by this stack
        aws_bedrockagent_agent_alias.live.agent_alias_arn,
        # Wildcard for any future alias of the same agent
        "arn:aws:bedrock:${var.aws_region}:${data.aws_caller_identity.current.account_id}:agent-alias/${aws_bedrockagent_agent.task_agent.agent_id}/*"
      ]
    }]
  })
}

resource "aws_cloudwatch_log_group" "orchestrator_logs" {
  name              = "/aws/lambda/${var.prefix}-agent-orchestrator"
  retention_in_days = var.log_retention_days
}

resource "aws_lambda_function" "orchestrator" {
  function_name = "${var.prefix}-agent-orchestrator"
  role          = aws_iam_role.orchestrator_role.arn
  handler       = "orchestrator.lambda_handler"
  runtime       = "python3.14"
  timeout       = 120
  memory_size   = 256
  filename      = "orchestrator.zip"

  environment {
    variables = {
      BEDROCK_AGENT_ID       = aws_bedrockagent_agent.task_agent.agent_id
      BEDROCK_AGENT_ALIAS_ID = aws_bedrockagent_agent_alias.live.agent_alias_id
      PREFIX                 = var.prefix
    }
  }

  depends_on = [
    aws_cloudwatch_log_group.orchestrator_logs,
    aws_iam_role_policy_attachment.orchestrator_basic,
    aws_iam_role_policy.orchestrator_bedrock,
  ]
}

############################################################
# 5. SQS DEAD-LETTER QUEUE (captures failed scheduler
#    invocations after retries are exhausted)
############################################################

resource "aws_sqs_queue" "scheduler_dlq" {
  name                      = "${var.prefix}-scheduler-dlq"
  message_retention_seconds = 1209600 # 14 days
}

############################################################
# 6. EVENTBRIDGE SCHEDULER (triggers the orchestrator
#    on a recurring schedule)
############################################################

resource "aws_iam_role" "scheduler_role" {
  name = "${var.prefix}-scheduler-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "scheduler.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy" "scheduler_invoke_lambda" {
  name = "${var.prefix}-scheduler-invoke-lambda"
  role = aws_iam_role.scheduler_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid      = "InvokeLambda"
        Effect   = "Allow"
        Action   = "lambda:InvokeFunction"
        Resource = aws_lambda_function.orchestrator.arn
      },
      {
        Sid      = "SendToDLQ"
        Effect   = "Allow"
        Action   = "sqs:SendMessage"
        Resource = aws_sqs_queue.scheduler_dlq.arn
      }
    ]
  })
}

resource "aws_sqs_queue_policy" "allow_scheduler" {
  queue_url = aws_sqs_queue.scheduler_dlq.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid       = "AllowSchedulerSendMessage"
      Effect    = "Allow"
      Principal = { Service = "scheduler.amazonaws.com" }
      Action    = "sqs:SendMessage"
      Resource  = aws_sqs_queue.scheduler_dlq.arn
      Condition = {
        ArnEquals = {
          "aws:SourceArn" = "arn:aws:scheduler:${var.aws_region}:${data.aws_caller_identity.current.account_id}:schedule/default/${var.prefix}-trigger-ai-agent"
        }
      }
    }]
  })
}

resource "aws_cloudwatch_log_group" "scheduler_logs" {
  name              = "/aws/scheduler/${var.prefix}-trigger-ai-agent"
  retention_in_days = var.log_retention_days
}

resource "aws_scheduler_schedule" "trigger_agent" {
  name                = "${var.prefix}-trigger-ai-agent"
  schedule_expression = var.schedule_expression

  flexible_time_window {
    mode = "OFF"
  }

  target {
    arn      = aws_lambda_function.orchestrator.arn
    role_arn = aws_iam_role.scheduler_role.arn

    input = jsonencode({
      taskType      = "scheduled-report"
      scheduleName  = "${var.prefix}-trigger-ai-agent"
      scheduledTime = "REPLACED_AT_RUNTIME"
    })

    retry_policy {
      maximum_retry_attempts       = 3
      maximum_event_age_in_seconds = 3600
    }

    dead_letter_config {
      arn = aws_sqs_queue.scheduler_dlq.arn
    }
  }

  depends_on = [aws_cloudwatch_log_group.scheduler_logs]
}

############################################################
# 7. OUTPUTS
############################################################

output "prefix" {
  value = var.prefix
}

output "schedule_name" {
  value = aws_scheduler_schedule.trigger_agent.name
}

output "schedule_arn" {
  value = aws_scheduler_schedule.trigger_agent.arn
}

output "orchestrator_lambda_name" {
  value = aws_lambda_function.orchestrator.function_name
}

output "action_group_lambda_name" {
  value = aws_lambda_function.action_group.function_name
}

output "bedrock_agent_id" {
  value = aws_bedrockagent_agent.task_agent.agent_id
}

output "bedrock_agent_alias_id" {
  value = aws_bedrockagent_agent_alias.live.agent_alias_id
}

output "bedrock_agent_alias_arn" {
  value       = aws_bedrockagent_agent_alias.live.agent_alias_arn
  description = "The alias ARN that the orchestrator Lambda is authorized to invoke"
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.task_executions.name
}

output "dlq_queue_url" {
  value = aws_sqs_queue.scheduler_dlq.url
}