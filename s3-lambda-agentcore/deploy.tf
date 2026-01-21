provider "aws" {
  region = var.aws_region
}

data "aws_region" "current" {}
data "aws_caller_identity" "current" {}
locals {
  region                 = data.aws_region.current.region
  account_id             = data.aws_caller_identity.current.account_id
  ecr_base_arn           = "${local.account_id}.dkr.ecr.${local.region}.amazonaws.com"
}

resource "random_id" "rand" {
  keepers = {
    first = "${timestamp()}"
  }     
  byte_length = 8
}

##################
### AgentCore ####
##################

# AgentCore IAM
data "aws_iam_policy_document" "agentcore_assume_role_policy" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["bedrock-agentcore.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "agentcore_permissions_policy" {
  statement {
    actions   = ["ecr:GetAuthorizationToken"]
    effect    = "Allow"
    resources = ["*"]
  }
  statement {
    actions = [
      "ecr:BatchGetImage",
      "ecr:GetDownloadUrlForLayer"
    ]
    effect    = "Allow"
    resources = [aws_ecr_repository.agentcore_repo.arn]
  }
statement {
  actions = [
    "logs:CreateLogGroup",
    "logs:CreateLogStream",
    "logs:PutLogEvents",
  ]
  effect    = "Allow"
  resources = [
    "arn:aws:logs:${local.region}:${local.account_id}:log-group:/aws/bedrock-agentcore/*",
    "arn:aws:logs:${local.region}:${local.account_id}:log-group:/aws/bedrock-agentcore/*:log-stream:*"
  ]
}
  statement {
    actions = [
      "xray:PutTraceSegments",
      "xray:PutTelemetryRecords"
    ]
    effect    = "Allow"
    resources = ["*"]
  }
statement {
  actions = [
    "bedrock:InvokeModel",
    "bedrock:InvokeModelWithResponseStream"
  ]
  effect    = "Allow"
  resources = [
    "arn:aws:bedrock:${local.region}::foundation-model/amazon.nova-pro-v1"
  ]
}
  statement {
  actions = [
    "s3:GetObject"
  ]
  effect    = "Allow"
  resources = [
    "${aws_s3_bucket.input_bucket.arn}/*"
  ]
}
statement {
  actions = [
    "s3:ListBucket"
  ]
  effect    = "Allow"
  resources = [
    aws_s3_bucket.input_bucket.arn
  ]
}

resource "aws_iam_role" "agentcore_role" {
  name               = "serverlessland-s3-lambda-agentcore-agentcore-role"
  assume_role_policy = data.aws_iam_policy_document.agentcore_assume_role_policy.json
}

resource "aws_iam_role_policy" "agentcore_role_policy" {
  role   = aws_iam_role.agentcore_role.id
  policy = data.aws_iam_policy_document.agentcore_permissions_policy.json
}

# Agent code repo
resource "aws_ecr_repository" "agentcore_repo" {
  name                 = "serverlessland-s3-lambda-agentcore-repo"
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = true
  }
  force_delete = true
}

# Build and push agent code
resource "null_resource" "agentcore_code" {
  depends_on = [aws_ecr_repository.agentcore_repo]
  triggers   = { always_run = "${random_id.rand.hex}" }
  provisioner "local-exec" {
    command = "bash ${path.module}/bin/build.sh ${local.ecr_base_arn} ${path.module}/agent ${aws_ecr_repository.agentcore_repo.name} ${aws_ecr_repository.agentcore_repo.repository_url} ${local.region}"
  }
}

# Agentcore runtime
resource "aws_bedrockagentcore_agent_runtime" "agentcore_runtime" {
  agent_runtime_name = substr("serverlessland_s3_lambda_agentcore_agent_${random_id.rand.hex}", 0, 47)
  role_arn           = aws_iam_role.agentcore_role.arn

  agent_runtime_artifact {
    container_configuration {
      container_uri = "${aws_ecr_repository.agentcore_repo.repository_url}:latest"
    }
  }
  network_configuration {
    network_mode = "PUBLIC"
  }
  environment_variables = {
    LOG_LEVEL = "INFO"
  }
  depends_on = [null_resource.agentcore_code]
}

