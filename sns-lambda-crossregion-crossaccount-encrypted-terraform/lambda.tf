resource "aws_lambda_permission" "sns_permission" {
  statement_id  = "AllowExecutionFromStepFunction"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.lambda.function_name}"
  principal = "sns.amazonaws.com"
  source_arn = "${aws_sns_topic.test.arn}"
  provider = aws.crossaccount
}

resource "aws_lambda_function" "lambda" {
  filename      = "lambdacode.zip"
  function_name = "sns-lambda"
  role          = aws_iam_role.role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"

  source_code_hash = filebase64sha256("lambdacode.zip")
  provider = aws.crossaccount
}

#Creating IAM role for lambda
resource "aws_iam_role" "role" {
  name = "sns-lambda-function-role"
 managed_policy_arns = [data.aws_iam_policy.ReadOnlyAccess.arn]
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

data "aws_iam_policy" "ReadOnlyAccess" {
    arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  }

resource "aws_iam_role_policy" "kms_policy" {
  name = "kms_policy"
  role = aws_iam_role.role.id

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "kms:*"
        ]
        Effect   = "Allow"
        Resource = "${aws_kms_key.kms.arn}"
      }
    ]
  })
  provider = aws.crossaccount
}

resource "aws_iam_role_policy" "sns_policy" {
    name = "sns_policy"
    role = aws_iam_role.role.id
  
    # Terraform's "jsonencode" function converts a
    # Terraform expression result to valid JSON syntax.
    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Action = [
            "sns:*"
          ]
          Effect   = "Allow"
          Resource = "${aws_sns_topic.test.arn}"
          
        }
      ]
    })
    provider = aws.crossaccount
  }

resource "aws_sns_topic_subscription" "sns-topic" {
    provider  = aws.snscrossaccount
    topic_arn = aws_sns_topic.test.arn
    protocol  = "lambda"
    endpoint  = aws_lambda_function.lambda.arn
  }