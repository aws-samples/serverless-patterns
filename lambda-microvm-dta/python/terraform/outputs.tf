output "artifact_bucket_name" {
  description = "S3 bucket for artifacts and reports."
  value       = aws_s3_bucket.artifacts.bucket
}

output "build_role_arn" {
  description = "Pass to `microvm-dta build-image --build-role-arn`."
  value       = aws_iam_role.build.arn
}

output "execution_role_arn" {
  description = "Pass to `microvm-dta run --execution-role-arn`."
  value       = aws_iam_role.execution.arn
}

output "github_actions_role_arn" {
  description = "Optional GitHub Actions OIDC role ARN (only when enable_github_oidc_role = true)."
  value       = var.enable_github_oidc_role ? aws_iam_role.ci[0].arn : null
}

output "vpc_id" {
  description = "Egress VPC id (when enable_vpc_egress = true)."
  value       = var.enable_vpc_egress ? aws_vpc.egress[0].id : null
}

output "egress_security_group_id" {
  description = "Restricted egress security group id (when enable_vpc_egress = true)."
  value       = var.enable_vpc_egress ? aws_security_group.egress[0].id : null
}

output "private_subnet_id" {
  description = "Private subnet id for MicroVM VPC egress (when enable_vpc_egress = true)."
  value       = var.enable_vpc_egress ? aws_subnet.private[0].id : null
}

output "flow_logs_log_group" {
  description = "CloudWatch log group for VPC Flow Logs (when enabled)."
  value       = var.enable_vpc_egress && var.enable_vpc_flow_logs ? aws_cloudwatch_log_group.flow_logs[0].name : null
}
