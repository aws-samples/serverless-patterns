terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.8.0"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_iam_role" "this" {
  managed_policy_arns = [
    "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  ]

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

data "archive_file" "layer_zip" {
  type        = "zip"
  source_dir  = "./dependencies/mysql-connector-python"
  output_path = "./dependencies/zipped/mysql-connector-python.zip"
}

resource "aws_lambda_layer_version" "this" {
  filename            = data.archive_file.layer_zip.output_path
  layer_name          = "mysql-connector-python"
  compatible_runtimes = ["python3.8"]

  # The filebase64sha256() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
  # source_code_hash = "${base64sha256(file("lambda_function_payload.zip"))}"
  source_code_hash = filebase64sha256(data.archive_file.layer_zip.output_path)
}

data "archive_file" "lambda_function" {
  type        = "zip"
  source_file = "./src/example-lambda/app.py"
  output_path = "./src/zipped/lambda_function.zip"
}

resource "aws_lambda_function" "with_layer" {
  function_name    = "lambda_with_layer"
  filename         = data.archive_file.lambda_function.output_path
  role             = aws_iam_role.this.arn
  handler          = "app.lambda_handler"
  runtime          = "python3.8"
  source_code_hash = filebase64sha256(data.archive_file.lambda_function.output_path)

  layers = [
    aws_lambda_layer_version.this.arn
  ]
}

resource "aws_lambda_function" "without_layer" {
  function_name    = "lambda_without_layer"
  filename         = data.archive_file.lambda_function.output_path
  role             = aws_iam_role.this.arn
  handler          = "app.lambda_handler"
  runtime          = "python3.8"
  source_code_hash = filebase64sha256(data.archive_file.lambda_function.output_path)
}