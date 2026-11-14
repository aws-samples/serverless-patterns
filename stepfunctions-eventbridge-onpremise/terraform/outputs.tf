output "connection_arn" {
  description = "ARN of the EventBridge connection"
  value       = module.eventbridge_connection.connection_arn
}

output "state_machine_arn" {
  description = "ARN of the Step Functions state machine"
  value = module.state_machine.state_machine_arn
}