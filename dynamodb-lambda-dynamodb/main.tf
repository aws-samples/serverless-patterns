provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

resource "aws_dynamodb_table" "source_table" {
  name             = "UserDB"
  hash_key         = "email"
  read_capacity    = 5
  write_capacity   = 5
  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"

  attribute {
    name = "email"
    type = "S"  # S for string, you can change it to other types if needed
  }
}

resource "aws_dynamodb_table" "target_table" {
  provider         = aws.west
  name             = "UserDB2"
  hash_key         = "email"
  read_capacity    = 5
  write_capacity   = 5
  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"

  attribute {
    name = "email"
    type = "S"  # S for string, you can change it to other types if needed
  }
}

resource "aws_lambda_function" "replicator" {
  function_name    = "data_replicator"
  runtime          = "java17"
  handler          = "com.sahh.multiregiondatareplication.DataReplicator::handleRequest"
  filename         = "C:\\multi-region-data-replication\\target\\multi-region-data-replication-0.0.1-SNAPSHOT.jar"
  source_code_hash = filebase64sha256("C:\\multi-region-data-replication\\target\\multi-region-data-replication-0.0.1-SNAPSHOT.jar")
  role             = aws_iam_role.lambda.arn
  timeout          = 60
  memory_size      = 256

  environment {
    variables = {
      SOURCE_REGION      = "us-east-1"
      DEST_REGION        = "us-west-2"
      TABLE_NAME         = aws_dynamodb_table.source_table.name
      TARGET_TABLE_NAME  = aws_dynamodb_table.target_table.name
    }
  }
}

resource "aws_iam_policy" "lambda_basic_execution" {
  name        = "lambda_basic_execution"
  description = "Policy for basic Lambda execution"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "dynamodb:DescribeStream",
        "dynamodb:GetRecords",
        "dynamodb:GetShardIterator",
        "dynamodb:ListStreams",
        "dynamodb:PutItem",
        "dynamodb:DeleteItem"
      ],
      "Resource": "*"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_basic_execution_attachment" {
  policy_arn = aws_iam_policy.lambda_basic_execution.arn
  role       = aws_iam_role.lambda.name
}

resource "aws_iam_role" "lambda" {
  name = "lambda-data-replicator-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_lambda_event_source_mapping" "event_mapping" {
  event_source_arn  = aws_dynamodb_table.source_table.stream_arn
  function_name     = aws_lambda_function.replicator.function_name
  starting_position = "LATEST"
}
