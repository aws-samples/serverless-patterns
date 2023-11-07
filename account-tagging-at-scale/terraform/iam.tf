resource "aws_iam_role" "iam_role" {
  name               = "apply-tags-current-accounts-role"
  tags               = var.default_tags
  assume_role_policy = data.aws_iam_policy_document.assume_role_lambda.json
}

data "aws_iam_policy_document" "assume_role_lambda" {
  statement {
    actions = ["sts:AssumeRole"]
    effect  = "Allow"
    principals {
      identifiers = ["lambda.amazonaws.com"]
      type        = "Service"
    }
  }
}

resource "aws_iam_policy" "lambda_policy_assume_policy_acctags" {
  name        = "apply-tags-current-accounts-assumepolicy"
  description = "apply-tags-current-accounts-assumepolicy"
  policy      = data.aws_iam_policy_document.lambda_policy_assume_policycrssact.json
}


data "aws_iam_policy_document" "lambda_policy_assume_policycrssact" {
  statement {
    effect    = "Allow"
    resources = ["arn:aws:iam::XXXXXXXXXXXXX:role/AFTCrossAccountRole"]
    actions   = ["sts:AssumeRole"]
  }
}



resource "aws_iam_role_policy_attachment" "assume_policy_attach_acc_close" {
  role       = aws_iam_role.iam_role.name
  policy_arn = aws_iam_policy.lambda_policy_assume_policy_acctags.arn
}


data "aws_iam_policy_document" "lambda_policy_core" {
  statement {
    sid       = "AllowLambdaFunctionToCreateLogs"
    effect    = "Allow"
    resources = ["arn:aws:logs:*:*:log-group:/aws/lambda/apply-tags-current-accounts:*"]
    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:CreateLogDelivery",
      "logs:PutLogEvents",
      "logs:GetLogEvents",
      "logs:DescribeLogStreams",
    ]
  }

  statement {
    sid       = "AllowLambdaFunctionToCreateEC2Interfaces"
    effect    = "Allow"
    resources = ["*"]
    actions = [
      "ec2:CreateNetworkInterface",
      "ec2:DescribeNetworkInterfaces",
      "ec2:DeleteNetworkInterface"
    ]
  }

  statement {
    sid       = "AllowLambdasqs"
    effect    = "Allow"
    resources = [aws_sqs_queue.lambdadlq.arn]
    actions = [
      "sqs:ChangeMessageVisibility",
      "sqs:DeleteMessage",
      "sqs:GetQueueAttributes",
      "sqs:GetQueueUrl",
      "sqs:ListQueueTags",
      "sqs:ReceiveMessage",
      "sqs:SendMessage",
    ]
  }
}


resource "aws_iam_role_policy" "lambda_policy" {
  name   = "apply-tags-current-accounts-policy"
  role   = aws_iam_role.iam_role.id
  policy = data.aws_iam_policy_document.lambda_policy_core.json
}