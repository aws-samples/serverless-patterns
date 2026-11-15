output "primary_console"{
  value = aws_mq_broker.primary.instances.0.console_url 
}

output "secondary_console"{
  value = aws_mq_broker.secondary.instances.0.console_url 
}

output "primary_endpoint"{
    value = aws_mq_broker.primary.instances.0.endpoints.0
}

output "secondary_endpoint"{
    value = aws_mq_broker.secondary.instances.0.endpoints.0
}