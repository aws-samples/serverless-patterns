resource "aws_sns_topic" "topic" {
  name = "${var.topicName}"
  provider = aws.default
}

resource "aws_sns_topic_policy" "lambdapolicy" {
  arn = aws_sns_topic.topic.arn
  provider = aws.default
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid = "lambda-access"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${var.lambdaAccountId}:root"
        }
        Action = [
          "SNS:Subscribe",
          "SNS:ListSubscriptionsByTopic"
        ]
        Resource = aws_sns_topic.topic.arn
      }
    ]
  })
}




resource "aws_sns_topic_subscription" "lambda_target" {
  depends_on = [aws_sns_topic_policy.lambdapolicy]
  topic_arn = aws_sns_topic.topic.arn
  protocol  = "lambda"
  endpoint  = aws_lambda_function.lambda.arn
  provider = aws.snssub
}