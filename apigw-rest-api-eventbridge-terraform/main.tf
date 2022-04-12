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

resource "random_string" "random" {
  length           = 4
  special          = false
}

resource "aws_api_gateway_rest_api" "rest_api_eb" {
  name        = "${var.apigw_name}-${random_string.random.id}"
  description = "serverlessland eb integration"
}


resource "aws_api_gateway_resource" "eb_resource" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_eb.id
  parent_id   = aws_api_gateway_rest_api.rest_api_eb.root_resource_id
  path_part   = "orders"
}


resource "aws_api_gateway_method" "post" {
  rest_api_id   = aws_api_gateway_rest_api.rest_api_eb.id
  resource_id   = aws_api_gateway_resource.eb_resource.id
  http_method   = "POST"
  authorization = "NONE"
  request_parameters   = {
      "method.request.header.Content-Type" = false
      "method.request.header.X-Amz-Target" = false
  }
}

resource "aws_api_gateway_method_response" "response_200" {
    rest_api_id         = aws_api_gateway_rest_api.rest_api_eb.id
    resource_id         = aws_api_gateway_resource.eb_resource.id
    http_method         = aws_api_gateway_method.post.http_method
    response_models     = {
        "application/json" = "Empty"
    }
    response_parameters = {}
    status_code         = "200"
}

resource "aws_api_gateway_integration" "eb_integration" {
  rest_api_id          = aws_api_gateway_rest_api.rest_api_eb.id
  resource_id          = aws_api_gateway_resource.eb_resource.id
  http_method          = aws_api_gateway_method.post.http_method
  integration_http_method  = aws_api_gateway_method.post.http_method
  type                 = "AWS"
  uri                  = "arn:aws:apigateway:${var.aws_region}:events:action/PutEvents" //arn:aws:apigateway:us-east-1:events:action/PutEvents
  passthrough_behavior = "WHEN_NO_TEMPLATES"
  credentials          = aws_iam_role.ApiGatewayEventBridgeRole.arn


  request_parameters = {}

  request_templates = {
        "application/json" = <<-EOT
            #set($context.requestOverride.header.X-Amz-Target = "AWSEvents.PutEvents")
            #set($context.requestOverride.header.Content-Type = "application/x-amz-json-1.1")            
            #set($inputRoot = $input.path('$')) 
            { 
              "Entries": [
                #foreach($elem in $inputRoot.items)
                {
                  "Detail": "$util.escapeJavaScript($elem.Detail).replaceAll("\\'","'")",
                  "DetailType": "$elem.DetailType",
                  "EventBusName": "${var.eventbus_name}",
                  "Source":"$elem.Source"
                }#if($foreach.hasNext),#end
                #end
              ]
            
            }
        EOT
  }
  
}

resource "aws_api_gateway_integration_response" "this" {
  rest_api_id          = aws_api_gateway_rest_api.rest_api_eb.id
  resource_id          = aws_api_gateway_resource.eb_resource.id
  http_method         = aws_api_gateway_method.post.http_method
  response_templates  = {
      "application/json" = <<-EOT
          #set($inputRoot = $input.path('$'))
        {
        }
      EOT
  }
  status_code         = aws_api_gateway_method_response.response_200.status_code
  depends_on = [aws_api_gateway_integration.eb_integration]
}

// API GATEWAY DEPLOYMENT

resource "aws_api_gateway_deployment" "this" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_eb.id

  triggers = {
    # NOTE: The configuration below will satisfy ordering considerations,
    #       but not pick up all future REST API changes. More advanced patterns
    #       are possible, such as using the filesha1() function against the
    #       Terraform configuration file(s) or removing the .id references to
    #       calculate a hash against whole resources. Be aware that using whole
    #       resources will show a difference after the initial implementation.
    #       It will stabilize to only change when resources change afterwards.
    redeployment = sha1(jsonencode([
      aws_api_gateway_resource.eb_resource.id,
      aws_api_gateway_method.post.id,
      aws_api_gateway_integration.eb_integration.id,
    ]))
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_stage" "dev" {
  deployment_id = aws_api_gateway_deployment.this.id
  rest_api_id   = aws_api_gateway_rest_api.rest_api_eb.id
  stage_name    = "dev"
}

// API GATEWAY ROLE WITH PERMISSIONS TO PUT EVENTS

resource "aws_iam_role" "ApiGatewayEventBridgeRole" {
  name = "ApiGatewayEventBridgeRole"

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

resource "aws_iam_policy" "EBPutEvents" {
  name = "EBPutEvents"

  policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "events:PutEvents",
            "Resource": "arn:aws:events:${var.aws_region}:${local.account_id}:event-bus/${var.eventbus_name}"
        }
    ]
}
POLICY
}

resource "aws_iam_role_policy_attachment" "apigwy_policy" {
  role       = aws_iam_role.ApiGatewayEventBridgeRole.name
  policy_arn = aws_iam_policy.EBPutEvents.arn
}

resource "aws_cloudwatch_event_bus" "integration" {
  name = var.eventbus_name
}

resource "aws_cloudwatch_event_rule" "catch_all" {
    name           = "catch_all"
    description    = "default catch all"
    event_bus_name = aws_cloudwatch_event_bus.integration.name
    event_pattern  = jsonencode(
        {
            account = [
                "${local.account_id}",
            ]
        }
    )
}

resource "aws_cloudwatch_log_group" "log" {
  name = "/aws/events/${aws_cloudwatch_event_bus.integration.name}/${var.eventbus_name}-catch_all"

  retention_in_days = var.catchall_log_retention
}

resource "aws_cloudwatch_event_target" "cw_log" {
  rule      = aws_cloudwatch_event_rule.catch_all.name
  arn       = aws_cloudwatch_log_group.log.arn
  event_bus_name = aws_cloudwatch_event_bus.integration.name
  depends_on = [aws_cloudwatch_log_group.log]
}