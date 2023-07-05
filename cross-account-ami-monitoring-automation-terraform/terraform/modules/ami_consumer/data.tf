data "aws_region" "consumer_account" {
}

data "aws_caller_identity" "consumer_account" {
}


data "archive_file" "ami_usage_lambda_function" {
  count            = var.ami_creator_account ? 0 : 1
  type             = "zip"
  source_file      = "../src/Consumer-Account/ami_usage.py"
  output_file_mode = "0666"
  output_path      = "${path.module}/files/ami-usage.zip"
}

data "archive_file" "creator_ami_usage_lambda_function" {
  count            = var.ami_creator_account ? 1 : 0
  type             = "zip"
  source_file      = "../src/Creator-Account/creator_ami_usage.py"
  output_file_mode = "0666"
  output_path      = "${path.module}/files/creator-ami-usage.zip"

}


data "aws_iam_policy_document" "ami_usage_lambda_policy_document" {
  statement {
    sid    = "loggroup"
    effect = "Allow"
    actions = [
      "logs:CreateLogGroup"
    ]
    resources = ["arn:aws:logs:${local.consumer_region}:${local.consumer_account_id}:*"]
  }
  statement {
    sid    = "logstream"
    effect = "Allow"
    actions = [
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]
    resources = ["arn:aws:logs:${local.consumer_region}:${local.consumer_account_id}:log-group:/aws/lambda/${var.ami_usage_function_name}*:*"]
  }
  statement {
    sid    = "stsassume"
    effect = "Allow"
    actions = [
      "sts:AssumeRole"
    ]
    resources = [local.external_assume_role_arn]
  }
  statement {
    sid    = "ec2image"
    effect = "Allow"
    actions = [
      "ec2:DescribeImages"
    ]
    resources = ["*"]
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
    resources = ["arn:aws:dynamodb:${local.consumer_region}:${local.consumer_account_id}:table/${aws_dynamodb_table.ami_mapping_table.id}"]
  }
}

data "aws_iam_policy_document" "ami_usage_assume_role" {
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
