output "webhook_url" {
  description = "GitHub webhook Payload URL. Content type: application/json."
  value       = "${aws_api_gateway_stage.webhook.invoke_url}/webhook"
}

output "pat_secret_arn" {
  description = "Secret to store the GitHub PAT in (aws secretsmanager put-secret-value)."
  value       = aws_secretsmanager_secret.pat.arn
}

output "webhook_secret_arn" {
  description = "Secret to store the webhook HMAC secret in; use the same value in the GitHub webhook."
  value       = aws_secretsmanager_secret.webhook.arn
}

output "microvm_image_arn" {
  description = "MicroVM runner image the webhook launches. RunMicrovm uses its latest active version."
  value       = aws_cloudformation_stack.microvm_image.outputs["ImageArn"]
}

output "artifacts_bucket_name" {
  description = "S3 bucket holding the MicroVM image zip and the per-job JIT configs."
  value       = aws_s3_bucket.artifacts.id
}

output "microvm_runtime_log_group" {
  description = "CloudWatch log group with the supervisor and runner output of each MicroVM."
  value       = aws_cloudwatch_log_group.microvm_runtime.name
}

output "region" {
  description = "Region the stack is deployed in."
  value       = var.region
}

output "name_prefix" {
  description = "Resource name prefix; the runner image is <name_prefix>-runner-image."
  value       = var.name_prefix
}