###########
### S3 ####
###########

# Input Bucket
resource "aws_s3_bucket" "input_bucket" {
    bucket = "serverlessland-s3-lambda-agentcore-input-${data.aws_caller_identity.current.account_id}"
    force_destroy = true 
}

# Output Bucket
resource "aws_s3_bucket" "output_bucket" {
    bucket = "serverlessland-s3-lambda-agentcore-output-${data.aws_caller_identity.current.account_id}"
    force_destroy = true 
}

# Lambda permission for S3 to invoke
resource "aws_lambda_permission" "allow_s3" {
  statement_id  = "AllowS3Invoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.s3_agent_lambda_function.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.input_bucket.arn
}

##############
### Lambda ###
##############

# Lambda IAM
data "aws_iam_policy_document" "lambda_assume_role_policy" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "lambda_permissions_policy" {
  statement {
    actions   = ["ecr:GetAuthorizationToken"]
    effect    = "Allow"
    resources = ["*"]
  }
statement {
  actions = [
    "logs:CreateLogGroup",
    "logs:CreateLogStream",
    "logs:PutLogEvents"
  ]
  effect    = "Allow"
  resources = [
    "arn:aws:logs:${local.region}:${local.account_id}:log-group:/aws/lambda/${aws_lambda_function.s3_agent_lambda_function.function_name}:*"
  ]
}
statement {
  actions = [
    "s3:GetObject"
  ]
  effect    = "Allow"
  resources = [
    "${aws_s3_bucket.input_bucket.arn}/*"
  ]
}
statement {
  actions = [
    "s3:PutObject"
  ]
  effect    = "Allow"
  resources = [
    "${aws_s3_bucket.output_bucket.arn}/*"
  ]
}
statement {
  actions = [
    "bedrock-agentcore:InvokeAgentRuntime"
  ]
  effect    = "Allow"
  resources = [
    aws_bedrockagentcore_agent_runtime.agentcore_runtime.agent_runtime_arn
  ]
}

resource "aws_iam_role" "lambda_role" {
  name               = "serverlessland-s3-lambda-agentcore-lambda-role"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume_role_policy.json
}

resource "aws_iam_role_policy" "lambda_role_policy" {
  role   = aws_iam_role.lambda_role.id
  policy = data.aws_iam_policy_document.lambda_permissions_policy.json
}

# Lambda Code
data "archive_file" "zip" {
  type        = "zip"
  source_file = "lambda/invoke_agent.py"
  output_path = "lambda/invoke_agent.zip"
}

# Lambda Function
resource "aws_lambda_function" "s3_agent_lambda_function" {
  function_name    = "serverlessland-s3-lambda-agentcore-func-${random_id.rand.hex}"
  role             = aws_iam_role.lambda_role.arn
  handler          = "invoke_agent.lambda_handler"
  runtime          = "python3.14"
timeout          = 300  # 5 minutes for agent processing
  filename         = data.archive_file.zip.output_path
  source_code_hash = data.archive_file.zip.output_base64sha256
  environment {
    variables = {
      AGENT_ARN = aws_bedrockagentcore_agent_runtime.agentcore_runtime.agent_runtime_arn
      OUTPUT_BUCKET = aws_s3_bucket.output_bucket.id
    }
  }
}

# S3->Lambda Trigger
resource "aws_s3_bucket_notification" "aws-lambda-trigger" {
  bucket = aws_s3_bucket.input_bucket.id
  lambda_function {
    lambda_function_arn = aws_lambda_function.s3_agent_lambda_function.arn
    events              = ["s3:ObjectCreated:*"]
  }
  depends_on = [aws_lambda_permission.allow_s3]
}