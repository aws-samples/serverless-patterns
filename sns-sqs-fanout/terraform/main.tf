provider "aws" {
  region = "us-east-1"
}

# Create an SNS topic
resource "aws_sns_topic" "MetricsSnsTopic" {
  name = "MetricsSnsTopic"
  display_name = "MetricsSnsTopic"
}

# Define SQS Queues
resource "aws_sqs_queue" "AllMetricsSqsQueue" {
  name = "AllMetricsSqsQueue"
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.MetricsSqsDLQueue.arn
    maxReceiveCount     = 5
  })
}

resource "aws_sqs_queue" "TemperatureSqsQueue" {
  name = "TemperatureSqsQueue"
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.TemperatureSqsDLQueue.arn
    maxReceiveCount     = 5
  })
}

resource "aws_sqs_queue" "HumiditySqsQueue" {
  name = "HumiditySqsQueue"
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.HumiditySqsDLQueue.arn
    maxReceiveCount     = 5
  })
}

# Define dead letter queues
resource "aws_sqs_queue" "MetricsSqsDLQueue" {
  name = "MetricsSqsDLQueue"
}

resource "aws_sqs_queue" "TemperatureSqsDLQueue" {
  name = "TemperatureSqsDLQueue"
}

resource "aws_sqs_queue" "HumiditySqsDLQueue" {
  name = "HumiditySqsDLQueue"
}

# SNS to SQS Policy
resource "aws_sqs_queue_policy" "SnsToSqsPolicy" {
  queue_url = aws_sqs_queue.AllMetricsSqsQueue.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "Allow SNS publish to SQS"
        Effect    = "Allow"
        Principal = "*"
        Action    = "sqs:SendMessage"
        Resource  = aws_sqs_queue.AllMetricsSqsQueue.arn

        Condition = {
          ArnEquals = {
            "aws:SourceArn" = aws_sns_topic.MetricsSnsTopic.arn
          }
        }
      },
    ]
  })
}

# Access policy for TemperatureSqsQueue
resource "aws_sqs_queue_policy" "TemperatureSqsQueuePolicy" {
  queue_url = aws_sqs_queue.TemperatureSqsQueue.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "Allow SNS publish to TemperatureSqsQueue"
        Effect    = "Allow"
        Principal = "*"
        Action    = "sqs:SendMessage"
        Resource  = aws_sqs_queue.TemperatureSqsQueue.arn

        Condition = {
          ArnEquals = {
            "aws:SourceArn" = aws_sns_topic.MetricsSnsTopic.arn
          }
        }
      },
    ]
  })
}

# Access policy for HumiditySqsQueue
resource "aws_sqs_queue_policy" "HumiditySqsQueuePolicy" {
  queue_url = aws_sqs_queue.HumiditySqsQueue.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "Allow SNS publish to HumiditySqsQueue"
        Effect    = "Allow"
        Principal = "*"
        Action    = "sqs:SendMessage"
        Resource  = aws_sqs_queue.HumiditySqsQueue.arn

        Condition = {
          ArnEquals = {
            "aws:SourceArn" = aws_sns_topic.MetricsSnsTopic.arn
          }
        }
      },
    ]
  })
}

# Define SNS Subscriptions
resource "aws_sns_topic_subscription" "MetricsQueueSubscription" {
  topic_arn = aws_sns_topic.MetricsSnsTopic.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.AllMetricsSqsQueue.arn
  raw_message_delivery = true
}

resource "aws_sns_topic_subscription" "TemperatureSqsQueueSubscription" {
  topic_arn            = aws_sns_topic.MetricsSnsTopic.arn
  protocol             = "sqs"
  endpoint             = aws_sqs_queue.TemperatureSqsQueue.arn
  raw_message_delivery = true
  filter_policy        = jsonencode({
    MetricType = ["Temperature"]
  })
}

resource "aws_sns_topic_subscription" "HumiditySqsQueueSubscription" {
  topic_arn            = aws_sns_topic.MetricsSnsTopic.arn
  protocol             = "sqs"
  endpoint             = aws_sqs_queue.HumiditySqsQueue.arn
  raw_message_delivery = true
  filter_policy        = jsonencode({
    MetricType = ["Humidity"]
  })
}

# Outputs
output "SNStopicName" {
  value = aws_sns_topic.MetricsSnsTopic.name
}

output "SNStopicARN" {
  value = aws_sns_topic.MetricsSnsTopic.arn
}

output "AllMetricsSqsQueueName" {
  value = aws_sqs_queue.AllMetricsSqsQueue.name
}

output "AllMetricsSqsQueueArn" {
  value = aws_sqs_queue.AllMetricsSqsQueue.arn
}

output "AllMetricsSqsQueueURL" {
  value = aws_sqs_queue.AllMetricsSqsQueue.id
}

output "TemperatureSqsQueueName" {
  value = aws_sqs_queue.TemperatureSqsQueue.name
}

output "TemperatureSqsQueueArn" {
  value = aws_sqs_queue.TemperatureSqsQueue.arn
}

output "TemperatureSqsQueueURL" {
  value = aws_sqs_queue.TemperatureSqsQueue.id
}

output "HumiditySqsQueueName" {
  value = aws_sqs_queue.HumiditySqsQueue.name
}

output "HumiditySqsQueueArn" {
  value = aws_sqs_queue.HumiditySqsQueue.arn
}

output "HumiditySqsQueueURL" {
  value = aws_sqs_queue.HumiditySqsQueue.id
}
