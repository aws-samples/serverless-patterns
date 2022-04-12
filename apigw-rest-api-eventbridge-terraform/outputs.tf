# Output value definitions

output "apigwy_url" {
  description = "URL for API Gateway stage"
  value = aws_api_gateway_stage.dev.invoke_url
}

output "catch_all_log" {
  description = "cw log for event bridge rule"
  value =  aws_cloudwatch_log_group.log.id
}