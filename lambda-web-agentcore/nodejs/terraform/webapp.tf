# ---------------------------------------------------------------------------------------------
# Web app: an Express server on an AWS Lambda Web Function that serves the chat UI and streams
# the agent's response to the browser.
# ---------------------------------------------------------------------------------------------

locals {
  webapp_src_dir = abspath("${path.module}/webapp")
}

# Install production dependencies into webapp/node_modules before the code is zipped. Runs again
# when package.json changes, or when node_modules is missing (for example after a fresh clone).
resource "terraform_data" "webapp_dependencies" {
  triggers_replace = [
    filesha256("${local.webapp_src_dir}/package.json"),
    fileexists("${local.webapp_src_dir}/node_modules/.package-lock.json"),
  ]

  provisioner "local-exec" {
    working_dir = local.webapp_src_dir
    command     = "npm install --omit=dev --no-audit --no-fund"
  }
}

data "archive_file" "webapp" {
  type        = "zip"
  source_dir  = local.webapp_src_dir
  output_path = "${local.build_dir}/webapp.zip"

  depends_on = [terraform_data.webapp_dependencies]
}

resource "aws_s3_object" "webapp" {
  bucket      = aws_s3_bucket.code.bucket
  key         = "webapp.zip"
  source      = data.archive_file.webapp.output_path
  source_hash = data.archive_file.webapp.output_base64sha256

  depends_on = [aws_s3_bucket_versioning.code]
}

# Lambda reads the Web Function code as the service principal, not as the execution role.
# Scoped to this account to avoid the confused deputy problem.
resource "aws_s3_bucket_policy" "code" {
  bucket = aws_s3_bucket.code.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = ["s3:GetObject", "s3:GetObjectVersion"]
      Resource  = "${aws_s3_bucket.code.arn}/${aws_s3_object.webapp.key}"
      Condition = { StringEquals = { "aws:SourceAccount" = local.account_id } }
    }]
  })

  depends_on = [aws_s3_bucket_public_access_block.code]
}

resource "aws_iam_role" "webapp" {
  name = "${local.name}-webapp"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Action    = "sts:AssumeRole"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy" "webapp" {
  role = aws_iam_role.webapp.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        # Lambda writes logs to a ".local" log group in each Region that serves traffic and
        # centralizes them into the function log group in the home Region.
        Sid    = "WebFunctionLogs"
        Effect = "Allow"
        Action = ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"]
        Resource = [
          "arn:${local.partition}:logs:${local.region}:${local.account_id}:log-group:/aws/lambda/web/${local.name}:*",
          "arn:${local.partition}:logs:*:${local.account_id}:log-group:/aws/lambda/web/${local.name}.local:*",
        ]
      },
      {
        Sid    = "InvokeThisAgent"
        Effect = "Allow"
        Action = "bedrock-agentcore:InvokeAgentRuntime"
        Resource = [
          aws_bedrockagentcore_agent_runtime.agent.agent_runtime_arn,
          "${aws_bedrockagentcore_agent_runtime.agent.agent_runtime_arn}/*",
        ]
      },
    ]
  })
}

resource "time_sleep" "webapp_role" {
  create_duration = "15s"
  triggers        = { role_arn = aws_iam_role.webapp.arn }
  depends_on      = [aws_iam_role_policy.webapp]
}

# CloudFront adds this header to every request it forwards. The web app rejects requests that do
# not carry it, so the Web Function endpoint cannot be used to bypass CloudFront.
resource "random_password" "origin_verify" {
  length  = 48
  special = false
}

# The stack owns the Web Function log groups, so they get a retention period and are deleted with
# the stack. Lambda writes to the ".local" group in the Region that serves the request and
# centralizes the events into the main group.
resource "aws_cloudwatch_log_group" "webapp" {
  for_each = {
    home  = "/aws/lambda/web/${local.name}"
    local = "/aws/lambda/web/${local.name}.local"
  }
  name              = each.value
  retention_in_days = var.log_retention_days
}

resource "awscc_lambda_web_function" "webapp" {
  function_name = local.name
}

# Revisions are immutable, so a code or configuration change creates a new revision.
# create_before_destroy lets the endpoint move to the new revision before the old one is deleted.
resource "awscc_lambda_web_function_revision" "webapp" {
  function_name = awscc_lambda_web_function.webapp.function_name

  build_config = {
    code_config = {
      s3_object = {
        bucket     = aws_s3_object.webapp.bucket
        key        = aws_s3_object.webapp.key
        version_id = aws_s3_object.webapp.version_id
      }
    }
    runtime_config = {
      runtime = "nodejs24.x"
    }
  }

  service_config = {
    execution_role_arn = time_sleep.webapp_role.triggers["role_arn"]
    # A streamed response lasts as long as the request timeout, so leave room for long answers.
    timeout_seconds = 300
    environment_variables = {
      AGENT_RUNTIME_ARN    = aws_bedrockagentcore_agent_runtime.agent.agent_runtime_arn
      ORIGIN_VERIFY_SECRET = random_password.origin_verify.result
    }
  }

  depends_on = [aws_s3_bucket_policy.code, aws_cloudwatch_log_group.webapp]

  lifecycle {
    create_before_destroy = true
  }
}

resource "awscc_lambda_web_function_endpoint" "webapp" {
  function_name = awscc_lambda_web_function.webapp.function_name
  endpoint_name = "default"
  endpoint_type = "HomeRegion"
  # The app authorizes requests itself (the CloudFront origin header). See README for adding sign-in.
  auth_type = "ApplicationManaged"

  throttle_config = { rate_limit = var.rate_limit }
  scaling_config  = { max_environments = var.max_environments }

  revision_weights = [{
    revision_id = awscc_lambda_web_function_revision.webapp.revision_id
    weight      = 100
  }]
}
