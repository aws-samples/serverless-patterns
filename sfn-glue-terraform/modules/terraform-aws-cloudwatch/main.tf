locals{
  schedule_expression= "rate(10 minutes)"
}

# Variables
variable "stf_function_name" {}
variable "stf_function_arn" {}

# Resources

data "aws_iam_policy_document" "allow_cloudwatch_to_execute_policy" {
  statement {
    actions = [
      "sts:AssumeRole"
    ]

    principals {
      type = "Service"
      identifiers = [
        "states.amazonaws.com",
        "events.amazonaws.com"
      ]
    }
  }
}

resource "aws_iam_role" "allow_cloudwatch_to_execute_role" {
  name               = "aws-events-invoke-StepFunction"
  assume_role_policy = data.aws_iam_policy_document.allow_cloudwatch_to_execute_policy.json
}

resource "aws_iam_role_policy" "state_execution" {
  name        = "state_execution_policy"
  role   = aws_iam_role.allow_cloudwatch_to_execute_role.id

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1647307985962",
      "Action": [
        "states:StartExecution"
      ],
      "Effect": "Allow",
      "Resource": "${var.stf_function_arn}"
    }
  ]
}
EOF
}

resource "aws_cloudwatch_event_rule" "stf_trigger_rule" {
  name = "stf_trigger_rule"
  schedule_expression = local.schedule_expression
  description = "Sample Event for Glue terraform example"
}

resource "aws_cloudwatch_event_target" "cloudwatch_event_target" {
  rule = aws_cloudwatch_event_rule.stf_trigger_rule.name
  arn = var.stf_function_arn
  role_arn = aws_iam_role.allow_cloudwatch_to_execute_role.arn
}

# Outputs
output "aws_cloudwatch_event_rule_arn" {
  value = aws_cloudwatch_event_rule.stf_trigger_rule.arn
}