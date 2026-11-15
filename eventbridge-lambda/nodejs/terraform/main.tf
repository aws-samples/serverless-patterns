terraform {
  required_providers {
	aws = {
	  source  = "hashicorp/aws"
	  version = "~> 5.0"
	}
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_lambda_function" "lambda_function" {
  function_name    = "ConsumerFunction"
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = data.archive_file.lambda_zip_file.output_base64sha256
  handler          = "app.handler"
  role             = aws_iam_role.lambda_iam_role.arn
  runtime          = "nodejs24.x"
}

data "archive_file" "lambda_zip_file" {
  type        = "zip"
  source_file = "${path.module}/src/app.js"
  output_path = "${path.module}/lambda.zip"
}

data "aws_iam_policy" "lambda_basic_execution_role_policy" {
  name = "AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role" "lambda_iam_role" {
  name_prefix         = "EventBridgeLambdaRole-"

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

resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role       = aws_iam_role.lambda_iam_role.name
  policy_arn = data.aws_iam_policy.lambda_basic_execution_role_policy.arn
}

resource "aws_cloudwatch_event_rule" "event_rule" {
	name_prefix = "eventbridge-lambda-"
  event_pattern = <<EOF
{
  "detail-type": ["transaction"],
  "source": ["custom.myApp"],
  "detail": {
	"location": [{
	  "prefix": "EUR-"
	}]
  }
}
EOF
}

resource "aws_cloudwatch_event_target" "target_lambda_function" {
  rule = aws_cloudwatch_event_rule.event_rule.name
  arn  = aws_lambda_function.lambda_function.arn
}

resource "aws_lambda_permission" "allow_cloudwatch" {
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_function.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.event_rule.arn
}

output "ConsumerFunction" {
  value       = aws_lambda_function.lambda_function.arn
  description = "ConsumerFunction function name"
}
