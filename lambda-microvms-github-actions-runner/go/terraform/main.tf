# Ephemeral GitHub Actions runners on AWS Lambda MicroVMs.
# Run ./src/microvm-runner/build.sh before terraform plan/apply.

data "aws_caller_identity" "current" {}

locals {
  account_id = data.aws_caller_identity.current.account_id

  tags = {
    Project = "lambda-microvms-github-actions-runner"
  }

  # CloudFormation requires a base image version. Bump it to pick up base-image
  # patches (aws lambda-microvms list-managed-microvm-image-versions).
  microvm_base_image_arn     = "arn:aws:lambda:${var.region}:aws:microvm-image:al2023-1"
  microvm_base_image_version = "4"

  # No leading or trailing slash. Scopes the webhook's S3 grant and the lifecycle rule.
  jit_key_prefix = "jit"

  webhook_function_name = "${var.name_prefix}-webhook"

  runner_image_name           = "${var.name_prefix}-runner-image"
  runner_image_arn_pattern    = "arn:aws:lambda:${var.region}:${local.account_id}:microvm-image:${var.name_prefix}-runner-*"
  build_log_group_arn_pattern = "arn:aws:logs:${var.region}:${local.account_id}:log-group:/aws/lambda-microvms/${var.name_prefix}-runner-*"

  supervisor_zip     = "${path.module}/src/microvm-runner/dist/supervisor.zip"
  supervisor_zip_md5 = fileexists(local.supervisor_zip) ? filemd5(local.supervisor_zip) : ""
}

# --- S3: image code artifact + per-job JIT configs ---
# A JIT config (~4.1 KB) exceeds the 4096-char run-hook-payload limit, so the VM
# gets a presigned GET URL for it instead. S3 rather than SSM: Standard
# parameters are also capped at 4 KB.

resource "aws_s3_bucket" "artifacts" {
  bucket        = "${var.name_prefix}-artifacts-${local.account_id}"
  force_destroy = true
  tags          = local.tags
}

resource "aws_s3_bucket_public_access_block" "artifacts" {
  bucket                  = aws_s3_bucket.artifacts.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_policy" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid       = "DenyInsecureTransport"
      Effect    = "Deny"
      Principal = "*"
      Action    = "s3:*"
      Resource  = [aws_s3_bucket.artifacts.arn, "${aws_s3_bucket.artifacts.arn}/*"]
      Condition = { Bool = { "aws:SecureTransport" = "false" } }
    }]
  })

  # Avoid concurrent bucket-policy / public-access-block writes (OperationAborted).
  depends_on = [aws_s3_bucket_public_access_block.artifacts]
}

resource "aws_s3_bucket_server_side_encryption_configuration" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# The VM has no S3 permissions, so nothing else deletes used JIT configs.
resource "aws_s3_bucket_lifecycle_configuration" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id

  rule {
    id     = "expire-jit-configs"
    status = "Enabled"

    filter {
      prefix = "${local.jit_key_prefix}/"
    }

    expiration {
      days = 1
    }
  }
}

# --- Secrets Manager ---
# Values are set out of band so secret material never lands in Terraform state.

resource "aws_secretsmanager_secret" "pat" {
  name = "${var.name_prefix}-github-pat"
  # Delete immediately on destroy, so a redeploy with the same name_prefix
  # doesn't collide with a secret pending deletion.
  recovery_window_in_days = 0
  tags                    = local.tags
}

resource "aws_secretsmanager_secret" "webhook" {
  name                    = "${var.name_prefix}-webhook-secret"
  recovery_window_in_days = 0
  tags                    = local.tags
}

# --- CloudWatch Logs ---
# Lambda creates the image build log group itself; Terraform doesn't manage it.

resource "aws_cloudwatch_log_group" "microvm_runtime" {
  name              = "/${var.name_prefix}/microvm-runtime"
  retention_in_days = 14
  tags              = local.tags
}

resource "aws_cloudwatch_log_group" "webhook" {
  name              = "/aws/lambda/${local.webhook_function_name}"
  retention_in_days = aws_cloudwatch_log_group.microvm_runtime.retention_in_days
  tags              = local.tags
}

# --- IAM ---
# RunMicrovm and TerminateMicrovm authorize against the microvm-image resource.

