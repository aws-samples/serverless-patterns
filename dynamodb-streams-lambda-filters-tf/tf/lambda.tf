resource "aws_iam_role_policy" "dynamodb_lambda_policy" {
  name   = "lambda-dynamodb-policy"
  role   = aws_iam_role.iam_for_lambda.id
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
        "Sid": "AllowLambdaFunctionToCreateLogs",
        "Action": [ 
            "logs:*" 
        ],
        "Effect": "Allow",
        "Resource": [ 
            "arn:aws:logs:*:*:*" 
        ]
    },
    {
        "Sid": "AllowLambdaFunctionInvocation",
        "Effect": "Allow",
        "Action": [
            "lambda:InvokeFunction"
        ],
        "Resource": [
            "${aws_dynamodb_table.dynamodb_request_table.arn}/stream/*"
        ]
    },
    {
        "Sid": "APIAccessForDynamoDBStreams",
        "Effect": "Allow",
        "Action": [
            "dynamodb:GetRecords",
            "dynamodb:GetShardIterator",
            "dynamodb:DescribeStream",
            "dynamodb:ListStreams"
        ],
        "Resource": "${aws_dynamodb_table.dynamodb_request_table.arn}/stream/*"
    }
  ]
}
EOF
}

resource "aws_iam_role" "iam_for_lambda" {
  name = "iam_for_lambda"

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
}

data "archive_file" "lambda_zip_file" {
  type        = "zip"
  source_file = "${path.module}/../src/handler.py"
  output_path = "${path.module}/../lambda.zip"
}

resource "aws_lambda_function" "lambda_dynamodb_stream_handler_bachelors" {
  function_name    = "process-bachelors-request"
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = data.archive_file.lambda_zip_file.output_base64sha256
  handler          = "handler.bachelors_handler"
  role             = aws_iam_role.iam_for_lambda.arn
  runtime          = "python3.10"
}

resource "aws_lambda_function" "lambda_dynamodb_stream_handler_masters" {
  function_name    = "process-masters-requests"
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = data.archive_file.lambda_zip_file.output_base64sha256
  handler          = "handler.masters_handler"
  role             = aws_iam_role.iam_for_lambda.arn
  runtime          = "python3.10"
}

resource "aws_lambda_function" "lambda_dynamodb_stream_handler_modify" {
  function_name    = "process-modify-request"
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = data.archive_file.lambda_zip_file.output_base64sha256
  handler          = "handler.modify_handler"
  role             = aws_iam_role.iam_for_lambda.arn
  runtime          = "python3.10"
}

resource "aws_lambda_function" "lambda_dynamodb_stream_handler_delete" {
  function_name    = "process-delete-request"
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = data.archive_file.lambda_zip_file.output_base64sha256
  handler          = "handler.remove_handler"
  role             = aws_iam_role.iam_for_lambda.arn
  runtime          = "python3.10"
}

resource "aws_lambda_event_source_mapping" "lambda_bachelors_dynamodb" {
  event_source_arn  = aws_dynamodb_table.dynamodb_request_table.stream_arn
  function_name     = aws_lambda_function.lambda_dynamodb_stream_handler_bachelors.arn
  starting_position = "LATEST"

  filter_criteria {
    filter {
      pattern = jsonencode(
        {
          "eventName" : ["INSERT"],
          "dynamodb": {
            "NewImage": {
              "degree":{
                "S": ["Bachelors"]
              }
            }
          }
        }
      )
    }
  }
}


resource "aws_lambda_event_source_mapping" "lambda_masters_dynamodb" {
  event_source_arn  = aws_dynamodb_table.dynamodb_request_table.stream_arn
  function_name     = aws_lambda_function.lambda_dynamodb_stream_handler_masters.arn
  starting_position = "LATEST"

  filter_criteria {
    filter {
      pattern = jsonencode(
        {
          "eventName" : ["INSERT"],
          "dynamodb": {
            "NewImage": {
              "degree":{
                "S": ["Masters"]
              }
            }
          }
        }
      )
    }
  }
}


resource "aws_lambda_event_source_mapping" "lambda_modify_dynamodb" {
  event_source_arn  = aws_dynamodb_table.dynamodb_request_table.stream_arn
  function_name     = aws_lambda_function.lambda_dynamodb_stream_handler_modify.arn
  starting_position = "LATEST"

  filter_criteria {
    filter {
      pattern = jsonencode(
        {
          "eventName" : ["MODIFY"]
        }
      )
    }
  }
}

resource "aws_lambda_event_source_mapping" "lambda_delete_dynamodb" {
  event_source_arn  = aws_dynamodb_table.dynamodb_request_table.stream_arn
  function_name     = aws_lambda_function.lambda_dynamodb_stream_handler_delete.arn
  starting_position = "LATEST"

  filter_criteria {
    filter {
      pattern = jsonencode(
        {
          "eventName" : ["REMOVE"]
        }
      )
    }
  }
}

