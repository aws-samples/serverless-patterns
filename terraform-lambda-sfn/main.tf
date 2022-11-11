provider "aws" {
  region = "eu-west-1"
}

data "aws_region" "current" {}

locals {
  definition = <<SFN
{
  "Comment": "State Machine example with various state types",
  "StartAt": "Pass State",
  "States": {
    "Pass State": {
      "Comment": "A Pass state passes its input to its output, without performing work. Pass states are useful when constructing and debugging state machines.",
      "Type": "Pass",
      "Next": "Wait State"
    },
    "Wait State": {
      "Comment": "A Wait state delays the state machine from continuing for a specified time. You can choose either a relative time, specified in seconds from when the state begins, or an absolute end time, specified as a timestamp.",
      "Type": "Wait",
      "Seconds": 3,
      "Next": "Choice State"
    },
    "Choice State": {
      "Comment": "A Choice state adds branching logic to a state machine.",
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.Choice",
          "StringEquals": "A",
          "Next": "Succeed State"
        },
        {
          "Variable": "$.Choice",
          "StringEquals": "B",
          "Next": "Parallel State"
        }
      ],
      "Default": "Error Handling State"
    },
    "Parallel State": {
      "Comment": "A Parallel state can be used to create parallel branches of execution in your state machine.",
      "Type": "Parallel",
      "Next": "Succeed State",
      "Branches": [
        {
          "StartAt": "Branch 1",
          "States": {
            "Branch 1": {
              "Type": "Pass",
              "Parameters": {
                "comment.$": "States.Format('Branch 1 Processing of Choice {}', $.Choice)"
              },
              "End": true
            }
          }
        },
        {
          "StartAt": "Branch 2",
          "States": {
            "Branch 2": {
              "Type": "Pass",
              "Parameters": {
                "comment.$": "States.Format('Branch 2 Processing of Choice {}', $.Choice)"
              },
              "End": true
            }
          }
        }
      ]
    },
    "Succeed State": {
      "Type": "Succeed",
      "Comment": "A Succeed state stops an execution successfully. The Succeed state is a useful target for Choice state branches that don't do anything but stop the execution."
    },
    "Error Handling State": {
      "Type": "Pass",
      "Parameters": {
        "error.$": "States.Format('{} is an invalid Choice.',$.Choice)"
      },
      "Next": "Fail State"
    },
    "Fail State": {
      "Type": "Fail"
    }
  }
}
SFN
}

####################################################
# Lambda Function (building from source)
####################################################

module "lambda_function" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "~> 4.0"

  function_name = "${random_pet.this.id}-lambda"
  description   = "My awesome lambda function"
  handler       = "LambdaFunction.lambda_handler"
  runtime       = "python3.8"
  publish       = true

  source_path = "${path.module}/src"

  layers = ["arn:aws:lambda:${data.aws_region.current.name}:017000801446:layer:AWSLambdaPowertoolsPython:15"]

  environment_variables = {
    SFN_ARN = module.step_function.state_machine_arn
  }

  attach_policy_statements = true
  policy_statements = {
    step_function = {
      effect    = "Allow",
      actions   = ["states:StartExecution"],
      resources = [module.step_function.state_machine_arn]
    }
  }

  tags = {
    Pattern = "terraform-lambda-sfn"
    Module  = "lambda_function"
  }
}

################
# Step Function
################

module "step_function" {
  source  = "terraform-aws-modules/step-functions/aws"
  version = "~> 2.0"

  name       = random_pet.this.id
  definition = local.definition

  logging_configuration = {
    include_execution_data = true
    level                  = "ALL"
  }

  service_integrations = {
    lambda = {
      lambda = [module.lambda_function.lambda_function_arn_static]
    }

    xray = {
      xray = true
    }
  }

  tags = {
    Pattern = "terraform-lambda-sfn"
    Module  = "step_function"
  }
}

##################
# Extra resources
##################

resource "random_pet" "this" {
  length = 2
}
