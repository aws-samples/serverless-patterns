resource "time_sleep" "wait_10_seconds" {
  depends_on = [aws_iam_role.role]
  create_duration = "10s"
}

#Ceating Lambda
resource "aws_lambda_permission" "sns_lambda" {
  statement_id  = "AllowExecutionFromStepFunction"
  action        = "lambda:InvokeFunction"
  function_name = "${var.lambdaName}"
  principal = "sns.amazonaws.com"
  source_arn = aws_sns_topic.topic.arn
  provider = aws.crossaccount
  depends_on = [
    time_sleep.wait_10_seconds
  ]
}

resource "aws_lambda_function" "lambda" {
  filename      = "lambdacode.zip"
  function_name = "${var.lambdaName}"
  role          = aws_iam_role.role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"

  source_code_hash = filebase64sha256("lambdacode.zip")
  provider = aws.crossaccount
}

#Creating IAM role for lambda
resource "aws_iam_role" "role" {
  name = "${var.lambdaName}-role"

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