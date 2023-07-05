data "aws_region" "creation_account" {
}

data "aws_caller_identity" "creation_account" {
}

data "archive_file" "ami_share_lambda_function" {
  type             = "zip"
  source_file      = "../src/Creator-Account/share_ami.py"
  output_file_mode = "0666"
  output_path      = "${path.module}/files/ami-share.zip"
}


data "aws_iam_policy_document" "ami_share_assume_role" {
  statement {
    sid = "AssumeRole"

    actions = [
      "sts:AssumeRole"
    ]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
    effect = "Allow"
  }
}


data "aws_iam_policy_document" "ami_share_lambda_policy_document" {
  statement {
    sid    = "loggroup"
    effect = "Allow"
    actions = [
      "logs:CreateLogGroup"
    ]
    resources = ["arn:aws:logs:${local.creation_region}:${local.creation_account_id}:*"]
  }
  statement {
    sid    = "logstream"
    effect = "Allow"
    actions = [
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]
    resources = ["arn:aws:logs:${local.creation_region}:${local.creation_account_id}:log-group:/aws/lambda/${var.ami_share_function_name}*:*"]
  }

  statement {
    sid    = "dynamodb"
    effect = "Allow"
    actions = [
      "dynamodb:BatchGetItem",
      "dynamodb:UntagResource",
      "dynamodb:PutItem",
      "dynamodb:ListTables",
      "dynamodb:DeleteItem",
      "dynamodb:Scan",
      "dynamodb:Query",
      "dynamodb:UpdateItem",
      "dynamodb:CreateTable",
      "dynamodb:TagResource",
      "dynamodb:DescribeTable",
      "dynamodb:GetItem",
      "dynamodb:UpdateTable",
      "dynamodb:GetRecords"
    ]
    resources = ["arn:aws:dynamodb:${local.creation_region}:${local.creation_account_id}:table/${aws_dynamodb_table.ami_share_dynamodb_table.id}"]
  }

  statement {
    sid    = "ssm"
    effect = "Allow"
    actions = [
      "ssm:DescribeParameters",
      "ssm:GetParameterHistory",
      "ssm:GetParametersByPath",
      "ssm:GetParameters",
      "ssm:GetParameter"
    ]
    resources = ["arn:aws:ssm:${local.creation_region}:${local.creation_account_id}:parameter/cross-*"]
  }
  statement {
    sid    = "ses"
    effect = "Allow"
    actions = [
      "ses:SendEmail"
    ]
    resources = ["arn:aws:ses:${local.creation_region}:${local.creation_account_id}:identity/*"]
  }
}


data "aws_iam_policy_document" "external_dynamodb_access_policy_document" {
  statement {
    sid    = "dynamodb"
    effect = "Allow"
    actions = [
      "dynamodb:BatchGetItem",
      "dynamodb:UntagResource",
      "dynamodb:PutItem",
      "dynamodb:ListTables",
      "dynamodb:DeleteItem",
      "dynamodb:Scan",
      "dynamodb:Query",
      "dynamodb:UpdateItem",
      "dynamodb:CreateTable",
      "dynamodb:TagResource",
      "dynamodb:DescribeTable",
      "dynamodb:GetItem",
      "dynamodb:UpdateTable",
      "dynamodb:GetRecords"
    ]
    resources = ["arn:aws:dynamodb:${local.creation_region}:${local.creation_account_id}:table/${aws_dynamodb_table.ami_share_dynamodb_table.id}"]
  }
}


data "aws_iam_policy_document" "external_assume_role" {
  dynamic "statement" {
    for_each = var.account_email_mapping
    content {
      actions = ["sts:AssumeRole"]
      effect  = "Allow"
      principals {
        type        = "AWS"
        identifiers = ["arn:aws:iam::${statement.value["account"]}:root"]
      }
    }

  }
}