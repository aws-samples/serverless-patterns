# Output value definitions

output "apigwy_url" {
  description = "URL for API Gateway stage"

  value = aws_apigatewayv2_api.lambda.api_endpoint
}