# Assumed by Lambda during image builds; the build-time /ready hook runs under it.
resource "aws_iam_role" "microvm_build" {
  name = "${var.name_prefix}-microvm-build-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = ["sts:AssumeRole", "sts:TagSession"]
    }]
  })
  tags = local.tags
}

resource "aws_iam_role_policy" "microvm_build" {
  name = "${var.name_prefix}-microvm-build-policy"
  role = aws_iam_role.microvm_build.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid      = "ReadArtifact"
        Effect   = "Allow"
        Action   = ["s3:GetObject"]
        Resource = ["${aws_s3_bucket.artifacts.arn}/supervisor-runner-*"]
      },
      {
        Sid      = "BuildLogs"
        Effect   = "Allow"
        Action   = ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"]
        Resource = [local.build_log_group_arn_pattern]
      }
    ]
  })
}

# TRUST BOUNDARY: these credentials are reachable by arbitrary CI job code
# running in the VM, not just the supervisor (see README Security).
resource "aws_iam_role" "microvm_execution" {
  name = "${var.name_prefix}-microvm-exec-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = ["sts:AssumeRole", "sts:TagSession"]
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
  tags = local.tags
}

resource "aws_iam_role_policy" "microvm_execution" {
  name = "${var.name_prefix}-microvm-exec-policy"
  role = aws_iam_role.microvm_execution.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        # There is no MicroVM-ID resource or condition key, so this is scoped to
        # the image the MicroVM was launched from.
        Sid      = "SelfTerminate"
        Effect   = "Allow"
        Action   = ["lambda:TerminateMicrovm"]
        Resource = [local.runner_image_arn_pattern]
      },
      {
        Sid      = "RuntimeLogs"
        Effect   = "Allow"
        Action   = ["logs:CreateLogStream", "logs:PutLogEvents"]
        Resource = ["${aws_cloudwatch_log_group.microvm_runtime.arn}:*"]
      }
      # No S3 access: the VM reads its JIT config through a presigned URL.
    ]
  })
}

resource "aws_iam_role" "webhook" {
  name = "${var.name_prefix}-webhook-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
  tags = local.tags
}

# Inline policy instead of AWSLambdaBasicExecutionRole, which grants logs on "*".
resource "aws_iam_role_policy" "webhook" {
  name = "${var.name_prefix}-webhook-policy"
  role = aws_iam_role.webhook.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid      = "FunctionLogs"
        Effect   = "Allow"
        Action   = ["logs:CreateLogStream", "logs:PutLogEvents"]
        Resource = ["${aws_cloudwatch_log_group.webhook.arn}:*"]
      },
      {
        Sid      = "ReadSecrets"
        Effect   = "Allow"
        Action   = ["secretsmanager:GetSecretValue"]
        Resource = [aws_secretsmanager_secret.pat.arn, aws_secretsmanager_secret.webhook.arn]
      },
      {
        Sid      = "RunMicrovm"
        Effect   = "Allow"
        Action   = ["lambda:RunMicrovm"]
        Resource = [local.runner_image_arn_pattern]
      },
      {
        Sid      = "PassMicrovmExecutionRole"
        Effect   = "Allow"
        Action   = ["iam:PassRole"]
        Resource = [aws_iam_role.microvm_execution.arn]
        Condition = {
          StringEquals = { "iam:PassedToService" = "lambda.amazonaws.com" }
        }
      },
      {
        # The AWS-managed connectors live in the "aws" account.
        Sid    = "PassNetworkConnectors"
        Effect = "Allow"
        Action = ["lambda:PassNetworkConnector"]
        Resource = [
          "arn:aws:lambda:${var.region}:aws:network-connector:aws-network-connector:NO_INGRESS",
          "arn:aws:lambda:${var.region}:aws:network-connector:aws-network-connector:INTERNET_EGRESS",
        ]
      },
      {
        # Presigning a GET URL requires the signer to hold s3:GetObject.
        Sid      = "WriteSignJitConfig"
        Effect   = "Allow"
        Action   = ["s3:PutObject", "s3:GetObject"]
        Resource = ["${aws_s3_bucket.artifacts.arn}/${local.jit_key_prefix}/*"]
      }
    ]
  })
}

