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

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

#Create SQS queue
resource "aws_sqs_queue" "MySQSqueue" {
}

# Create an IAM role for API Gateway
resource "aws_iam_role" "APIGWRole" {
  assume_role_policy = <<POLICY1
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Principal" : {
        "Service" : "apigateway.amazonaws.com"
      },
      "Action" : "sts:AssumeRole"
    }
  ]
}
POLICY1
}

# Create an IAM policy for API Gateway to send messages to SQS
resource "aws_iam_policy" "APIGWPolicy" {
  policy = <<POLICY2
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "sqs:SendMessage",
        "sqs:SendMessageBatch"
      ],
      "Resource" : "${aws_sqs_queue.MySQSqueue.arn}"
    }
  ]
}
POLICY2
}

# Attach the IAM policies to the equivalent rule
resource "aws_iam_role_policy_attachment" "APIGWPolicyAttachment" {
  role       = aws_iam_role.APIGWRole.name
  policy_arn = aws_iam_policy.APIGWPolicy.arn
}

#Create a new API Gateway rest api with SQS Integration
resource "aws_api_gateway_rest_api" "MyApiGatewayRestApi" {
  name = "APIGW SQS Serverless Pattern Demo"
  body = jsonencode({
    "openapi" : "3.0.1",
    "info" : {
      "title" : "APIGW SQS Serverless Pattern Demo",
      "version" : "2022-03-03T00:00:00Z"
    },
    "servers" : [{
      "variables" : {
        "basePath" : {
          "default" : "/default"
        }
      }
    }],
    "paths" : {
      "/submit" : {
        "post" : {
          "responses" : {
            "200" : {
              "description" : "200 response",
              "content" : {
                "application/json" : {
                  "schema" : {
                    "$ref" : "#/components/schemas/Empty"
                  }
                }
              }
            }
          },
          "x-amazon-apigateway-integration" : {
            "type" : "aws",
            "credentials" : "${aws_iam_role.APIGWRole.arn}",
            "httpMethod" : "POST",
            "uri" : "arn:aws:apigateway:${data.aws_region.current.name}:sqs:path/${data.aws_caller_identity.current.account_id}/${aws_sqs_queue.MySQSqueue.name}",
            "responses" : {
              "default" : {
                "statusCode" : "200"
              }
            },
            "requestParameters" : {
              "integration.request.header.Content-Type" : "'application/x-www-form-urlencoded'"
            },
            "requestTemplates" : {
              "application/json" : "Action=SendMessage&MessageBody=$input.body"
            },
            "passthroughBehavior" : "never"
          }
        }
      }
    },
    "components" : {
      "schemas" : {
        "Empty" : {
          "title" : "Empty Schema",
          "type" : "object"
        }
      }
    }
  })
}

# Create a new API Gateway deployment for the created rest api
resource "aws_api_gateway_deployment" "MyApiGatewayDeployment" {
  rest_api_id = aws_api_gateway_rest_api.MyApiGatewayRestApi.id
}

# Create a Log Group for API Gateway to push logs to
resource "aws_cloudwatch_log_group" "MyLogGroup" {
  name_prefix = "/aws/APIGW/terraform"
}

# Create a Log Policy to allow Cloudwatch to Create log streams and put logs
resource "aws_cloudwatch_log_resource_policy" "MyCloudWatchLogPolicy" {
  policy_name     = "Terraform-CloudWatchLogPolicy-${data.aws_caller_identity.current.account_id}"
  policy_document = <<POLICY3
{
  "Version": "2012-10-17",
  "Id": "CWLogsPolicy",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [ 
          "apigateway.amazonaws.com",
          "delivery.logs.amazonaws.com"
          ]
      },
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
        ],
      "Resource": "${aws_cloudwatch_log_group.MyLogGroup.arn}",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "${aws_api_gateway_rest_api.MyApiGatewayRestApi.arn}"
        }
      }
    }
  ]
}
POLICY3  
}

# Create a new API Gateway stage with logging enabled
resource "aws_api_gateway_stage" "MyApiGatewayStage" {
  deployment_id = aws_api_gateway_deployment.MyApiGatewayDeployment.id
  rest_api_id   = aws_api_gateway_rest_api.MyApiGatewayRestApi.id
  stage_name    = "default"

  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.MyLogGroup.arn
    format          = "{ \"requestId\":\"$context.requestId\", \"ip\": \"$context.identity.sourceIp\", \"requestTime\":\"$context.requestTime\", \"httpMethod\":\"$context.httpMethod\",\"routeKey\":\"$context.routeKey\", \"status\":\"$context.status\",\"protocol\":\"$context.protocol\", \"responseLength\":\"$context.responseLength\" }"
  }
}

# If you are using apigateway and you have an existing cloudwatch role ARN set to your account delete the aws_api_gateway_account block, the aws_iam_role block & the aws_iam_role_policy block.

## delete if you have this configured in your account
resource "aws_api_gateway_account" "ApiGatewayAccountSetting" {
  cloudwatch_role_arn = aws_iam_role.APIGatewayCloudWatchRole.arn
}

## delete if you have this configured in your account
resource "aws_iam_role" "APIGatewayCloudWatchRole" {
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "apigateway.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

## delete if you have this configured in your account
resource "aws_iam_role_policy" "APIGatewayCloudWatchPolicy" {
  role = aws_iam_role.APIGatewayCloudWatchRole.id

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams",
                "logs:PutLogEvents",
                "logs:GetLogEvents",
                "logs:FilterLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
EOF
}

# Configure API Gateway to push all logs to CloudWatch Logs
resource "aws_api_gateway_method_settings" "MyApiGatewaySetting" {
  rest_api_id = aws_api_gateway_rest_api.MyApiGatewayRestApi.id
  stage_name  = aws_api_gateway_stage.MyApiGatewayStage.stage_name
  method_path = "*/*"

  settings {
    # Enable CloudWatch logging and metrics
    metrics_enabled = true
    logging_level   = "INFO"
  }
}

# Display the SQS queue URL & API Gateway invokation URL
output "SQS-QUEUE" {
  value       = aws_sqs_queue.MySQSqueue.id
  description = "The SQS Queue URL"
}

output "APIGW-URL" {
  value       = aws_api_gateway_stage.MyApiGatewayStage.invoke_url
  description = "The API Gateway Invocation URL Queue URL"
}

# Command for testing to send data to api gateway
output "Test-Command1" {
  value       = "curl --location --request POST '${aws_api_gateway_stage.MyApiGatewayStage.invoke_url}/submit' --header 'Content-Type: application/json'  --data-raw '{ \"TestMessage\": \"Hello From ApiGateway!\" }'"
  description = "Command to invoke the API Gateway"
}

# Command for testing to retrieve the message from the SQS queue
output "Test-Command2" {
  value       = "aws sqs receive-message --queue-url ${aws_sqs_queue.MySQSqueue.id}"
  description = "Command to query the SQS Queue for messages"
}