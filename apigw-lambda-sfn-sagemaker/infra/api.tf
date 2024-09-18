# api gateway resources
resource "aws_api_gateway_rest_api" "api" {
  name = "sagemaker-api-provisioning-${data.aws_region.current.name}"
}
# stage
# resource "aws_api_gateway_stage" "dev" {
#   deployment_id = aws_api_gateway_deployment.deployment.id
#   rest_api_id   = aws_api_gateway_rest_api.api.id
#   stage_name    = "dev"
# }
# deployment
resource "aws_api_gateway_deployment" "deployment" {
  rest_api_id = aws_api_gateway_rest_api.api.id
  stage_name  = "dev"
  depends_on  = [aws_api_gateway_integration.app_post]
}

resource "aws_api_gateway_resource" "app" {
  rest_api_id = aws_api_gateway_rest_api.api.id
  parent_id   = aws_api_gateway_rest_api.api.root_resource_id
  path_part   = "app"
}
# post method
resource "aws_api_gateway_method" "app_post" {
  rest_api_id   = aws_api_gateway_rest_api.api.id
  resource_id   = aws_api_gateway_resource.app.id
  http_method   = "POST"
  authorization = "NONE"
}
# integration
resource "aws_api_gateway_integration" "app_post" {
  rest_api_id             = aws_api_gateway_rest_api.api.id
  resource_id             = aws_api_gateway_resource.app.id
  http_method             = aws_api_gateway_method.app_post.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_function.invoke_arn
  credentials             = aws_iam_role.api_gateway_role.arn
}
