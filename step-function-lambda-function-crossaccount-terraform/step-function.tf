#Step function creation

#Creating IAM role for stepfunction
resource "aws_iam_role" "step-function-role" {
    name = "${var.prefix}-stepfunction-function-role"
    
    assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "states.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": "stepfunction"
    }
  ]
}
POLICY

    inline_policy {
        name = "lambda_function_inline_policy"

        policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
            Action   = ["lambda:InvokeFunction"]
            Effect   = "Allow"
            Resource = "${aws_lambda_function.lambda.arn}"
            },
        ]
        })
    }
    provider = aws.default
}



resource "aws_sfn_state_machine" "sfn_state_machine" {
  name = "${var.prefix}-my-state-machine"
  role_arn = aws_iam_role.step-function-role.arn

  definition = <<EOF
{
  "Comment": "A Hello World example of the Amazon States Language using Pass states",
  "StartAt": "LambdaFunction",
  "States": {
    "LambdaFunction": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
        "FunctionName": "${aws_lambda_function.lambda.arn}",
        "Payload": {
          "data.$": "$.payload"
        }
      },
      "End": true
    }
  }
}
EOF
provider = aws.default
}

output "Step_function_ARN" {
    value = "${aws_sfn_state_machine.sfn_state_machine.arn}"
}

output "Step_function_URL" {
    value = "https://${var.region}.console.aws.amazon.com/states/home?region=${var.region}#/statemachines/view/${aws_sfn_state_machine.sfn_state_machine.arn}"
}