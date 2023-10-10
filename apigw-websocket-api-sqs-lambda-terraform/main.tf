terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.1.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.2.0"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region = var.aws_region
}

data "aws_caller_identity" "current" {}

locals {
  account_id = data.aws_caller_identity.current.account_id
}

output "account_id" {
  value = local.account_id
}

resource "aws_sqs_queue" "fifo_queue" {
  fifo_queue                        = true
  name                              = var.sqs_name
  sqs_managed_sse_enabled           = true
}

resource "random_string" "random" {
  length           = 4
  special          = false
}

#========================================================================
// API Gateway setup
#========================================================================

resource "aws_apigatewayv2_api" "my_websocket_api" {
  name                         = "${var.apigwy_name}-${random_string.random.id}"
  description                  = "Send websocket data to SQS which is then processed by a Lambda"
  protocol_type                = "WEBSOCKET"
  route_selection_expression   = "$request.body.action"
}

resource "aws_apigatewayv2_integration" "demo_integration" {
    api_id                                    = aws_apigatewayv2_api.my_websocket_api.id
    connection_type                           = "INTERNET"
    credentials_arn                           = aws_iam_role.apigwy_websocket_sqs_role.arn
    integration_method                        = "POST"
    integration_type                          = "AWS"
    integration_uri                           = "arn:aws:apigateway:${var.aws_region}:sqs:path/${local.account_id}/${var.sqs_name}"
    passthrough_behavior                      = "NEVER"
    request_parameters                        = {
        "integration.request.header.Content-Type" = "'application/x-www-form-urlencoded'"
    }
    request_templates                         = {
        "$default" = "Action=SendMessage&MessageGroupId=$input.path('$.MessageGroupId')&MessageDeduplicationId=$context.requestId&MessageAttribute.1.Name=connectionId&MessageAttribute.1.Value.StringValue=$context.connectionId&MessageAttribute.1.Value.DataType=String&MessageAttribute.2.Name=requestId&MessageAttribute.2.Value.StringValue=$context.requestId&MessageAttribute.2.Value.DataType=String&MessageBody=$input.json('$')"
    }
    template_selection_expression             = "\\$default"
    timeout_milliseconds                      = 29000
    depends_on = [
    aws_iam_role.apigwy_websocket_sqs_role,  
    ]
}

resource "aws_apigatewayv2_stage" "production" {
  api_id          = aws_apigatewayv2_api.my_websocket_api.id
  name            = "production"
  auto_deploy     = true
}

resource "aws_apigatewayv2_route" "default" {
    api_id               = aws_apigatewayv2_api.my_websocket_api.id
    route_key            = "$default"
    target               = "integrations/${aws_apigatewayv2_integration.demo_integration.id}"  
}


#========================================================================
// lambda setup
#========================================================================

resource "aws_lambda_function" "lambda_sqs_websocket_response" {
    function_name                  = "${var.lambda_name}-${random_string.random.id}"
    description                    = "serverlessland pattern"
    s3_bucket                      = aws_s3_bucket.lambda_bucket.id
    s3_key                         = aws_s3_object.lambda.key
    source_code_hash               = data.archive_file.lambda_source.output_base64sha256
    runtime                        = "python3.8"
    handler                        = "app.lambda_handler"
    role                           = aws_iam_role.lambda_execution.arn
    timeout                        = 15

    environment {
        variables = {
            "ApiGatewayEndpoint" = "https://${aws_apigatewayv2_api.my_websocket_api.id}.execute-api.${var.aws_region}.amazonaws.com/${aws_apigatewayv2_stage.production.name}"
        }
    }

    timeouts {}

    tracing_config {
        mode = "PassThrough"
    }
    depends_on = [aws_cloudwatch_log_group.lambda_logs, aws_apigatewayv2_stage.production]
}

resource "aws_cloudwatch_log_group" "lambda_logs" {
  name = "/aws/lambda/${var.lambda_name}-${random_string.random.id}"

  retention_in_days = var.lambda_log_retention
}


resource "aws_lambda_event_source_mapping" "apigwy_sqs" {
    event_source_arn = aws_sqs_queue.fifo_queue.arn
    function_name    = aws_lambda_function.lambda_sqs_websocket_response.arn
}

// S3 for Lambda
resource "aws_s3_bucket" "lambda_bucket" {
  bucket_prefix = var.s3_bucket_prefix
  force_destroy = true
}

resource "aws_s3_bucket_acl" "private_bucket" {
  bucket = aws_s3_bucket.lambda_bucket.id
  acl    = "private"
}

data "archive_file" "lambda_source" {
  type = "zip"
  source_dir  = "${path.module}/src"
  output_path = "${path.module}/src.zip"
}

resource "aws_s3_object" "lambda" {
  bucket = aws_s3_bucket.lambda_bucket.id
  key    = "source.zip"
  source = data.archive_file.lambda_source.output_path
  etag = filemd5(data.archive_file.lambda_source.output_path)
}

// IAM Role for SQS
resource "aws_iam_role" "apigwy_websocket_sqs_role" {
  name = "ApiGatewayWebsocketSQSRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Sid    = ""
      Principal = {
        Service = "apigateway.amazonaws.com"
      }
      }
    ]
  })
}

resource "aws_iam_policy" "apigwy_sqs_send_message" {
  name = "APIGatewaySQSSendMessagePolicy"

  policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "sqs:SendMessage",
            "Resource": "arn:aws:sqs:${var.aws_region}:${local.account_id}:${var.sqs_name}",
            "Effect": "Allow"
        }
    ]
}
POLICY
}

resource "aws_iam_role_policy_attachment" "apigwy_policy" {
  role       = aws_iam_role.apigwy_websocket_sqs_role.name
  policy_arn = aws_iam_policy.apigwy_sqs_send_message.arn
}

// IAM Role for lambda
resource "aws_iam_role" "lambda_execution" {
  name = "WebsocketApi-${var.lambda_name}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Sid    = ""
      Principal = {
        Service = "lambda.amazonaws.com"
      }
      }
    ]
  })
}

resource "aws_iam_policy" "lambda_exec_role" {
  name = "SQSWebsocketResponseServiceRole"

  policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "execute-api:ManageConnections",
            "Resource": "${aws_apigatewayv2_stage.production.execution_arn}/POST/*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "sqs:ReceiveMessage",
                "sqs:ChangeMessageVisibility",
                "sqs:GetQueueUrl",
                "sqs:DeleteMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "arn:aws:sqs:${var.aws_region}:${local.account_id}:${var.sqs_name}",
            "Effect": "Allow"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
POLICY
}

resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       = aws_iam_role.lambda_execution.name
  policy_arn = aws_iam_policy.lambda_exec_role.arn
}