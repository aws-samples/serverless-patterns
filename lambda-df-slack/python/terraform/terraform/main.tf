########################################
# Terraform Configuration & Providers
########################################

terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.4"
    }
    null = {
      source  = "hashicorp/null"
      version = "~> 3.0"
    }
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project   = var.prefix
      ManagedBy = "terraform"
    }
  }
}

data "aws_caller_identity" "current" {}

########################################
# Variables
########################################

variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-2"
}


variable "prefix" {
  description = "Prefix for all resource names"
  type        = string
}

variable "slack_bot_token" {
  description = "Slack Bot User OAuth Token (xoxb-...)"
  type        = string
  sensitive   = true
}

variable "slack_signing_secret" {
  description = "Slack App Signing Secret"
  type        = string
  sensitive   = true
}


variable "lambda_runtime" {
  description = "Lambda runtime version"
  type        = string
  default     = "python3.13"
}

variable "lambda_timeout" {
  description = "Lambda function timeout in seconds"
  type        = number
  default     = 60
}

variable "lambda_memory_size" {
  description = "Lambda function memory size in MB"
  type        = number
  default     = 512
}

variable "orchestrator_timeout" {
  description = "Orchestrator Lambda timeout in seconds"
  type        = number
  default     = 900
}

variable "durable_execution_timeout" {
  description = "Durable execution timeout in seconds"
  type        = number
  default     = 3600
}

variable "durable_retention_days" {
  description = "Durable execution history retention in days"
  type        = number
  default     = 7
}

variable "bedrock_model_id" {
  description = "Bedrock model ID for Claude"
  type        = string
  default     = "us.anthropic.claude-sonnet-4-6"
}

variable "dynamodb_billing_mode" {
  description = "DynamoDB billing mode"
  type        = string
  default     = "PAY_PER_REQUEST"
}

variable "enable_xray_tracing" {
  description = "Enable AWS X-Ray tracing"
  type        = bool
  default     = false
}

variable "log_retention_days" {
  description = "CloudWatch Logs retention period in days"
  type        = number
  default     = 7
}

########################################
# Locals
########################################

locals {
  name_prefix       = var.prefix
  lambda_source_dir = "${path.module}/../src"

  common_lambda_env = {
    SLACK_SECRETS_ARN    = aws_secretsmanager_secret.slack_secrets.arn
    BEDROCK_MODEL_ID     = var.bedrock_model_id
    BEDROCK_REGION       = var.aws_region
    AGENT_RUNTIME_ARN    = try(trimspace(data.local_file.agent_runtime_arn.content), "")
    CALLBACKS_TABLE_NAME = aws_dynamodb_table.callbacks.name
  }

  common_tags = {
    Project = var.prefix
  }
}

########################################
# DynamoDB - Callbacks Table
########################################

resource "aws_dynamodb_table" "callbacks" {
  name         = "${local.name_prefix}-callbacks"
  billing_mode = var.dynamodb_billing_mode
  hash_key     = "user_id"
  range_key    = "step"

  attribute {
    name = "user_id"
    type = "S"
  }

  attribute {
    name = "step"
    type = "S"
  }

  ttl {
    attribute_name = "ttl"
    enabled        = true
  }

  server_side_encryption {
    enabled = true
  }

  tags = merge(
    local.common_tags,
    {
      Name = "${local.name_prefix}-callbacks"
    }
  )
}

########################################
# Secrets Manager - Slack Secrets
########################################

resource "aws_secretsmanager_secret" "slack_secrets" {
  name                    = "${local.name_prefix}-slack-secrets"
  description             = "Slack bot token and signing secret for the travel assistant"
  recovery_window_in_days = 0

  tags = local.common_tags
}

resource "aws_secretsmanager_secret_version" "slack_secrets" {
  secret_id = aws_secretsmanager_secret.slack_secrets.id
  secret_string = jsonencode({
    SLACK_BOT_TOKEN      = var.slack_bot_token
    SLACK_SIGNING_SECRET = var.slack_signing_secret
  })
}

########################################
# IAM Roles & Policies
########################################

