data "aws_caller_identity" "current" {}

data "aws_iam_policy_document" "event_bus_invoke_central_event_bus_policy" {
  statement {
    effect    = "Allow"
    actions   = ["events:PutEvents"]
    resources = ["*"]
  }
}

data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["events.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}