//SQS Queue with deadletter queue
resource "aws_sqs_queue" "sqs_queue" {
  name                      = "sqs-queue"
  delay_seconds             = 90
  max_message_size          = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10
  tags = {
    Environment = "production"
  }
  redrive_policy             = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.sqs_deadletter.arn
    maxReceiveCount     = 10
  })
}

resource "aws_sqs_queue" "sqs_deadletter" {
  name = "sqs-deadletter-queue"
 
}
