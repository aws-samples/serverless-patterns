output "all_rules" {
  value = resource.aws_cloudwatch_event_rule.ebrule
}

output "ebRole" {
  value = aws_iam_role.event_bus_invoke_central_event_bus.arn
}

output "central_bus_arn" {
  value = module.central_eventbridge.eventbridge_bus_arn
}

output "central_bus_rule_arn" {
  value = module.central_eventbridge.eventbridge_rule_arns
}