# Slack Handler Role
resource "aws_iam_role" "slack_handler_role" {
  name = "${local.name_prefix}-slack-handler-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })

  tags = local.common_tags
}

# Orchestrator Role
resource "aws_iam_role" "orchestrator_role" {
  name = "${local.name_prefix}-orchestrator-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })

  tags = local.common_tags
}

# CloudWatch Logs
resource "aws_iam_role_policy_attachment" "slack_handler_logs" {
  role       = aws_iam_role.slack_handler_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy_attachment" "orchestrator_logs" {
  role       = aws_iam_role.orchestrator_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Durable Execution Policy
resource "aws_iam_role_policy_attachment" "orchestrator_durable_execution" {
  role       = aws_iam_role.orchestrator_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicDurableExecutionRolePolicy"
}

# Bedrock & AgentCore Access
resource "aws_iam_role_policy" "orchestrator_bedrock" {
  name = "${local.name_prefix}-orchestrator-bedrock"
  role = aws_iam_role.orchestrator_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = ["bedrock:InvokeModel"]
        Resource = [
          "arn:aws:bedrock:*::foundation-model/anthropic.claude-*",
          "arn:aws:bedrock:*:*:inference-profile/*"
        ]
      },
      {
        Effect   = "Allow"
        Action   = ["bedrock-agentcore:InvokeAgentRuntime"]
        Resource = [try(trimspace(data.local_file.agent_runtime_arn.content), "*")]
      },
      {
        Effect   = "Allow"
        Action   = ["dynamodb:PutItem"]
        Resource = aws_dynamodb_table.callbacks.arn
      }
    ]
  })
}

# Lambda Invoke Permission
resource "aws_iam_role_policy" "slack_handler_invoke" {
  name = "${local.name_prefix}-slack-handler-invoke"
  role = aws_iam_role.slack_handler_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = ["lambda:InvokeFunction"]
      Resource = [
        aws_lambda_function.orchestrator.arn,
        "${aws_lambda_function.orchestrator.arn}:*"
      ]
    }]
  })
}

# Durable Execution Callback Permissions
resource "aws_iam_role_policy" "slack_handler_callback" {
  name = "${local.name_prefix}-slack-handler-callback"
  role = aws_iam_role.slack_handler_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "lambda:SendDurableExecutionCallbackSuccess",
          "lambda:SendDurableExecutionCallbackFailure",
          "lambda:SendDurableExecutionCallbackHeartbeat"
        ]
        Resource = [
          aws_lambda_function.orchestrator.arn,
          "${aws_lambda_function.orchestrator.arn}:*"
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "dynamodb:GetItem",
          "dynamodb:PutItem",
          "dynamodb:DeleteItem",
          "dynamodb:Query"
        ]
        Resource = aws_dynamodb_table.callbacks.arn
      }
    ]
  })
}

# Secrets Manager Access
resource "aws_iam_role_policy" "slack_handler_secrets" {
  name = "${local.name_prefix}-slack-handler-secrets"
  role = aws_iam_role.slack_handler_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["secretsmanager:GetSecretValue"]
      Resource = [aws_secretsmanager_secret.slack_secrets.arn]
    }]
  })
}

resource "aws_iam_role_policy" "orchestrator_secrets" {
  name = "${local.name_prefix}-orchestrator-secrets"
  role = aws_iam_role.orchestrator_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["secretsmanager:GetSecretValue"]
      Resource = [aws_secretsmanager_secret.slack_secrets.arn]
    }]
  })
}

# X-Ray Tracing
resource "aws_iam_role_policy_attachment" "slack_handler_xray" {
  count      = var.enable_xray_tracing ? 1 : 0
  role       = aws_iam_role.slack_handler_role.name
  policy_arn = "arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess"
}

resource "aws_iam_role_policy_attachment" "orchestrator_xray" {
  count      = var.enable_xray_tracing ? 1 : 0
  role       = aws_iam_role.orchestrator_role.name
  policy_arn = "arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess"
}

########################################
# Lambda Functions
########################################

