
# modules/state_machine/main.tf
resource "aws_iam_role" "state_machine" {
  name = "state-machine-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "states.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy" "state_machine" {
  name = "state-machine-policy"
  role = aws_iam_role.state_machine.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid      = "invokeHTTP"
        Effect   = "Allow"
        Action   = "states:InvokeHTTPEndpoint"
        Resource = "*"
        Condition = {
          StringLike = {
            "states:HTTPEndpoint" = "https://${var.api_domain_name}/*"
          }
        }
      },
      {
        Sid    = "retrieveEBConnection"
        Effect = "Allow"
        Action = "events:RetrieveConnectionCredentials"
        Resource = var.connection_arn
      },
      {
        Sid    = "retrieveEBSecretForConnection"
        Effect = "Allow"
        Action = [
          "secretsmanager:GetSecretValue",
          "secretsmanager:DescribeSecret"
        ]
        Resource = var.connection_secret_arn
      }
    ]
  })
}

resource "aws_cloudwatch_log_group" "state_machine" {
  name              = "/aws/stepfunctions/state-machine"
  retention_in_days = var.log_retention_days
}

resource "aws_iam_role_policy" "state_machine_logging" {
  name = "state-machine-logging-policy"
  role = aws_iam_role.state_machine.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogDelivery",
          "logs:GetLogDelivery",
          "logs:UpdateLogDelivery",
          "logs:DeleteLogDelivery",
          "logs:ListLogDeliveries",
          "logs:PutLogEvents",
          "logs:PutResourcePolicy",
          "logs:DescribeResourcePolicies",
          "logs:DescribeLogGroups"
        ]
        Resource = "*"
      }
    ]
  })
}

resource "aws_sfn_state_machine" "state_machine" {
  name     = "state-machine-call-onprem"
  role_arn = aws_iam_role.state_machine.arn

  definition = templatefile("${path.module}/state-machine.asl.json", {
    EventBridgeConnectionArn = var.connection_arn
    GetHelloEndpoint         = "https://${var.api_domain_name}/hello"
  })

  logging_configuration {
    log_destination        = "${aws_cloudwatch_log_group.state_machine.arn}:*"
    include_execution_data = true
    level                 = "ALL"
  }

  tracing_configuration {
    enabled = true
  }

  type = "EXPRESS"
}
