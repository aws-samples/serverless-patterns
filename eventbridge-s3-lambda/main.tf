variable "region" {}

provider "aws" {
  region  = "${var.region}"
}

data "aws_partition" "current" {}
resource "aws_iam_role" "lambda_execution_role" {
  name               = "lambda-execution-role-sns"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}
resource "aws_iam_role_policy" "lambda_policy" {
  name   = "LambdaPolicy"
  role   = aws_iam_role.lambda_execution_role.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        Resource = "arn:${data.aws_partition.current.partition}:logs:*:*:*"
      },
      {
        Effect = "Allow",
        Action = "sns:Publish",
        Resource = aws_sns_topic.sns_topic.arn
      }
    ]
  })
}
resource "aws_sns_topic" "sns_topic" {
  name = "s3-lambda-topic"
}
resource "aws_lambda_function" "sns_lambda" {
  function_name = "sns-lambda"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.12"
  role          = aws_iam_role.lambda_execution_role.arn
  filename      = "lambda_function_payload.zip"
  source_code_hash = filebase64sha256("lambda_function_payload.zip")
  environment {
    variables = {
      SNS_TOPIC_ARN = aws_sns_topic.sns_topic.arn
    }
  }
}
resource "aws_cloudwatch_log_group" "lambda_log_group" {
  name              = "/aws/lambda/sns-lambda"
  retention_in_days = 7
}
resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id  = "AllowEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.sns_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.s3_create_bucket_rule.arn
}
resource "aws_cloudwatch_event_rule" "s3_create_bucket_rule" {
  name        = "s3-create-bucket-rule"
  description = "Rule to capture S3 bucket creation events"
  event_pattern = jsonencode({
    source = ["aws.s3"],
    "detail-type" = ["AWS API Call via CloudTrail"],
    detail = {
      eventSource = ["s3.amazonaws.com"],
      eventName = ["CreateBucket"]
    }
  })
}
resource "aws_cloudwatch_event_target" "s3_create_bucket_target" {
  rule = aws_cloudwatch_event_rule.s3_create_bucket_rule.name
  arn  = aws_lambda_function.sns_lambda.arn
}
output "lambda_function_arn" {
  value = aws_lambda_function.sns_lambda.arn
}
output "sns_topic_arn" {
  value = aws_sns_topic.sns_topic.arn
}