# --- MicroVM runner image ---
# A one-resource CloudFormation stack: the hashicorp/aws image resource can't
# configure hooks, and hashicorp/awscc drops the empty AdditionalOsCapabilities
# list CloudFormation requires. A new zip changes the template, and the stack
# update builds a new image version under the same ARN; a failed build rolls
# back to the previous version.

# Content-addressed key: a changed zip is a new object, so a new image version.
resource "aws_s3_object" "supervisor_zip" {
  bucket      = aws_s3_bucket.artifacts.id
  key         = "supervisor-runner-${local.supervisor_zip_md5}.zip"
  source      = local.supervisor_zip
  source_hash = local.supervisor_zip_md5
  tags        = local.tags

  lifecycle {
    # Delete the old zip only after the stack update succeeds. If the new build
    # fails, the CloudFormation rollback rebuilds from the old zip's URI.
    create_before_destroy = true

    precondition {
      condition     = local.supervisor_zip_md5 != ""
      error_message = "src/microvm-runner/dist/supervisor.zip not found: run ./src/microvm-runner/build.sh first."
    }
  }
}

resource "aws_cloudformation_stack" "microvm_image" {
  name = "${var.name_prefix}-microvm-image"
  # Only applies to a failed first create; a failed update rolls back.
  on_failure = "DELETE"
  tags       = local.tags

  template_body = jsonencode({
    AWSTemplateFormatVersion = "2010-09-09"
    Description              = "Lambda MicroVM image for the ${var.name_prefix} GitHub Actions runner (managed by Terraform)."
    Resources = {
      RunnerImage = {
        Type = "AWS::Lambda::MicrovmImage"
        Properties = {
          Name             = local.runner_image_name
          Description      = "GitHub Actions runner supervisor for ${var.name_prefix} (built by Terraform)"
          BaseImageArn     = local.microvm_base_image_arn
          BaseImageVersion = local.microvm_base_image_version
          BuildRoleArn     = aws_iam_role.microvm_build.arn
          CodeArtifact     = { Uri = "s3://${aws_s3_object.supervisor_zip.bucket}/${aws_s3_object.supervisor_zip.key}" }
          # Must match ARCH in src/microvm-runner/build.sh.
          CpuConfigurations = [{ Architecture = "ARM_64" }]
          Resources         = [{ MinimumMemoryInMiB = 2048 }]
          # Required by CloudFormation even when empty.
          AdditionalOsCapabilities = []
          # Required by CloudFormation even when empty.
          EnvironmentVariables = []
          # The build needs internet (apt, runner download).
          EgressNetworkConnectors = ["arn:aws:lambda:${var.region}:aws:network-connector:aws-network-connector:INTERNET_EGRESS"]
          # The supervisor needs /run to start the job; /run requires /ready.
          Hooks = {
            Port              = 8080
            MicrovmHooks      = { Run = "ENABLED", RunTimeoutInSeconds = 30 }
            MicrovmImageHooks = { Ready = "ENABLED", ReadyTimeoutInSeconds = 30 }
          }
          Logging = { CloudWatch = { LogGroup = "/aws/lambda-microvms/${local.runner_image_name}" } }
          Tags    = [for k, v in local.tags : { Key = k, Value = v }]
        }
      }
    }
    Outputs = {
      ImageArn = { Value = { "Fn::GetAtt" = ["RunnerImage", "ImageArn"] } }
    }
  })

  # Create and update wait for the image build.
  timeouts {
    create = "60m"
    update = "60m"
    delete = "30m"
  }

  depends_on = [aws_iam_role_policy.microvm_build, aws_s3_bucket_policy.artifacts]
}

# --- Webhook Lambda ---

# Vendors boto3: the runtime's built-in boto3 predates the lambda-microvms client.
resource "null_resource" "webhook_build" {
  triggers = {
    handler = filemd5("${path.module}/src/webhook/handler.py")
    reqs    = filemd5("${path.module}/src/webhook/requirements.txt")
  }

  provisioner "local-exec" {
    command = <<-EOT
      set -e
      PKG="${path.module}/.build/webhook_pkg"
      rm -rf "$PKG" && mkdir -p "$PKG"
      cp "${path.module}/src/webhook/handler.py" "$PKG/"
      pip3 install -r "${path.module}/src/webhook/requirements.txt" \
        --target "$PKG" --only-binary=:all: --platform manylinux2014_x86_64 \
        --python-version 3.12 --quiet
    EOT
  }
}

