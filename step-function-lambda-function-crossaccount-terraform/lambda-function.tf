# while adding permissions to the lambda function it needs the step function IAM role so 
# sometime is required for role to populate globally and become available.
resource "time_sleep" "wait_10_seconds" {
  depends_on = [aws_iam_role.step-function-role]
  create_duration = "10s"
}

#Ceating Lambda
resource "aws_lambda_permission" "step_function_lambda" {
  statement_id  = "AllowExecutionFromStepFunction"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.lambda.function_name}"
  principal = "${aws_iam_role.step-function-role.arn}"
  provider = aws.crossaccount
  depends_on = [
    time_sleep.wait_10_seconds
  ]
}

resource "aws_lambda_function" "lambda" {
  filename      = "lambdacode.zip"
  function_name = "${var.prefix}-step-function-lambda"
  role          = aws_iam_role.role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"

  source_code_hash = filebase64sha256("lambdacode.zip")
  provider = aws.crossaccount
}

#Creating IAM role for lambda
resource "aws_iam_role" "role" {
  name = "${var.prefix}-lambda-function-role"

  assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
POLICY
provider = aws.crossaccount
}