# Build Lambda deployment package (install deps + copy source)
resource "null_resource" "lambda_build" {
  triggers = {
    source_hash       = sha1(join("", [for f in fileset("${path.module}/../src", "**/*.py") : filemd5("${path.module}/../src/${f}")]))
    requirements_hash = filemd5("${path.module}/../requirements.txt")
    build_script_hash = filemd5("${path.module}/build.sh")
  }

  provisioner "local-exec" {
    command = "bash ${path.module}/build.sh"
  }
}

# Create deployment package from build directory
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "${path.module}/build"
  output_path = "${path.module}/lambda_deployment.zip"

  depends_on = [null_resource.lambda_build]
}

# CloudWatch Log Groups
resource "aws_cloudwatch_log_group" "slack_handler" {
  name              = "/aws/lambda/${local.name_prefix}-slack-handler"
  retention_in_days = var.log_retention_days
  tags              = local.common_tags
}

resource "aws_cloudwatch_log_group" "orchestrator" {
  name              = "/aws/lambda/${local.name_prefix}-orchestrator"
  retention_in_days = var.log_retention_days
  tags              = local.common_tags
}

# Lambda Function: Slack Handler
resource "aws_lambda_function" "slack_handler" {
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = "${local.name_prefix}-slack-handler"
  role             = aws_iam_role.slack_handler_role.arn
  handler          = "slack_handler.lambda_handler"
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  runtime          = var.lambda_runtime
  timeout          = var.lambda_timeout
  memory_size      = var.lambda_memory_size

  environment {
    variables = merge(
      local.common_lambda_env,
      {
        ORCHESTRATOR_FUNCTION_ARN = "${aws_lambda_function.orchestrator.arn}:live"
      }
    )
  }

  tracing_config {
    mode = var.enable_xray_tracing ? "Active" : "PassThrough"
  }

  depends_on = [aws_cloudwatch_log_group.slack_handler]
  tags       = local.common_tags
}

# Lambda Function: Orchestrator (Durable)
resource "aws_lambda_function" "orchestrator" {
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = "${local.name_prefix}-orchestrator"
  role             = aws_iam_role.orchestrator_role.arn
  handler          = "orchestrator.lambda_handler"
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  runtime          = var.lambda_runtime
  timeout          = var.orchestrator_timeout
  memory_size      = var.lambda_memory_size
  publish          = true

  environment {
    variables = local.common_lambda_env
  }

  logging_config {
    log_format            = "JSON"
    system_log_level      = "INFO"
    application_log_level = "INFO"
  }

  tracing_config {
    mode = var.enable_xray_tracing ? "Active" : "PassThrough"
  }

  depends_on = [
    aws_cloudwatch_log_group.orchestrator,
    aws_iam_role_policy_attachment.orchestrator_durable_execution
  ]

  tags = local.common_tags

  lifecycle {
    ignore_changes = [source_code_hash]
  }
}

