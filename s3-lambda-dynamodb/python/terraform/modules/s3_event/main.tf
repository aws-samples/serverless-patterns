locals {
  s3_name = "${var.project}-${var.bucket_name}"
}

data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

data "archive_file" "python_lambda_package" {
  type        = "zip"
  source_file = "${path.module}/code/lambda_function.py"
  output_path = "lambda_function_payload.zip"
}

resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

resource "aws_iam_policy" "write_to_ddb" {
  name        = "write_to_ddb"
  path        = "/"
  description = "Write to ddb policy"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        "Sid": "Statement1",
        "Effect": "Allow",
        "Action": [
          "dynamodb:UpdateTable",
          "dynamodb:CreateTable",
          "dynamodb:BatchWriteItem",
          "dynamodb:PutItem",
          "dynamodb:UpdateItem"
        ],
        "Resource": [
          "*"
        ]
		  }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic_policy" {
  role       = aws_iam_role.iam_for_lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole" 
}

resource "aws_iam_role_policy_attachment" "s3_read_only" {
  role       = aws_iam_role.iam_for_lambda.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess" 
}

resource "aws_iam_role_policy_attachment" "write_to_ddb" {
  role       = aws_iam_role.iam_for_lambda.name
  policy_arn = aws_iam_policy.write_to_ddb.arn
}

resource "aws_lambda_permission" "allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.test_lambda.arn
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.json_bucket.arn
}

resource "aws_lambda_function" "test_lambda" {
  filename      = "lambda_function_payload.zip"
  function_name = "upload_to_ddb"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "lambda_function.lambda_handler"

  source_code_hash = data.archive_file.python_lambda_package.output_base64sha256

  runtime = "python3.14"

  environment {
    variables = {
      DYNAMODB_TABLE_NAME = var.table_name
    }
  }
}

resource "aws_s3_bucket" "json_bucket" {
  bucket = local.s3_name
  force_destroy = true
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.json_bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.test_lambda.arn
    events              = ["s3:ObjectCreated:*"]
  }

  depends_on = [aws_lambda_permission.allow_bucket]
}