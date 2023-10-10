# Output value definitions

output "apigwy_url" {
  description = "URL for API Gateway stage"

  value = aws_api_gateway_stage.Stage.invoke_url
}