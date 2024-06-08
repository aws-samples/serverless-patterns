provider "aws" {
  region = "us-east-1" # Replace with your desired AWS region
}
data "aws_secretsmanager_secret" "mq_access" {
  name = "MQaccess"
}
data "aws_secretsmanager_secret_version" "mq_access_version" {
  secret_id = data.aws_secretsmanager_secret.mq_access.id
}
resource "aws_mq_broker" "mq_broker" {
  broker_name           = "myQueue"
  engine_type           = "RabbitMQ"
  engine_version        = "3.11.28"
  host_instance_type    = "mq.t3.micro"
  publicly_accessible   = true
  auto_minor_version_upgrade = false
  deployment_mode       = "SINGLE_INSTANCE"
  
  user {
    username = jsondecode(data.aws_secretsmanager_secret_version.mq_access_version.secret_string)["username"]
    password = jsondecode(data.aws_secretsmanager_secret_version.mq_access_version.secret_string)["password"]
  }
}
resource "aws_lambda_function" "mq_consumer" {
  filename      = "src/app.zip"
  function_name = "MQConsumer"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "app.lambda_handler"
  runtime       = "python3.12"
  timeout       = 3
  environment {
    variables = {
      MQ_BROKER_ARN = aws_mq_broker.mq_broker.arn
    }
  } 
  # Policies
  depends_on = [
    aws_iam_role_policy.mq_consumer_policy
  ]
}
resource "aws_iam_role" "lambda_exec" {
  name = "mq_consumer_role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}
resource "aws_iam_role_policy" "mq_consumer_policy" {
  name   = "mq_consumer_policy"
  role   = aws_iam_role.lambda_exec.id  
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Allow",
        Action   = [
          "mq:DescribeBroker",
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        Resource = aws_mq_broker.mq_broker.arn
      },
      {
        Effect   = "Allow",
        Action   = [
          "secretsmanager:GetSecretValue"
        ],
        Resource = data.aws_secretsmanager_secret.mq_access.arn
      }
    ]
  })
}
resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = aws_iam_role.lambda_exec.name
}
# Lambda Event Source Mapping
resource "aws_lambda_event_source_mapping" "mq_event_source_mapping" {
  event_source_arn = aws_mq_broker.mq_broker.arn
  function_name    = aws_lambda_function.mq_consumer.arn
  source_access_configuration {
    type = "BASIC_AUTH"
    uri  = data.aws_secretsmanager_secret.mq_access.arn
  }
  queues = ["myQueue"]
}
# Output resources
output "mq_broker_arn" {
  value = aws_mq_broker.mq_broker.arn
}
output "lambda_function_arn" {
  value = aws_lambda_function.mq_consumer.arn
}