# Make function DURABLE via AWS CLI
resource "null_resource" "make_durable" {
  depends_on = [aws_lambda_function.orchestrator]

  triggers = {
    function_name     = aws_lambda_function.orchestrator.function_name
    source_code_hash  = data.archive_file.lambda_zip.output_base64sha256
    execution_timeout = var.durable_execution_timeout
    retention_days    = var.durable_retention_days
    role_arn          = aws_iam_role.orchestrator_role.arn
    timeout           = var.orchestrator_timeout
    memory_size       = var.lambda_memory_size
    runtime           = var.lambda_runtime
    region            = var.aws_region
    bedrock_model_id  = var.bedrock_model_id
    prefix            = var.prefix
    callbacks_table   = aws_dynamodb_table.callbacks.name
  }

  provisioner "local-exec" {
    command = <<-EOT
      set -e

      FUNCTION_NAME="${aws_lambda_function.orchestrator.function_name}"
      echo "🔧 Making function DURABLE: $FUNCTION_NAME"

      # Check AWS CLI supports durable functions
      if ! aws lambda create-function help 2>&1 | grep -q "durable-config"; then
        echo "❌ AWS CLI DOES NOT SUPPORT DURABLE FUNCTIONS"
        echo "Your AWS CLI version: $(aws --version)"
        echo "Lambda Durable Functions require AWS CLI v2.30.0+"
        exit 1
      fi

      # Check if already durable
      CURRENT_TIMEOUT=$(aws lambda get-function-configuration \
        --function-name "$FUNCTION_NAME" \
        --query 'DurableConfig.ExecutionTimeout' \
        --output text \
        --region ${var.aws_region} 2>/dev/null || echo "None")

      if [ "$CURRENT_TIMEOUT" = "${var.durable_execution_timeout}" ]; then
        echo "✅ Function is already DURABLE"
        exit 0
      fi

      echo "⚠️  Function is STANDARD - recreating as DURABLE..."

      # Delete alias if exists
      aws lambda delete-alias \
        --function-name "$FUNCTION_NAME" \
        --name live \
        --region ${var.aws_region} 2>/dev/null || true

      # Delete function
      aws lambda delete-function \
        --function-name "$FUNCTION_NAME" \
        --region ${var.aws_region}

      echo "Waiting for deletion..."
      sleep 10

      # Write environment variables to a temp file to avoid secrets in command line
      cat > /tmp/lambda-env-vars.json <<EOF
      {"Variables":{"SLACK_SECRETS_ARN":"${aws_secretsmanager_secret.slack_secrets.arn}","BEDROCK_MODEL_ID":"${var.bedrock_model_id}","BEDROCK_REGION":"${var.aws_region}","AGENT_RUNTIME_ARN":"${try(trimspace(data.local_file.agent_runtime_arn.content), "")}","CALLBACKS_TABLE_NAME":"${aws_dynamodb_table.callbacks.name}"}}
EOF

      # Recreate with durable config
      CREATE_OUTPUT=$(aws lambda create-function \
        --function-name "$FUNCTION_NAME" \
        --runtime ${var.lambda_runtime} \
        --role ${aws_iam_role.orchestrator_role.arn} \
        --handler orchestrator.lambda_handler \
        --zip-file fileb://${data.archive_file.lambda_zip.output_path} \
        --timeout ${var.orchestrator_timeout} \
        --memory-size ${var.lambda_memory_size} \
        --durable-config ExecutionTimeout=${var.durable_execution_timeout},RetentionPeriodInDays=${var.durable_retention_days} \
        --logging-config LogFormat=JSON,SystemLogLevel=INFO,ApplicationLogLevel=INFO \
        --environment file:///tmp/lambda-env-vars.json \
        --publish \
        --region ${var.aws_region})

      # Clean up temp file
      rm -f /tmp/lambda-env-vars.json

      # Get the published version
      VERSION=$(echo "$CREATE_OUTPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('Version','1'))")
      echo "✓ Durable function created! Version: $VERSION"

      # Wait for active
      aws lambda wait function-active-v2 \
        --function-name "$FUNCTION_NAME" \
        --region ${var.aws_region}

      # Create alias pointing to the published version
      aws lambda create-alias \
        --function-name "$FUNCTION_NAME" \
        --name live \
        --function-version "$VERSION" \
        --description "Live alias for durable function orchestrator" \
        --region ${var.aws_region} > /dev/null

      echo "✓ Alias 'live' created"

      # Verify
      echo "✅ Durable Config:"
      aws lambda get-function-configuration \
        --function-name "$FUNCTION_NAME" \
        --query 'DurableConfig' \
        --region ${var.aws_region}
    EOT
  }
}

