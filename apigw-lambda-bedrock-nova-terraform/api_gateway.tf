resource "aws_api_gateway_rest_api" "generate_content_api" {
  name = "generate-content-api"
}

resource "aws_api_gateway_resource" "generate_content" {
  rest_api_id = aws_api_gateway_rest_api.generate_content_api.id
  parent_id   = aws_api_gateway_rest_api.generate_content_api.root_resource_id
  path_part   = "generate_content"
}

resource "aws_api_gateway_method" "generate_content_post" {
  rest_api_id   = aws_api_gateway_rest_api.generate_content_api.id
  resource_id   = aws_api_gateway_resource.generate_content.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "lambda_integration" {
  rest_api_id = aws_api_gateway_rest_api.generate_content_api.id
  resource_id = aws_api_gateway_resource.generate_content.id
  http_method = aws_api_gateway_method.generate_content_post.http_method
  
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.content_generation.invoke_arn
}

resource "aws_api_gateway_deployment" "api_deployment" {
  rest_api_id = aws_api_gateway_rest_api.generate_content_api.id
  
  depends_on = [
    aws_api_gateway_integration.lambda_integration
  ]

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_stage" "dev" {
  deployment_id = aws_api_gateway_deployment.api_deployment.id
  rest_api_id   = aws_api_gateway_rest_api.generate_content_api.id
  stage_name    = "dev"
}
