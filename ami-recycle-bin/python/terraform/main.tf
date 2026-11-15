# Default terraform provider configuration to manage resources in a region of the aws cloud provider
# To provision resources in a different region, update the region variable in variables.tf
provider "aws" {
  region = var.region
}

# Terraform block to enable hashicorp/aws provider and use the version constraint
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.65.0"
    }
  }
}

resource "aws_cloudwatch_event_rule" "event_rule" {
  name                = "invoke-lambda-daily"
  description         = "Invoke a Lambda function once per day"
  schedule_expression = "rate(1 day)"
  tags = {
    "Name" = "invoke-lambda-daily"
  }
}

resource "aws_cloudwatch_event_target" "event_target" {
  rule      = aws_cloudwatch_event_rule.event_rule.name
  target_id = "InvokeLambda"
  arn       = aws_lambda_function.lambda_function.arn
}

resource "aws_lambda_permission" "lambda_permission" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_function.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.event_rule.arn
}

resource "aws_cloudwatch_log_group" "example" {
  name              = "/aws/lambda/${aws_lambda_function.lambda_function.function_name}"
  retention_in_days = var.cw_retention_period
}

resource "aws_lambda_function" "lambda_function" {
  filename      = "src/ami-recycle-lambda.zip"
  function_name = var.function_name
  description   = var.function_description
  role          = aws_iam_role.lambda_role.arn
  handler       = "ami-recycle-lambda.lambda_handler"
  runtime       = var.function_runtime
  environment {
    variables = {
      "RECYCLE_BIN_TAG_KEY"         = var.resource_tag_key
      "RECYCLE_BIN_TAG_VALUE"       = var.resource_tag_value
      "RBIN_RETENTION_PERIOD_VALUE" = var.rbin_retention_period_value
      "RBIN_RETENTION_PERIOD_UNIT"  = var.rbin_retention_period_unit
    }
  }
  timeout          = var.function_timeout
  memory_size      = var.memory_size
  source_code_hash = filebase64sha256("src/ami-recycle-lambda.zip")
  tags = {
    "Name" = var.function_name
  }
}

resource "aws_iam_role" "lambda_role" {
  name = "ami-recycle-lambda-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Sid    = ""
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })

  inline_policy {
    name = "ami-recycle-lambda-policy"
    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Effect = "Allow"
          Action = [
            "logs:CreateLogGroup"
          ]
          Resource = "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:*"
        },
        {
          Effect = "Allow"
          Action = [
            "logs:CreateLogStream",
            "logs:PutLogEvents"
          ]
          Resource = "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${var.function_name}:*"
        },
        {
          Effect = "Allow"
          Action = [
            "ec2:CreateTags",
            "ec2:DeregisterImage",
            "ec2:DeleteSnapshot"
          ]
          Resource = [
            "arn:aws:ec2:${data.aws_region.current.name}::image/*",
            "arn:aws:ec2:${data.aws_region.current.name}::snapshot/*"
          ]
        },
        {
          Effect = "Allow"
          Action = [
            "ec2:DescribeTags",
            "ec2:DescribeImages",
            "ec2:DescribeSnapshots",
            "rbin:ListRules"
          ]
          Resource = "*"
        }
      ]
    })
  }
  tags = {
    "Name" = "ami-recycle-lambda-role"
  }
}

resource "aws_rbin_rule" "snapshot_rbin" {
  description   = "Recycle bin rule to retain deleted snapshots"
  resource_type = "EBS_SNAPSHOT"

  retention_period {
    retention_period_value = var.rbin_retention_period_value
    retention_period_unit  = var.rbin_retention_period_unit
  }

  resource_tags {
    resource_tag_key   = var.resource_tag_key
    resource_tag_value = var.resource_tag_value
  }

  tags = {
    "Name" = "Snapshot-Recycle-Bin"
  }
}

resource "aws_rbin_rule" "image_rbin" {
  description   = "Recycle bin rule to retain deleted snapshots"
  resource_type = "EC2_IMAGE"

  retention_period {
    retention_period_value = var.rbin_retention_period_value
    retention_period_unit  = var.rbin_retention_period_unit
  }

  resource_tags {
    resource_tag_key   = var.resource_tag_key
    resource_tag_value = var.resource_tag_value
  }

  tags = {
    "Name" = "EC2-Image-Recycle-Bin"
  }
}
