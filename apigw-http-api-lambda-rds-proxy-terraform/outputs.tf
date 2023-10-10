# Output value definitions

output "apigwy_url" {
  description = "URL for API Gateway"

  value = aws_apigatewayv2_stage.lambda.invoke_url
}

output "lambda_function_log" {
  value = aws_cloudwatch_log_group.rds_proxy_function.id
}