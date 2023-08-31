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
  region = "eu-west-1"
}
data "aws_region" "current" {}

locals {
  stack_name = "template"
}

variable "api_stage_name" {
  description = "Name of WebSocket API stage"
  type        = string
  default     = "production"
}

resource "aws_sns_topic" "sns_topic" {
  display_name = "${local.stack_name}-SNSTopic"
}

resource "aws_apigatewayv2_api" "web_socket_api" {
  name                       = "${local.stack_name}-WebSocketApi"
  protocol_type              = "WEBSOCKET"
  route_selection_expression = "$request.body.action"
}


resource "aws_apigatewayv2_stage" "MyApiGatewayStage" {
  api_id      = aws_apigatewayv2_api.web_socket_api.id
  name        = var.api_stage_name
  auto_deploy = true
}

resource "aws_apigatewayv2_route" "connect_route" {
  api_id                              = aws_apigatewayv2_api.web_socket_api.id
  route_key                           = "$connect"
  authorization_type                  = "NONE"
  route_response_selection_expression = "$default"
  operation_name                      = "ConnectRoute"
  target                              = join("/", ["integrations", aws_apigatewayv2_integration.connect_route_integration.id])
}

resource "aws_apigatewayv2_integration" "connect_route_integration" {
  api_id           = aws_apigatewayv2_api.web_socket_api.id
  integration_type = "MOCK"
  request_templates = {
    200 = "{\"statusCode\":200}"
  }
  template_selection_expression = "200"
  passthrough_behavior          = "WHEN_NO_MATCH"
}

resource "aws_apigatewayv2_route_response" "connect_route_response" {
  route_id           = aws_apigatewayv2_route.connect_route.id
  api_id             = aws_apigatewayv2_api.web_socket_api.id
  route_response_key = "$default"
}

resource "aws_apigatewayv2_integration_response" "connect_route_integration_response" {
  api_id                        = aws_apigatewayv2_api.web_socket_api.id
  integration_id                = aws_apigatewayv2_integration.connect_route_integration.id
  integration_response_key      = "/200/"
  template_selection_expression = "\\$default"
  response_templates = {
    200 = "{\"statusCode\":, \"message\":\"order initiated\"}"
  }
}

resource "aws_iam_role" "apigw_sns_demo_functionrole" {
  #name               = "apigw_sns_demo_functionrole"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "apigateway.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# Custom policy
resource "aws_iam_policy" "apigw_sns_demo_policy" {
  name        = "apigw-sns-demo-policy"
  path        = "/"
  description = "Policy for APIGW to SNS demo"
  policy      = <<EOF
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect": "Allow",
      "Action": [
        "sns:Publish"
      ],
      "Resource": "${aws_sns_topic.sns_topic.arn}"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "apigw_policy_attachment" {
  role       = aws_iam_role.apigw_sns_demo_functionrole.name
  policy_arn = aws_iam_policy.apigw_sns_demo_policy.arn
}


resource "aws_apigatewayv2_route" "disconnect_route" {
  api_id         = aws_apigatewayv2_api.web_socket_api.id
  route_key      = "$disconnect"
  operation_name = "DisconnectRoute"
  target         = join("/", ["integrations", aws_apigatewayv2_integration.disconnect_route_integration.id])
}

resource "aws_apigatewayv2_integration" "disconnect_route_integration" {
  api_id           = aws_apigatewayv2_api.web_socket_api.id
  integration_type = "MOCK"
  request_templates = {
    200 = "{\"statusCode\":200}"
  }
  template_selection_expression = "200"
  passthrough_behavior          = "WHEN_NO_MATCH"
}

resource "aws_apigatewayv2_integration_response" "disconnect_route_integration_response" {
  api_id                        = aws_apigatewayv2_api.web_socket_api.id
  integration_id                = aws_apigatewayv2_integration.disconnect_route_integration.id
  integration_response_key      = "/200/"
  template_selection_expression = "\\$default"
}


resource "aws_apigatewayv2_integration" "send_order_route_integration" {
  api_id                    = aws_apigatewayv2_api.web_socket_api.id
  integration_type          = "AWS"
  integration_uri           = "arn:aws:apigateway:${data.aws_region.current.name}:sns:action/Publish"
  credentials_arn           = aws_iam_role.apigw_sns_demo_functionrole.arn
  integration_method        = "POST"
  content_handling_strategy = "CONVERT_TO_TEXT"
  request_parameters = {
    "integration.request.header.Content-Type" = "'application/x-www-form-urlencoded'"
  }
  request_templates = {
    "$default" = "Action=Publish&TopicArn=$util.urlEncode(\"${aws_sns_topic.sns_topic.id}\")&Message=$input.json('$')"
  }
  template_selection_expression = "$request.body.action"
}

resource "aws_apigatewayv2_model" "food_order_model" {
  api_id       = aws_apigatewayv2_api.web_socket_api.id
  content_type = "application/json"
  description  = "this model helps us to ensure that all the required parameters are passed on to the SNS topic"
  name         = "orderModel"
  schema       = "{\"$schema\":\"http://json-schema.org/draft-04/schema#\",\"title\":\"orderInputModel\",\"type\":\"object\",\"properties\":{\"Number\":{\"type\":\"string\"},\"SirName\":{\"type\":\"string\"},\"Name\":{\"type\":\"string\"}},\"required\":[\"Name\",\"SirName\",\"Number\"]}"
}

resource "aws_apigatewayv2_route" "send_order" {
  api_id                     = aws_apigatewayv2_api.web_socket_api.id
  route_key                  = "sendOrder"
  authorization_type         = "NONE"
  model_selection_expression = "$request.body.action"
  request_models = {
    sendOrder = "orderModel"
  }
  target = join("/", ["integrations", aws_apigatewayv2_integration.send_order_route_integration.id])
}

resource "aws_apigatewayv2_route_response" "send_order_route_response" {
  route_id           = aws_apigatewayv2_route.send_order.id
  api_id             = aws_apigatewayv2_api.web_socket_api.id
  route_response_key = "$default"
}

resource "aws_apigatewayv2_integration_response" "send_order_route_integration_response" {
  api_id                   = aws_apigatewayv2_api.web_socket_api.id
  integration_id           = aws_apigatewayv2_integration.send_order_route_integration.id
  integration_response_key = "$default"
}



output "api_endpoint" {
  description = "API Gateway endpoint URL"
  value       = "wss://${aws_apigatewayv2_api.web_socket_api.id}.execute-api.${data.aws_region.current.name}.amazonaws.com/${var.api_stage_name}"
}
