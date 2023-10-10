terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

# Create a zip file from the Lambda source code
data "archive_file" "LambdaZipFile" {
  type        = "zip"
  source_file = "${path.module}/src/LambdaFunction.py"
  output_path = "${path.module}/LambdaFunction.zip"
}

# Create an IAM role for Lambda
resource "aws_iam_role" "LambdaRole" {
  assume_role_policy = <<POLICY1
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Principal" : {
        "Service" : "lambda.amazonaws.com"
      },
      "Action" : "sts:AssumeRole"
    }
  ]
}
POLICY1
}

# Create an IAM policy for Lambda to push CloudWatch Logs
resource "aws_iam_policy" "LambdaPolicy" {
  policy = <<POLICY2
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource" : "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${aws_lambda_function.MyLambdaFunction.function_name}:*:*"
    },
    {
        "Effect": "Allow",
        "Action": [
                "states:StartExecution"
            ],
        "Resource" : "${aws_sfn_state_machine.sfn_state_machine.arn}"
    }
  ]
}
POLICY2
}

# Create an IAM role for Step Functions State Machine
resource "aws_iam_role" "StateMachineRole" {
  assume_role_policy = <<POLICY3
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Principal" : {
        "Service" : "states.amazonaws.com"
      },
      "Action" : "sts:AssumeRole"
    }
  ]
}
POLICY3
}

# Create an IAM policy to enable Step Function State Machine to push logs to CloudWatch logs
resource "aws_iam_policy" "StateMachineLogDeliveryPolicy" {
  policy = <<POLICY4
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "logs:CreateLogDelivery",
        "logs:GetLogDelivery",
        "logs:UpdateLogDelivery",
        "logs:DeleteLogDelivery",
        "logs:ListLogDeliveries",
        "logs:PutResourcePolicy",
        "logs:DescribeResourcePolicies",
        "logs:DescribeLogGroups"
      ],
      "Resource" : "*"
    }
  ]
}
POLICY4
}

# Attach the IAM policies to the equivalent rule
resource "aws_iam_role_policy_attachment" "LambdaPolicyAttachment" {
  role       = aws_iam_role.LambdaRole.name
  policy_arn = aws_iam_policy.LambdaPolicy.arn
}

resource "aws_iam_role_policy_attachment" "StateMachinePolicyAttachment" {
  role       = aws_iam_role.StateMachineRole.name
  policy_arn = aws_iam_policy.StateMachineLogDeliveryPolicy.arn
}

# Create a log group for the Lambda function with 60 days retention period
resource "aws_cloudwatch_log_group" "MyLambdaLogGroup" {
  name              = "/aws/lambda/${aws_lambda_function.MyLambdaFunction.function_name}"
  retention_in_days = 60
}

# Create an Log group for the Step Function
resource "aws_cloudwatch_log_group" "MySFNLogGroup" {
  name_prefix       = "/aws/vendedlogs/states/StateMachine-terraform-"
  retention_in_days = 60
}

# Create the Lambda function with the created Zip file of the source code
resource "aws_lambda_function" "MyLambdaFunction" {
  function_name    = "lambda-sfn-terraform-demo-${data.aws_caller_identity.current.account_id}"
  filename         = data.archive_file.LambdaZipFile.output_path
  source_code_hash = filebase64sha256(data.archive_file.LambdaZipFile.output_path)
  role             = aws_iam_role.LambdaRole.arn
  handler          = "LambdaFunction.lambda_handler"
  runtime          = "python3.9"
  layers           = ["arn:aws:lambda:${data.aws_region.current.name}:017000801446:layer:AWSLambdaPowertoolsPython:15"]

  environment {
    variables = {
      SFN_ARN = aws_sfn_state_machine.sfn_state_machine.arn
    }
  }
}

# Create a Step Function State Machine
resource "aws_sfn_state_machine" "sfn_state_machine" {
  name     = "lambda-sfn-demo-${data.aws_caller_identity.current.account_id}"
  role_arn = aws_iam_role.StateMachineRole.arn

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

  logging_configuration {
    log_destination        = "${aws_cloudwatch_log_group.MySFNLogGroup.arn}:*"
    include_execution_data = true
    level                  = "ALL"
  }
}


output "LambdaFunctionName" {
  value       = aws_lambda_function.MyLambdaFunction.function_name
  description = "The Lambda Function name"
}

output "CloudWatchLogName" {
  value       = "/aws/lambda/${aws_lambda_function.MyLambdaFunction.function_name}"
  description = "The Lambda Function Log Group"
}

output "StepFunction-Name" {
  value       = aws_sfn_state_machine.sfn_state_machine.name
  description = "The Step Function Name"
}