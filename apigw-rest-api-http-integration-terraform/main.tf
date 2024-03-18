provider "aws" {
  region = "us-east-1" # Update with your desired region
}
resource "aws_api_gateway_rest_api" "AppApi" {
  name        = "apigw-rest-api-http-integration"
  description = "HTTP Integration REST API demo"
}
resource "aws_api_gateway_method" "RootMethodGet" {
  rest_api_id   = aws_api_gateway_rest_api.AppApi.id
  resource_id   = aws_api_gateway_rest_api.AppApi.root_resource_id
  http_method   = "GET"
  authorization = "NONE"
}
resource "aws_api_gateway_integration" "Integration" {
  rest_api_id = aws_api_gateway_rest_api.AppApi.id
  resource_id = aws_api_gateway_method.RootMethodGet.resource_id
  http_method = aws_api_gateway_method.RootMethodGet.http_method
  type        = "HTTP_PROXY"
  
  # Replace the following url with your own HTTP url
  uri                     = "http://petstore-demo-endpoint.execute-api.com/petstore/pets"
  integration_http_method = "GET"
  depends_on              = [aws_api_gateway_method.RootMethodGet]
}
resource "aws_api_gateway_deployment" "Deployment" {
  rest_api_id = aws_api_gateway_rest_api.AppApi.id
  depends_on  = [aws_api_gateway_integration.Integration]
}
resource "aws_api_gateway_stage" "Stage" {
  stage_name    = "Prod"
  rest_api_id   = aws_api_gateway_rest_api.AppApi.id
  deployment_id = aws_api_gateway_deployment.Deployment.id
}

