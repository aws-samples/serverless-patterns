output "state_machine_arn" {
  description = "ARN of the Step Functions state machine"
  value       = aws_sfn_state_machine.state_machine.arn
}

output "role_arn" {
  description = "ARN of the IAM role used by the state machine"
  value       = aws_iam_role.state_machine.arn
}

output "log_group_name" {
  description = "Name of the CloudWatch Log Group for the state machine"
  value       = aws_cloudwatch_log_group.state_machine.name
}
