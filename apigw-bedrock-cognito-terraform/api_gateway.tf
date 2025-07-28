resource "aws_api_gateway_rest_api" "restAPI" {
  name = "${var.contructID}_rest_api"
  endpoint_configuration {
    types = ["EDGE"]
  }
}

resource "aws_api_gateway_account" "main" {
  cloudwatch_role_arn = aws_iam_role.api_gw_logging.arn
}

resource "aws_api_gateway_stage" "stage" {
  rest_api_id   = aws_api_gateway_rest_api.restAPI.id
  stage_name    = var.stage_name
  deployment_id = aws_api_gateway_deployment.deployment.id

  access_log_settings {
    destination_arn = "arn:aws:logs:${var.region}:${data.aws_caller_identity.current.account_id}:log-group:/aws/apigateway/${var.stage_name}"
    format          = "{\"requestId\":\"$context.requestId\",...}"
  }

  xray_tracing_enabled = true
}

resource "aws_api_gateway_method_settings" "method_settings" {
  rest_api_id = aws_api_gateway_rest_api.restAPI.id
  stage_name  = aws_api_gateway_stage.stage.stage_name

  method_path = "*/*"
  settings {
    metrics_enabled         = true
    logging_level           = "INFO"
    throttling_rate_limit   = var.rate_limit
    throttling_burst_limit  = var.burst_limit
  }
}

resource "aws_api_gateway_usage_plan" "usage_plan" {
  name = "APIUsagePlanID"

  api_stages {
    api_id = aws_api_gateway_rest_api.restAPI.id
    stage  = aws_api_gateway_stage.stage.stage_name
  }

  quota_settings {
    limit  = var.quota_limit
    period = var.quota_period
  }
  throttle_settings {
    burst_limit = var.burst_limit
    rate_limit  = var.rate_limit
  }
}

resource "aws_api_gateway_authorizer" "cognito_authorizer" {
  name            = "CognitoAuthorizer"
  rest_api_id     = aws_api_gateway_rest_api.restAPI.id
  type            = "COGNITO_USER_POOLS"
  provider_arns   = [aws_cognito_user_pool.UserPool.arn]
  identity_source = "method.request.header.Authorization"
}

resource "aws_api_gateway_resource" "register" {
  rest_api_id = aws_api_gateway_rest_api.restAPI.id
  parent_id   = aws_api_gateway_rest_api.restAPI.root_resource_id
  path_part   = "register"
}

resource "aws_api_gateway_method" "register_post" {
  rest_api_id   = aws_api_gateway_rest_api.restAPI.id
  resource_id   = aws_api_gateway_resource.register.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "register_post_integration" {
  rest_api_id             = aws_api_gateway_rest_api.restAPI.id
  resource_id             = aws_api_gateway_resource.register.id
  http_method             = aws_api_gateway_method.register_post.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.auth_lambda_function.invoke_arn
  credentials             = aws_iam_role.api_gw_invoke_role.arn
}

resource "aws_api_gateway_resource" "login" {
  rest_api_id = aws_api_gateway_rest_api.restAPI.id
  parent_id   = aws_api_gateway_rest_api.restAPI.root_resource_id
  path_part   = "login"
}

resource "aws_api_gateway_method" "login_post" {
  rest_api_id   = aws_api_gateway_rest_api.restAPI.id
  resource_id   = aws_api_gateway_resource.login.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "login_post_integration" {
  rest_api_id             = aws_api_gateway_rest_api.restAPI.id
  resource_id             = aws_api_gateway_resource.login.id
  http_method             = aws_api_gateway_method.login_post.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.auth_lambda_function.invoke_arn
  credentials             = aws_iam_role.api_gw_invoke_role.arn
}

resource "aws_api_gateway_resource" "bedrock" {
  rest_api_id = aws_api_gateway_rest_api.restAPI.id
  parent_id   = aws_api_gateway_rest_api.restAPI.root_resource_id
  path_part   = "bedrock"
}

resource "aws_api_gateway_method" "bedrock_any" {
  rest_api_id      = aws_api_gateway_rest_api.restAPI.id
  resource_id      = aws_api_gateway_resource.bedrock.id
  http_method      = "ANY"
  authorization    = "COGNITO_USER_POOLS"
  authorizer_id    = aws_api_gateway_authorizer.cognito_authorizer.id
  api_key_required = true
}

resource "aws_api_gateway_integration" "bedrock_any_integration" {
  rest_api_id             = aws_api_gateway_rest_api.restAPI.id
  resource_id             = aws_api_gateway_resource.bedrock.id
  http_method             = aws_api_gateway_method.bedrock_any.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.bedrock_lambda_function.invoke_arn
  credentials             = aws_iam_role.api_gw_invoke_role.arn
}

resource "aws_api_gateway_deployment" "deployment" {
  rest_api_id = aws_api_gateway_rest_api.restAPI.id

  depends_on = [
    aws_api_gateway_method.register_post,
    aws_api_gateway_integration.register_post_integration,
    aws_api_gateway_method.login_post,
    aws_api_gateway_integration.login_post_integration,
    aws_api_gateway_method.bedrock_any,
    aws_api_gateway_integration.bedrock_any_integration
  ]

  triggers = {
    redeploy = sha256(jsonencode(aws_api_gateway_rest_api.restAPI))
  }
}

resource "aws_ssm_parameter" "usage_play_id" {
  name        = "/${var.contructID}/api/usage_plan/id" 
  description = "ID of API gateway usage plan"
  type        = "String"
  value       = aws_api_gateway_usage_plan.usage_plan.id
}
