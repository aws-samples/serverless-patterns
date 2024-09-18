# create an iam role for sagemaker execution
resource "aws_iam_role" "sagemaker_role" {
  name = "serverless-sagemaker-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "sagemaker.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role" "lambda_role" {
  name = "serverless-lambda-role"

  assume_role_policy = <<EOF
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
EOF

  inline_policy {
    name   = "sagemaker-permissions"
    policy = data.aws_iam_policy_document.example.json
  }

}

data "aws_iam_policy_document" "example" {
  statement {
    sid = "1"

    actions = [
      "sagemaker:*"
    ]

    resources = [
      "*"
    ]
  }
  statement {
    sid = "2"
    actions = [
      "iam:PassRole"
    ]
    resources = [
      "arn:aws:iam::${data.aws_caller_identity.current.id}:role/serverless-sagemaker-role"
    ]
  }

  statement {
    sid = "3"
    actions = [
      "states:StartExecution",
    ]
    resources = [
      "${aws_sfn_state_machine.manage_sagemaker.arn}"
    ]
  }
}

# attach cloudwatch managed policy to lambda role
resource "aws_iam_role_policy_attachment" "lambda_cloudwatch" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# stepfunctions role
data "aws_iam_policy_document" "stepfunctions_policy" {
  statement {
    sid = "1"

    actions = [
      "sagemaker:DescribeDomain"
    ]

    resources = [
      "*"
    ]
  }
}
resource "aws_iam_role" "stepfunctions_role" {
  name = "serverless-stepfunctions-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "states.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF

  inline_policy {
    name   = "sagemaker-permissions"
    policy = data.aws_iam_policy_document.stepfunctions_policy.json
  }
}

# iam role for api gateway
resource "aws_iam_role" "api_gateway_role" {
  name = "serverless-api-gateway-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "apigateway.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}


# attach permissions to sagemaker role to invoke lambda function
resource "aws_iam_role_policy_attachment" "sagemaker_lambda_invoke" {
  role       = aws_iam_role.api_gateway_role.name
  policy_arn = aws_iam_policy.lambda_invoke.arn
}
# create policy for lambda invoke
resource "aws_iam_policy" "lambda_invoke" {
  name        = "lambda-invoke"
  path        = "/"
  description = "Allow lambda invoke"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "lambda:InvokeFunction"
      ],
      "Effect": "Allow",
      "Resource": ["${aws_lambda_function.lambda_function.arn}"]
    }
  ]
}
EOF
}
