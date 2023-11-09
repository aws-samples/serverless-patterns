//SQS ARN
output "sqs_arn" {
    value       = aws_sqs_queue.sqs_deadletter.arn
    description = "sqs_arn"
}