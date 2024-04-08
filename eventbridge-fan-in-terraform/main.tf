locals {
  account_id = data.aws_caller_identity.current.account_id
}

// Loop over all Eventbus and create rule for each
resource "aws_cloudwatch_event_rule" "ebrule" {
  provider = aws.others
  for_each = nonsensitive(toset(var.buses))
  event_bus_name = each.value
  event_pattern = jsonencode({
    account = [
      local.account_id
    ]
  })
  is_enabled = true
}

//IAM role and policy for Event rule
resource "aws_iam_role" "event_bus_invoke_central_event_bus" {
  name               = "event-bus-invoke-central-event-bus"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

resource "aws_iam_policy" "event_bus_invoke_central_event_bus" {
  name   = "event_bus_invoke_central_event_bus_policy"
  policy = data.aws_iam_policy_document.event_bus_invoke_central_event_bus_policy.json
}

resource "aws_iam_role_policy_attachment" "event_bus_invoke_central_event_bus" {
  role       = aws_iam_role.event_bus_invoke_central_event_bus.name
  policy_arn = aws_iam_policy.event_bus_invoke_central_event_bus.arn
}


// Create Cloudwatch log group for central bus
resource "aws_cloudwatch_log_group" "log-group" {
  provider = aws.central
  name  = "/aws/events/central-bus-logs/logs"
  retention_in_days =  7  
}

// Create log policy
data "aws_iam_policy_document" "log_policy" {
  depends_on = [ module.central_eventbridge ]
  statement {
    effect = "Allow"
    actions = [
      "logs:CreateLogStream"
    ]

    resources = [
      "${aws_cloudwatch_log_group.log-group.arn}:*"
    ]

    principals {
      type = "Service"
      identifiers = [
        "events.amazonaws.com",
        "delivery.logs.amazonaws.com"
      ]
    }
 }
  statement {
    effect = "Allow"
    actions = [
      "logs:PutLogEvents"
    ]

    resources = [
      "${aws_cloudwatch_log_group.log-group.arn}:*:*"
    ]

    principals {
      type = "Service"
      identifiers = [
        "events.amazonaws.com",
        "delivery.logs.amazonaws.com"
      ]
    }
    condition {
      test     = "ArnEquals"
      values   = [module.central_eventbridge.eventbridge_rule_arns.log-rule]
      variable = "aws:SourceArn"
    }
  }
}

resource "aws_cloudwatch_log_resource_policy" "log-resource-policy" {
  policy_document = data.aws_iam_policy_document.log_policy.json
  policy_name     = "eventbridge-log-publishing-policy"
}

//Use Eventbridge module to create Central Eventbus
module "central_eventbridge" {
  providers = {
    aws = aws.central
  }
  source = "terraform-aws-modules/eventbridge/aws"

  bus_name = "central-event-bus"

  rules = {
    log-rule={
        name          = "central-bus-event-rule"
        description   = "Send all events from Central Eventbus to Cloudwatch logs"
        event_bus_name = "central-event-bus"
        event_pattern = jsonencode({
          account = [
          local.account_id
          ]
          })
        enabled = true
     }
  }

  targets = {
    log-rule = [
      {
        name = "send-logs-to-cloudwatch"
        arn  = aws_cloudwatch_log_group.log-group.arn
      }
    ]
  }
  tags = {
    Name = "my-bus"
  }
}

//Create targets on each rule to send events to Central Eventbus
resource "aws_cloudwatch_event_target" "EBtargets" {
  for_each       = tomap(aws_cloudwatch_event_rule.ebrule)
  event_bus_name = each.key
  rule           = each.value.name
  arn            = module.central_eventbridge.eventbridge_bus_arn
  role_arn       = aws_iam_role.event_bus_invoke_central_event_bus.arn
}