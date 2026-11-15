# Output value definitions

output "websocket_URI" {
  description = "API Gateway websocket endpoint URL for Prod stage"

  value = aws_apigatewayv2_stage.production.invoke_url
}

output "Queue" {
  description = "SQS FIFO queue which receives the websocket message events"
  value = aws_sqs_queue.fifo_queue.id
}

output "lambda_log_group" {
  description = "Name of the CloudWatch logs group for the lambda function"
  value = aws_cloudwatch_log_group.lambda_logs.id
}


