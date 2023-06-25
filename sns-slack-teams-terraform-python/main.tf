# Copyright Amazon.com, Inc.or its affiliates.All Rights Reserved.
# SPDX - License - Identifier: MIT - 0

# Define provider and region

terraform {
  required_providers {
        aws = {
            source  = "hashicorp/aws"
            version = "~> 4.16"
        }
    }
    required_version = ">= 1.2.0"
}

provider "aws" {
    region = "us-east-1"
    access_key = "my-access-key"
    secret_key = "my-secret-key"
}

#Create an IAM role for the Lambda function
    data "aws_iam_policy" "lambda_basic_execution_role_policy" {
    name = "AWSLambdaBasicExecutionRole"
}


resource "aws_iam_role" "lambda_iam_role" {
    name_prefix = "LambdaSNSRole-"
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

#Create the Lambda function
resource "aws_lambda_function" "slack_teams_integration_lambda" {
    
    function_name = "slack_teams_integration_lambda"
    filename = data.archive_file.lambda_zip_file.output_path
    source_code_hash = data.archive_file.lambda_zip_file.output_base64sha256
    handler = "slack_teams_integration_lambda.lambda_handler"
    runtime = "python3.8"
    role = aws_iam_role.lambda_iam_role.arn
    timeout = 10
    memory_size = 128
    publish = true
    
    # Add your lambda function code here or specify the location of the deployment package

    #Example using a deployment package stored in a S3 bucket:
    #s3_bucket = "your-bucket-name"
    #s3_key = "slack_teams_integration.zip"
    #source_code_hash = "your-source_code_hash"
}

#Adding policy to allow SNS service to invoke the lambda function
    resource "aws_lambda_permission" "with_sns" {
    statement_id = "AllowExecutionFromSNS"
    action = "lambda:InvokeFunction"
    function_name = "${aws_lambda_function.slack_teams_integration_lambda.arn}"
    principal = "sns.amazonaws.com"
    source_arn = "${aws_sns_topic.slack_teams_integration_topic.arn}"
}

#Example using Python code for slack:
  
data "archive_file" "lambda_zip_file" {
    type = "zip"
    source_file = "${path.module}/src/slack_teams_integration_lambda.py"
    output_path = "${path.module}/lambda.zip"

}

# Create the SNS topic
resource "aws_sns_topic" "slack_teams_integration_topic" {
    name = "slack_teams_integration_topic"
}

# Create an SNS topic subscription for the lambda function
    resource "aws_sns_topic_subscription" "lambda_subscription"{
    topic_arn = aws_sns_topic.slack_teams_integration_topic.arn
    protocol = "lambda"
    endpoint = aws_lambda_function.slack_teams_integration_lambda.arn
}

# Output the ARN of the Lambda function and SNS topic
output "lambda_function_arn" {
    value = aws_lambda_function.slack_teams_integration_lambda.arn
}

output "sns_topic_arn"{
    value = aws_sns_topic.slack_teams_integration_topic.arn
}