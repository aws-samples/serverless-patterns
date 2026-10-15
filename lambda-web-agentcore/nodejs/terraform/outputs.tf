output "app_url" {
  description = "Open this URL in a browser to use the chat app (served through Amazon CloudFront)."
  value       = "https://${aws_cloudfront_distribution.webapp.domain_name}/"
}

output "web_function_endpoint_url" {
  description = "The Lambda Web Function endpoint. Direct requests are rejected with HTTP 403, because they do not come through CloudFront."
  value       = "https://${awscc_lambda_web_function_endpoint.webapp.domain_name}/"
}

output "login_secret_arn" {
  description = "ARN of the AWS Secrets Manager secret that holds the chat app's login secret."
  value       = aws_secretsmanager_secret.login.arn
}

output "web_function_name" {
  description = "Name of the Lambda Web Function."
  value       = awscc_lambda_web_function.webapp.function_name
}

output "agent_runtime_arn" {
  description = "ARN of the Amazon Bedrock AgentCore runtime that hosts the agent."
  value       = aws_bedrockagentcore_agent_runtime.agent.agent_runtime_arn
}

output "model_id" {
  description = "Amazon Bedrock inference profile that the agent uses."
  value       = local.model_id
}
