# Lambda functions and related IAM roles/policies

resource "aws_iam_role" "auth_lambda_execution_role" {
  name = "auth_function_execution_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action: "sts:AssumeRole",
        Effect: "Allow",
        Principal: { Service: "lambda.amazonaws.com" }
      }
    ]
  })
}

resource "aws_iam_policy" "auth_lambda_execution_policy" {
  name = "auth_function_execution_policy"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action: [
          "apigateway:POST",
          "ssm:GetParameter",
          "cognito-idp:AdminUpdateUserAttributes",
          "cognito-idp:InitiateAuth",
          "cognito-idp:SignUp"
        ],
        Effect: "Allow",
        Resource: "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "auth_lambda_policy_attachment" {
  role       = aws_iam_role.auth_lambda_execution_role.name
  policy_arn = aws_iam_policy.auth_lambda_execution_policy.arn
}

resource "aws_iam_role_policy_attachment" "auth_lambda_logging_policy_attachment" {
  role       = aws_iam_role.auth_lambda_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role" "bedrock_lambda_execution_role" {
  name = "bedrock_function_execution_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action: "sts:AssumeRole",
        Effect: "Allow",
        Principal: { Service: "lambda.amazonaws.com" }
      }
    ]
  })
}

resource "aws_iam_policy" "bedrock_lambda_execution_policy" {
  name = "bedrock_function_execution_policy"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action: [
          "bedrock:ListFoundationModels",
          "bedrock:InvokeModel",
          "cognito-idp:InitiateAuth",
          "cognito-idp:SignUp"
        ],
        Effect: "Allow",
        Resource: "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "bedrock_lambda_policy_attachment" {
  role       = aws_iam_role.bedrock_lambda_execution_role.name
  policy_arn = aws_iam_policy.bedrock_lambda_execution_policy.arn
}

resource "aws_iam_role_policy_attachment" "bedrock_lambda_logging_policy_attachment" {
  role       = aws_iam_role.bedrock_lambda_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "auth_lambda_function" {
  function_name = "auth_function"
  runtime       = var.lambda_runtime
  handler       = var.auth_handler
  timeout       = var.timeout

  environment {
    variables = {
      CONSTRUCT_ID = var.contructID
    }
  }

  role             = aws_iam_role.auth_lambda_execution_role.arn
  filename         = "${path.module}/src/auth/auth.zip"
  source_code_hash = filebase64sha256("${path.module}/src/auth/auth.zip")
}

resource "aws_lambda_function" "bedrock_lambda_function" {
  function_name = "bedrock_function"
  runtime       = var.lambda_runtime
  handler       = "bedrock.handler"
  timeout       = var.timeout

  role             = aws_iam_role.bedrock_lambda_execution_role.arn
  filename         = "${path.module}/${var.bedrock_path}/bedrock.zip"
  source_code_hash = filebase64sha256("${path.module}/src/bedrock/bedrock.zip")
}
