provider "aws" {
  region = "eu-west-1"
}

module "eventbridge" {
  source  = "terraform-aws-modules/eventbridge/aws"
  version = "~> 1.0"

  # ScheduleExpression is supported only on the default event bus.
  create_bus = false

  rules = {
    crons = {
      description         = "Trigger a Lambda Function periodically"
      schedule_expression = "rate(1 minute)"
    }
  }

  targets = {
    crons = [
      {
        name  = "lambda-loves-cron"
        arn   = module.lambda_function.lambda_function_arn
        input = jsonencode({ "job" : "cron-by-rate" })
      }
    ]
  }

  tags = {
    Pattern = "terraform-eventbridge-scheduled-lambda"
    Module  = "eventbridge"
  }
}

#############################################
# Lambda Function (building package locally)
#############################################

module "lambda_function" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "~> 4.0"

  function_name = "${random_pet.this.id}-lambda"
  description   = "My awesome lambda function"
  handler       = "index.lambda_handler"
  runtime       = "python3.8"
  publish       = true

  source_path = "${path.module}/../terraform-fixtures/python"

  allowed_triggers = {
    ScheduledEventBridgeRule = {
      principal  = "events.amazonaws.com"
      source_arn = module.eventbridge.eventbridge_rule_arns["crons"]
    }
  }

  tags = {
    Pattern = "terraform-eventbridge-scheduled-lambda"
    Module  = "lambda_function"
  }
}

##################
# Extra resources
##################

resource "random_pet" "this" {
  length = 2
}
