//---------------------------------------------------------
// Provider
//---------------------------------------------------------

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

//---------------------------------------------------------
// Data
//---------------------------------------------------------
data "aws_caller_identity" "current" {}

data "archive_file" "lambda_zip_file" {
  type        = "zip"
  source_file = "${path.module}/src/app.js"
  output_path = "${path.module}/lambda.zip"
}

data "aws_iam_policy" "lambda_basic_execution_role_policy" {
  name = "AWSLambdaBasicExecutionRole"
}

//---------------------------------------------------------
// Resources - EventBridge
//---------------------------------------------------------

# Create a new event bridge Rule
resource "aws_cloudwatch_event_rule" "MyEventRule" {
  event_pattern = <<PATTERN
{
  "account": ["${data.aws_caller_identity.current.account_id}"],
  "source": ["demo.sns"]
}
PATTERN
}

# Set the SNS topic as a target to the EventBridge rule.
resource "aws_cloudwatch_event_target" "MyRuleTarget" {
  rule = aws_cloudwatch_event_rule.MyEventRule.name
  arn  = aws_sns_topic.MySNSTopic.arn
}

//---------------------------------------------------------
// Resources - SNS
//---------------------------------------------------------

# Create new SNS topic
resource "aws_sns_topic" "MySNSTopic" {
  name = "MySNSTopic"
}

# Create SNS topic policy to allow Eventbridge to publish to the SNS topic
resource "aws_sns_topic_policy" "default" {
  arn    = aws_sns_topic.MySNSTopic.arn
  policy = <<POLICY
{
  "Version": "2008-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Action": "sns:Publish",
      "Resource": "${aws_sns_topic.MySNSTopic.arn}",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "${aws_cloudwatch_event_rule.MyEventRule.arn}"
        }
      }
    }
  ]
}
POLICY  
}

resource "aws_sns_topic_subscription" "sns-topic" {
  topic_arn = aws_sns_topic.MySNSTopic.arn
  protocol  = "lambda"
  endpoint  = aws_lambda_function.lambda_function.arn
}

//---------------------------------------------------------
// Resources - AWS Lambda
//---------------------------------------------------------

resource "aws_lambda_function" "lambda_function" {
  function_name    = "TopicSubscriberFunction"
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = data.archive_file.lambda_zip_file.output_base64sha256
  handler          = "app.handler"
  role             = aws_iam_role.lambda_iam_role.arn
  runtime          = "nodejs14.x"
}


resource "aws_iam_role" "lambda_iam_role" {
  name_prefix         = "LambdaSNSRole-"
  managed_policy_arns = [
    data.aws_iam_policy.lambda_basic_execution_role_policy.arn
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

resource "aws_lambda_permission" "with_sns" {
  statement_id  = "AllowExecutionFromSNS"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_function.function_name
  principal     = "sns.amazonaws.com"
  source_arn    = aws_sns_topic.MySNSTopic.arn
}





//---------------------------------------------------------
// Output
//---------------------------------------------------------

# display the Name and ARN of the SNS topic
output "SNS-Topic" {
  value       = aws_sns_topic.MySNSTopic.name
  description = "The SNS Topic Name"
}

output "SNS-Topic-ARN" {
  value       = aws_sns_topic.MySNSTopic.arn
  description = "The SNS Topic ARN"
}

output "Lambda-function" {
  value       = aws_lambda_function.lambda_function.arn
  description = "TopicSubscriberFunction function name"
}