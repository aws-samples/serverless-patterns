# create http api gateway
resource "aws_apigatewayv2_api" "http_api" {
  description = var.http_api_description
  name          = var.http_api_name
  protocol_type = "HTTP"
  tags = {
    Name = var.http_api_name
  }
  cors_configuration {
    allow_origins = ["*"]
    allow_methods = ["*"]
    allow_headers = ["*"]
  }
  disable_execute_api_endpoint = local.domain_enabled
}

# create http api gateway route
resource "aws_apigatewayv2_route" "http_api_route" {
  api_id    = aws_apigatewayv2_api.http_api.id
  authorization_type = "CUSTOM"
  authorizer_id = aws_apigatewayv2_authorizer.http_api_auth_authorizer.id
  route_key = "ANY /"
  target = "integrations/${aws_apigatewayv2_integration.http_api_integration.id}"
}

# create http api gateway integration
resource "aws_apigatewayv2_integration" "http_api_integration" {
  api_id           = aws_apigatewayv2_api.http_api.id
  integration_type = "AWS_PROXY"
  description      = "Mock Integration for ${var.http_api_name}"
  integration_method = "POST"
  integration_uri = aws_lambda_function.http_api_lambda.invoke_arn
  passthrough_behavior = "WHEN_NO_MATCH"
  payload_format_version = "2.0"
}

# create http api gateway stage
resource "aws_apigatewayv2_stage" "http_api_stage" {
  api_id = aws_apigatewayv2_api.http_api.id
  name   = var.http_api_stage
  auto_deploy = true
  default_route_settings {
    throttling_burst_limit   = var.throttling_burst_limit
    throttling_rate_limit    = var.throttling_rate_limit
  }
  tags = {
    Name = var.http_api_name
  }
}