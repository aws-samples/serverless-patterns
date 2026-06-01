output "connection_arn" {
  description = "ARN of the EventBridge connection"
  value       = aws_cloudwatch_event_connection.on_premise_connection.arn
}

output "connection_secret_arn" {
  description = "ARN of the secret for EventBridge connection"
  value       = aws_cloudwatch_event_connection.on_premise_connection.secret_arn
}

