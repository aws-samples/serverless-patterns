# IAM roles and policies related to API Gateway

resource "aws_iam_role" "api_gw_invoke_role" {
  assume_role_policy = jsonencode({
    Version: "2012-10-17",
    Statement: [
      {
        Effect: "Allow",
        Principal: { Service: "apigateway.amazonaws.com" },
        Action: "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role" "api_gw_logging" {
  name = "api-gw-log-role"

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

resource "aws_iam_role_policy_attachment" "attach_cloudwatch_logging" {
  role       = aws_iam_role.api_gw_logging.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs"
}

resource "aws_iam_policy" "api_gw_invoke_policy" {
  name = "api-gw-lambda-invoke-policy"

  policy = jsonencode({
    Version: "2012-10-17",
    Statement: [
      {
        Action: "lambda:InvokeFunction",
        Effect: "Allow",
        Resource: [
          aws_lambda_function.bedrock_lambda_function.arn,
          aws_lambda_function.auth_lambda_function.arn
        ]
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "api_gw_invoke_role_attachment" {
  role       = aws_iam_role.api_gw_invoke_role.name
  policy_arn = aws_iam_policy.api_gw_invoke_policy.arn
}