data "archive_file" "webhook" {
  type        = "zip"
  source_dir  = "${path.module}/.build/webhook_pkg"
  output_path = "${path.module}/.build/webhook.zip"
  depends_on  = [null_resource.webhook_build]
}

resource "aws_lambda_function" "webhook" {
  function_name    = local.webhook_function_name
  role             = aws_iam_role.webhook.arn
  runtime          = "python3.12"
  handler          = "handler.handler"
  filename         = data.archive_file.webhook.output_path
  source_code_hash = data.archive_file.webhook.output_base64sha256
  timeout          = 15

  environment {
    variables = {
      RUNNER_SCOPE    = var.runner_scope
      GITHUB_OWNER    = var.github_owner
      GITHUB_REPO     = var.github_repo
      GITHUB_ORG      = var.github_org
      RUNNER_LABELS   = join(",", var.runner_labels)
      RUNNER_GROUP_ID = "1"
      # RunMicrovm launches the image's latest active version, so an image
      # update doesn't change this value.
      MICROVM_IMAGE_ARN            = aws_cloudformation_stack.microvm_image.outputs["ImageArn"]
      MICROVM_EXECUTION_ROLE_ARN   = aws_iam_role.microvm_execution.arn
      MICROVM_MAX_DURATION_SECONDS = tostring(var.microvm_max_duration_seconds)
      JIT_BUCKET                   = aws_s3_bucket.artifacts.id
      JIT_KEY_PREFIX               = local.jit_key_prefix
      MICROVM_LOG_GROUP            = aws_cloudwatch_log_group.microvm_runtime.name
      PAT_SECRET_ARN               = aws_secretsmanager_secret.pat.arn
      WEBHOOK_SECRET_ARN           = aws_secretsmanager_secret.webhook.arn
    }
  }

  lifecycle {
    # Variable validation can't reference other variables on Terraform < 1.9.
    precondition {
      condition     = var.runner_scope != "repo" || (var.github_owner != "" && var.github_repo != "")
      error_message = "runner_scope = \"repo\" requires github_owner and github_repo."
    }
    precondition {
      condition     = var.runner_scope != "org" || var.github_org != ""
      error_message = "runner_scope = \"org\" requires github_org."
    }
  }

  depends_on = [aws_cloudwatch_log_group.webhook]

  tags = local.tags
}

# --- API Gateway ---
# REST API (v1) so AWS WAF can be attached to the stage.

resource "aws_api_gateway_rest_api" "webhook" {
  name = "${var.name_prefix}-webhook-api"

  endpoint_configuration {
    types = ["REGIONAL"]
  }

  tags = local.tags
}

resource "aws_api_gateway_resource" "webhook" {
  rest_api_id = aws_api_gateway_rest_api.webhook.id
  parent_id   = aws_api_gateway_rest_api.webhook.root_resource_id
  path_part   = "webhook"
}

resource "aws_api_gateway_method" "webhook_post" {
  rest_api_id   = aws_api_gateway_rest_api.webhook.id
  resource_id   = aws_api_gateway_resource.webhook.id
  http_method   = "POST"
  authorization = "NONE" # public; the handler's HMAC check is the authentication
}

resource "aws_api_gateway_integration" "webhook" {
  rest_api_id             = aws_api_gateway_rest_api.webhook.id
  resource_id             = aws_api_gateway_resource.webhook.id
  http_method             = aws_api_gateway_method.webhook_post.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.webhook.invoke_arn
}

resource "aws_api_gateway_deployment" "webhook" {
  rest_api_id = aws_api_gateway_rest_api.webhook.id

  triggers = {
    redeploy = sha1(jsonencode([
      aws_api_gateway_resource.webhook.id,
      aws_api_gateway_method.webhook_post.id,
      aws_api_gateway_integration.webhook.id,
    ]))
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_stage" "webhook" {
  rest_api_id   = aws_api_gateway_rest_api.webhook.id
  deployment_id = aws_api_gateway_deployment.webhook.id
  stage_name    = "v1"
  tags          = local.tags
}

resource "aws_lambda_permission" "apigw_invoke" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.webhook.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.webhook.execution_arn}/*/*"
}
