output "cognito_user_pool" {
  value       = aws_cognito_user_pool.UserPool.id
  description = "CognitoUserPoolID"
}

output "Endpoint_URL" {
  value       = aws_api_gateway_stage.stage.invoke_url
  description = "Root Resource ID for the API"
}
