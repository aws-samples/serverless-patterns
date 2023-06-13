resource "aws_sns_topic" "test" {
  name              = "sns-test-topic"
  kms_master_key_id = "alias/${var.kmsAlias}"
  provider = aws.default
}

resource "aws_sns_topic_policy" "default" {
  arn = aws_sns_topic.test.arn
  policy = data.aws_iam_policy_document.sns_topic_policy.json
  provider = aws.default
}

data "aws_iam_policy_document" "sns_topic_policy" {
  policy_id = "__default_policy_ID"

  statement {
    actions = [
      "SNS:Subscribe",
      "SNS:ListSubscriptionsByTopic"
    ]

    effect = "Allow"

    principals {
      type        = "AWS"
      identifiers = ["arn:aws:iam::${var.lambdaAccountId}:root"]
    }

    resources = [
      aws_sns_topic.test.arn,
    ]

    sid = "__default_statement_ID"
  }
  provider = aws.default
}
