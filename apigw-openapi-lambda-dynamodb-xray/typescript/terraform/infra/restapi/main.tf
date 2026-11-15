# This code deploys REST api hosted on AWS API Gateway.  
# © 2023 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.  
# This AWS Content is provided subject to the terms of the AWS Customer Agreement available at  
# http://aws.amazon.com/agreement or other written agreement between Customer and either
# Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

resource "aws_api_gateway_rest_api" "this" {
  name        = var.name
  description = var.desc
  body        = var.body
  endpoint_configuration {
    types = ["REGIONAL"]
  }
  lifecycle {
    create_before_destroy = true # CKV_AWS_237
  }
}

resource "aws_api_gateway_deployment" "this" {
  rest_api_id = aws_api_gateway_rest_api.this.id
  triggers = {
    redeployment = sha1(jsonencode(aws_api_gateway_rest_api.this.body))
  }
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_stage" "this" {
  deployment_id = aws_api_gateway_deployment.this.id
  rest_api_id   = aws_api_gateway_rest_api.this.id
  stage_name    = var.stage_name
  dynamic "access_log_settings" {
    for_each = var.access_log_enabled ? [] : [1]
    content {
      destination_arn = aws_cloudwatch_log_group.this[0].arn
      format          = var.log_format
    }
  }
  xray_tracing_enabled = var.xray_tracing_enabled
}

resource "aws_api_gateway_method_settings" "this" {
  rest_api_id = aws_api_gateway_rest_api.this.id
  stage_name  = aws_api_gateway_stage.this.stage_name
  method_path = "*/*"
  settings {
    metrics_enabled    = true
    logging_level      = "INFO"
    data_trace_enabled = true
  }
}

resource "aws_cloudwatch_log_group" "this" {
  count             = var.access_log_enabled ? 1 : 0
  name              = "API-Gateway-Execution-Logs_${aws_api_gateway_rest_api.this.id}/${var.stage_name}"
  kms_key_id        = var.kms_key_id
  retention_in_days = 30
}

# Region wide applicable CloudWatch Role for API Gateway Account
resource "aws_api_gateway_account" "this" {
  cloudwatch_role_arn = aws_iam_role.this.arn
}

# Random id generator
resource "random_id" "id" {
	  byte_length = 8
}

# IAM role to allow API gateway to push CW Logs
resource "aws_iam_role" "this" {
  name               = "api-gateway-cloudwatch-role-${random_id.id.hex}"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

# IAM role policy to allow API gateway to push CW Logs
resource "aws_iam_role_policy" "cloudwatch" {
  name   = "api-gateway-cloudwatch-policy-${random_id.id.hex}"
  role   = aws_iam_role.this.id
  policy = data.aws_iam_policy_document.cloudwatch.json
}