# Lambda Permissions
resource "aws_lambda_permission" "api_gateway" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.slack_handler.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.slack_api.execution_arn}/*/*"
}

resource "aws_lambda_permission" "slack_invoke_orchestrator" {
  statement_id  = "AllowSlackHandlerInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.orchestrator.function_name
  principal     = "lambda.amazonaws.com"
  source_arn    = aws_lambda_function.slack_handler.arn
  qualifier     = "live"

  depends_on = [null_resource.make_durable]
}

########################################
# API Gateway
########################################

resource "aws_api_gateway_rest_api" "slack_api" {
  name        = "${local.name_prefix}-api"
  description = "API Gateway for Slack webhooks"

  endpoint_configuration {
    types = ["REGIONAL"]
  }

  tags = local.common_tags
}

resource "aws_api_gateway_resource" "slack" {
  rest_api_id = aws_api_gateway_rest_api.slack_api.id
  parent_id   = aws_api_gateway_rest_api.slack_api.root_resource_id
  path_part   = "slack"
}

resource "aws_api_gateway_resource" "events" {
  rest_api_id = aws_api_gateway_rest_api.slack_api.id
  parent_id   = aws_api_gateway_resource.slack.id
  path_part   = "events"
}

resource "aws_api_gateway_method" "post_events" {
  rest_api_id   = aws_api_gateway_rest_api.slack_api.id
  resource_id   = aws_api_gateway_resource.events.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "lambda" {
  rest_api_id             = aws_api_gateway_rest_api.slack_api.id
  resource_id             = aws_api_gateway_resource.events.id
  http_method             = aws_api_gateway_method.post_events.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.slack_handler.invoke_arn
}

resource "aws_api_gateway_method_response" "response_200" {
  rest_api_id = aws_api_gateway_rest_api.slack_api.id
  resource_id = aws_api_gateway_resource.events.id
  http_method = aws_api_gateway_method.post_events.http_method
  status_code = "200"

  response_parameters = {
    "method.response.header.Access-Control-Allow-Origin" = true
  }
}

resource "aws_api_gateway_deployment" "deployment" {
  rest_api_id = aws_api_gateway_rest_api.slack_api.id

  triggers = {
    redeployment = sha1(jsonencode([
      aws_api_gateway_resource.events.id,
      aws_api_gateway_method.post_events.id,
      aws_api_gateway_integration.lambda.id,
    ]))
  }

  lifecycle {
    create_before_destroy = true
  }

  depends_on = [aws_api_gateway_integration.lambda]
}

resource "aws_api_gateway_stage" "prod" {
  deployment_id        = aws_api_gateway_deployment.deployment.id
  rest_api_id          = aws_api_gateway_rest_api.slack_api.id
  stage_name           = "prod"
  xray_tracing_enabled = var.enable_xray_tracing

  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.api_gateway.arn
    format = jsonencode({
      requestId      = "$context.requestId"
      ip             = "$context.identity.sourceIp"
      requestTime    = "$context.requestTime"
      httpMethod     = "$context.httpMethod"
      resourcePath   = "$context.resourcePath"
      status         = "$context.status"
      protocol       = "$context.protocol"
      responseLength = "$context.responseLength"
    })
  }

  tags = local.common_tags
}

resource "aws_cloudwatch_log_group" "api_gateway" {
  name              = "/aws/apigateway/${local.name_prefix}"
  retention_in_days = var.log_retention_days
  tags              = local.common_tags
}

resource "aws_api_gateway_account" "account" {
  cloudwatch_role_arn = aws_iam_role.api_gateway_cloudwatch.arn
  reset_on_delete    = true
}

resource "aws_iam_role" "api_gateway_cloudwatch" {
  name = "${local.name_prefix}-api-gateway-cloudwatch"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "apigateway.amazonaws.com"
      }
    }]
  })

  tags = local.common_tags
}

resource "aws_iam_role_policy_attachment" "api_gateway_cloudwatch" {
  role       = aws_iam_role.api_gateway_cloudwatch.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs"
}

########################################
# AgentCore
########################################

resource "aws_ecr_repository" "agentcore_agent" {
  name                 = "${local.name_prefix}-agentcore-agent"
  image_tag_mutability = "MUTABLE"
  force_delete         = true

  image_scanning_configuration {
    scan_on_push = false
  }

  tags = local.common_tags
}

resource "null_resource" "agentcore_image_build" {
  depends_on = [aws_ecr_repository.agentcore_agent]

  triggers = {
    agent_py_hash     = filemd5("${path.module}/../agentcore-agent/agent.py")
    dockerfile_hash   = filemd5("${path.module}/../agentcore-agent/Dockerfile")
    requirements_hash = filemd5("${path.module}/../agentcore-agent/requirements.txt")
    ecr_repo_url      = aws_ecr_repository.agentcore_agent.repository_url
  }

  provisioner "local-exec" {
    command = <<-EOT
      set -e

      # Login to ECR using Finch
      aws ecr get-login-password --region ${var.aws_region} | \
        finch login --username AWS --password-stdin ${aws_ecr_repository.agentcore_agent.repository_url}

      # Build image with Finch
      cd ${path.module}/../agentcore-agent
      finch build --no-cache --platform linux/arm64 \
        -t ${aws_ecr_repository.agentcore_agent.repository_url}:latest .

      # Push to ECR
      finch push ${aws_ecr_repository.agentcore_agent.repository_url}:latest

      # Save image digest
      DIGEST=$(finch images --no-trunc --format '{{.ID}}' ${aws_ecr_repository.agentcore_agent.repository_url}:latest)
      echo "$DIGEST" > ${path.module}/image_digest.txt
      echo "Image digest saved: $DIGEST"
    EOT
  }
}

resource "aws_iam_role" "agentcore_runtime" {
  name = "${local.name_prefix}-agentcore-runtime-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "bedrock-agentcore.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })

  tags = local.common_tags
}

resource "aws_iam_role_policy" "agentcore_runtime" {
  name = "${local.name_prefix}-agentcore-runtime-policy"
  role = aws_iam_role.agentcore_runtime.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "bedrock:InvokeModel",
          "bedrock:InvokeModelWithResponseStream"
        ]
        Resource = [
          "arn:aws:bedrock:*::foundation-model/anthropic.claude-*",
          "arn:aws:bedrock:*:*:inference-profile/*"
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "lambda:SendDurableExecutionCallbackSuccess",
          "lambda:SendDurableExecutionCallbackFailure",
          "lambda:SendDurableExecutionCallbackHeartbeat"
        ]
        Resource = [
          "arn:aws:lambda:${var.aws_region}:${data.aws_caller_identity.current.account_id}:function:${local.name_prefix}-orchestrator",
          "arn:aws:lambda:${var.aws_region}:${data.aws_caller_identity.current.account_id}:function:${local.name_prefix}-orchestrator:*"
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "ecr:GetAuthorizationToken"
        ]
        Resource = "*"
      },
      {
        Effect = "Allow"
        Action = [
          "ecr:BatchCheckLayerAvailability",
          "ecr:GetDownloadUrlForLayer",
          "ecr:BatchGetImage"
        ]
        Resource = [aws_ecr_repository.agentcore_agent.arn]
      },
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
          "logs:DescribeLogStreams"
        ]
        Resource = [
          "arn:aws:logs:*:*:log-group:/aws/bedrock-agentcore/runtimes/*",
          "arn:aws:logs:*:*:log-group:/aws/bedrock-agentcore/runtimes/*:*"
        ]
      }
    ]
  })
}

resource "null_resource" "agentcore_runtime" {
  depends_on = [
    null_resource.agentcore_image_build,
    aws_iam_role_policy.agentcore_runtime
  ]

  triggers = {
    image_url  = "${aws_ecr_repository.agentcore_agent.repository_url}:latest"
    runtime_id = replace("${local.name_prefix}_travel_agent", "-", "_")
    region     = var.aws_region
  }

  provisioner "local-exec" {
    command = <<-EOT
      set -e

      # Wait for IAM role to propagate
      sleep 10

      # Create AgentCore runtime
      aws bedrock-agentcore-control create-agent-runtime \
        --agent-runtime-name ${self.triggers.runtime_id} \
        --description "Travel planning agent using Strands and Bedrock" \
        --role-arn ${aws_iam_role.agentcore_runtime.arn} \
        --agent-runtime-artifact '{"containerConfiguration":{"containerUri":"${aws_ecr_repository.agentcore_agent.repository_url}:latest"}}' \
        --network-configuration '{"networkMode":"PUBLIC"}' \
        --region ${self.triggers.region} 2>&1 | tee /tmp/agentcore-create.log || true

      # Get ARN
      RUNTIME_ARN=$(aws bedrock-agentcore-control list-agent-runtimes \
        --region ${self.triggers.region} \
        --query "agentRuntimes[?agentRuntimeName=='${self.triggers.runtime_id}'].agentRuntimeArn" \
        --output text 2>/dev/null || echo "")

      if [ -z "$RUNTIME_ARN" ]; then
        echo "ERROR: Failed to create or find AgentCore runtime"
        cat /tmp/agentcore-create.log
        exit 1
      fi

      echo "$RUNTIME_ARN" > ${path.module}/agent_runtime_arn.txt
      echo "AgentCore runtime created: $RUNTIME_ARN"
    EOT
  }

  provisioner "local-exec" {
    when    = destroy
    command = <<-EOT
      set -e

      # Get runtime ID from list
      RUNTIME_ID=$(aws bedrock-agentcore-control list-agent-runtimes \
        --region ${self.triggers.region} \
        --query "agentRuntimes[?agentRuntimeName=='${self.triggers.runtime_id}'].agentRuntimeId" \
        --output text 2>/dev/null || echo "")

      if [ -n "$RUNTIME_ID" ] && [ "$RUNTIME_ID" != "None" ]; then
        echo "Deleting AgentCore runtime: $RUNTIME_ID"
        aws bedrock-agentcore-control delete-agent-runtime \
          --agent-runtime-id "$RUNTIME_ID" \
          --region ${self.triggers.region} 2>/dev/null || true
        echo "AgentCore runtime deletion initiated"
      else
        echo "No AgentCore runtime found to delete"
      fi

      rm -f ${path.module}/agent_runtime_arn.txt
    EOT
  }
}

data "local_file" "agent_runtime_arn" {
  depends_on = [null_resource.agentcore_runtime]
  filename   = "${path.module}/agent_runtime_arn.txt"
}

########################################
# Outputs
########################################

output "api_gateway_url" {
  description = "API Gateway endpoint URL for Slack webhooks"
  value       = "${aws_api_gateway_stage.prod.invoke_url}/slack/events"
}

output "api_gateway_id" {
  description = "API Gateway REST API ID"
  value       = aws_api_gateway_rest_api.slack_api.id
}

output "slack_handler_function_name" {
  description = "Slack Handler Lambda function name"
  value       = aws_lambda_function.slack_handler.function_name
}

output "orchestrator_function_name" {
  description = "Orchestrator Lambda function name"
  value       = aws_lambda_function.orchestrator.function_name
}

output "orchestrator_qualified_arn" {
  description = "Orchestrator Lambda ARN with 'live' alias"
  value       = "${aws_lambda_function.orchestrator.arn}:live"
}

output "region" {
  description = "AWS region"
  value       = var.aws_region
}

output "agentcore_runtime_arn" {
  value       = try(trimspace(data.local_file.agent_runtime_arn.content), "")
  description = "ARN of the AgentCore runtime"
}

output "deployment_instructions" {
  description = "Next steps after deployment"
  value       = <<-EOT

    ✅ Deployment Complete! Orchestrator is DURABLE ✓

    Next steps:

    1. Configure Slack Event Subscriptions:
       - Go to https://api.slack.com/apps
       - Select your app
       - Navigate to "Event Subscriptions"
       - Set Request URL to: ${aws_api_gateway_stage.prod.invoke_url}/slack/events
       - Subscribe to events: message.im, message.channels, app_mention
       - Save changes and reinstall app

    2. Test the bot:
       - Open Slack and DM your bot
       - Type: "Plan a trip for me"
       - Bot should respond and start asking questions

    3. Monitor logs:
       - Slack Handler: aws logs tail ${aws_cloudwatch_log_group.slack_handler.name} --follow --region ${var.aws_region}
       - Orchestrator: aws logs tail ${aws_cloudwatch_log_group.orchestrator.name} --follow --region ${var.aws_region}

    🎉 Your bot is ready to use!
  EOT
}
