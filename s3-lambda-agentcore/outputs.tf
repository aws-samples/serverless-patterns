# Output value definitions

output "lambda_arn" {
  description = "Lambda"
  value = aws_lambda_function.s3_agent_lambda_function.arn
}

output "agent_arn" {
  description = "Agent"
  value = aws_bedrockagentcore_agent_runtime.agentcore_runtime.agent_runtime_arn
}

output "s3_input_bucket" {
    description = "S3_input_bucket"
    value = aws_s3_bucket.input_bucket.id
}

output "s3_output_bucket" {
    description = "S3_output_bucket"
    value = aws_s3_bucket.output_bucket.id
}