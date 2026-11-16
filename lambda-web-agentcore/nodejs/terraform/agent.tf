# ---------------------------------------------------------------------------------------------
# Agent: a Strands agent on Amazon Bedrock AgentCore Runtime, deployed as a .zip (direct code
# deployment), so there is no container image, Docker or Amazon ECR repository to manage.
# ---------------------------------------------------------------------------------------------

locals {
  agent_src_dir = abspath("${path.module}/agent")
  agent_pkg_dir = "${local.build_dir}/agent"
}

# AgentCore Runtime runs on arm64, and it does not install dependencies for you, so the package
# must contain Linux arm64 wheels for every dependency next to the agent code:
# https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-code-deploy-python.html
resource "terraform_data" "agent_package" {
  triggers_replace = [
    filesha256("${local.agent_src_dir}/main.py"),
    filesha256("${local.agent_src_dir}/requirements.txt"),
  ]

  provisioner "local-exec" {
    interpreter = ["bash", "-c"]
    command     = <<-EOT
      set -euo pipefail
      rm -rf "${local.agent_pkg_dir}"
      uv pip install --quiet \
        --python-platform aarch64-manylinux2014 --python-version 3.13 \
        --only-binary :all: \
        --target "${local.agent_pkg_dir}" \
        -r "${local.agent_src_dir}/requirements.txt"
      cp "${local.agent_src_dir}/main.py" "${local.agent_pkg_dir}/"
    EOT
  }
}

data "archive_file" "agent" {
  type        = "zip"
  source_dir  = local.agent_pkg_dir
  output_path = "${local.build_dir}/agent.zip"

  depends_on = [terraform_data.agent_package]
}

resource "aws_s3_object" "agent" {
  bucket      = aws_s3_bucket.code.bucket
  key         = "agent.zip"
  source      = data.archive_file.agent.output_path
  source_hash = data.archive_file.agent.output_base64sha256

  depends_on = [aws_s3_bucket_versioning.code]
}

resource "aws_iam_role" "agent" {
  name = "${local.name}-agent"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Action    = "sts:AssumeRole"
      Principal = { Service = "bedrock-agentcore.amazonaws.com" }
      Condition = {
        StringEquals = { "aws:SourceAccount" = local.account_id }
        ArnLike      = { "aws:SourceArn" = "arn:${local.partition}:bedrock-agentcore:${local.region}:${local.account_id}:*" }
      }
    }]
  })
}

locals {
  inference_profile_arn = "arn:${local.partition}:bedrock:${local.region}:${local.account_id}:inference-profile/${local.model_id}"
}

# Permissions from the AgentCore Runtime execution role reference, scoped to this agent where the
# action allows it: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html
resource "aws_iam_role_policy" "agent" {
  role = aws_iam_role.agent.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid      = "InvokeModelThroughProfile"
        Effect   = "Allow"
        Action   = ["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream"]
        Resource = local.inference_profile_arn
      },
      {
        # A cross-Region inference profile routes each request to the foundation model in one of
        # the Regions of its geography, so allow the model in any Region, but only when the
        # request comes through the profile above.
        Sid      = "InvokeFoundationModelViaProfile"
        Effect   = "Allow"
        Action   = ["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream"]
        Resource = "arn:${local.partition}:bedrock:*::foundation-model/${local.foundation_model_id}"
        Condition = {
          StringEquals = { "bedrock:InferenceProfileArn" = local.inference_profile_arn }
        }
      },
      {
        Sid    = "AgentLogs"
        Effect = "Allow"
        Action = ["logs:CreateLogGroup", "logs:DescribeLogStreams", "logs:CreateLogStream", "logs:PutLogEvents"]
        Resource = [
          "arn:${local.partition}:logs:${local.region}:${local.account_id}:log-group:/aws/bedrock-agentcore/runtimes/*",
          "arn:${local.partition}:logs:${local.region}:${local.account_id}:log-group:/aws/bedrock-agentcore/runtimes/*:log-stream:*",
        ]
      },
      {
        Sid      = "DescribeLogGroups"
        Effect   = "Allow"
        Action   = "logs:DescribeLogGroups"
        Resource = "arn:${local.partition}:logs:${local.region}:${local.account_id}:log-group:*"
      },
      {
        Sid      = "Tracing"
        Effect   = "Allow"
        Action   = ["xray:PutTraceSegments", "xray:PutTelemetryRecords", "xray:GetSamplingRules", "xray:GetSamplingTargets"]
        Resource = "*"
      },
      {
        Sid       = "Metrics"
        Effect    = "Allow"
        Action    = "cloudwatch:PutMetricData"
        Resource  = "*"
        Condition = { StringEquals = { "cloudwatch:namespace" = "bedrock-agentcore" } }
      },
    ]
  })
}

# A new IAM role takes a few seconds to become assumable.
resource "time_sleep" "agent_role" {
  create_duration = "15s"
  triggers        = { role_arn = aws_iam_role.agent.arn }
  depends_on      = [aws_iam_role_policy.agent]
}

resource "aws_bedrockagentcore_agent_runtime" "agent" {
  agent_runtime_name = replace(local.name, "-", "_")
  description        = "Strands agent behind a Lambda Web Function (lambda-web-agentcore pattern)"
  role_arn           = time_sleep.agent_role.triggers["role_arn"]

  agent_runtime_artifact {
    code_configuration {
      entry_point = ["main.py"]
      runtime     = "PYTHON_3_13"

      code {
        s3 {
          bucket     = aws_s3_object.agent.bucket
          prefix     = aws_s3_object.agent.key
          version_id = aws_s3_object.agent.version_id
        }
      }
    }
  }

  environment_variables = {
    MODEL_ID = local.model_id
  }

  network_configuration {
    network_mode = "PUBLIC"
  }
}

# AgentCore Runtime creates its log group itself when the runtime is created, with the runtime ID in
# the name, so Terraform cannot create it first. This sets a retention period on it and deletes it
# when you run terraform destroy, so no logs are left behind.
resource "terraform_data" "agent_log_group" {
  input = {
    name   = "/aws/bedrock-agentcore/runtimes/${aws_bedrockagentcore_agent_runtime.agent.agent_runtime_id}-DEFAULT"
    region = local.region
    days   = var.log_retention_days
  }

  provisioner "local-exec" {
    command = "aws logs put-retention-policy --region ${self.input.region} --log-group-name '${self.input.name}' --retention-in-days ${self.input.days}"
  }

  provisioner "local-exec" {
    when    = destroy
    command = "aws logs delete-log-group --region ${self.input.region} --log-group-name '${self.input.name}' || true"
  }
}
