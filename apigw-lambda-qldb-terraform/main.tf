terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.22"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

data "aws_iam_policy" "lambda_basic_execution_role_policy" {
  name = "AWSLambdaBasicExecutionRole"
}

resource "aws_qldb_ledger" "ledger" {
  name                = "qldb-serverless-pattern"
  permissions_mode    = "STANDARD"
  deletion_protection = false
  tags                = {
    name = "qldb-serverless-pattern"
  }
}

# Create Person

resource "aws_lambda_function" "lambda_function_create_person" {
  function_name    = "CreatePerson"
  filename         = data.archive_file.lambda_zip_file_create_person.output_path
  source_code_hash = data.archive_file.lambda_zip_file_create_person.output_base64sha256
  handler          = "create-person.handler"
  role             = aws_iam_role.lambda_iam_role_create_person.arn
  runtime          = "nodejs14.x"
  environment {
    variables = {
      LEDGER_NAME = aws_qldb_ledger.ledger.id
      AWS_NODEJS_CONNECTION_REUSE_ENABLED = 1
    }
  }
  
}

data "archive_file" "lambda_zip_file_create_person" {
  type        = "zip"
  source_file = "${path.module}/src/create-person.js"
  output_path = "${path.module}/lambda-create-person.zip"
}

resource "aws_iam_role" "lambda_iam_role_create_person" {
  name_prefix = "LambdaCreatePersonRole-"
  managed_policy_arns = [
    data.aws_iam_policy.lambda_basic_execution_role_policy.arn,
    aws_iam_policy.lambda_policy_create_person.arn
  ]

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

data "aws_iam_policy_document" "lambda_policy_document_create_person" {
  statement {
  
    effect = "Allow"
  
    actions = [
      "qldb:SendCommand"
    ]

    resources = [
      aws_qldb_ledger.ledger.arn
    ]
  }
  
  statement {
    effect = "Allow"
    
    actions = [
      "qldb:PartiQLInsert",
      "qldb:PartiQLUpdate",
      "qldb:PartiQLSelect"
    ]
    
    resources = [
      "${aws_qldb_ledger.ledger.arn}/*"
    ]
  }
}

resource "aws_iam_policy" "lambda_policy_create_person" {
  name_prefix   = "lambda_policy_create_person-"
  path          = "/"
  policy        = data.aws_iam_policy_document.lambda_policy_document_create_person.json
}

# Get Person

resource "aws_lambda_function" "lambda_function_get_person" {
  function_name    = "GetPerson"
  filename         = data.archive_file.lambda_zip_file_get_person.output_path
  source_code_hash = data.archive_file.lambda_zip_file_get_person.output_base64sha256
  handler          = "app.handler"
  role             = aws_iam_role.lambda_iam_role_get_person.arn
  runtime          = "nodejs14.x"
  environment {
    variables = {
      LEDGER_NAME = aws_qldb_ledger.ledger.id
      AWS_NODEJS_CONNECTION_REUSE_ENABLED = 1
    }
  }
}

data "archive_file" "lambda_zip_file_get_person" {
  type        = "zip"
  source_file = "${path.module}/src/get-person.js"
  output_path = "${path.module}/lambda-get-person.zip"
}

resource "aws_iam_role" "lambda_iam_role_get_person" {
  name_prefix = "LambdaGetPersonRole-"
  managed_policy_arns = [
    data.aws_iam_policy.lambda_basic_execution_role_policy.arn,
    aws_iam_policy.lambda_policy_get_person.arn
  ]

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

data "aws_iam_policy_document" "lambda_policy_document_get_person" {
  statement {
  
    effect = "Allow"
  
    actions = [
      "qldb:SendCommand"
    ]

    resources = [
      aws_qldb_ledger.ledger.arn
    ]
  }
  
  statement {
    effect = "Allow"
    
    actions = [
      "qldb:PartiQLSelect"
    ]
    
    resources = [
      "${aws_qldb_ledger.ledger.arn}/*"
    ]
  }
}

resource "aws_iam_policy" "lambda_policy_get_person" {
  name_prefix   = "lambda_policy_get_person-"
  path          = "/"
  policy        = data.aws_iam_policy_document.lambda_policy_document_get_person.json
}

# Get Person History

resource "aws_lambda_function" "lambda_function_get_person_history" {
  function_name    = "GetPersonHistory"
  filename         = data.archive_file.lambda_zip_file_get_person_history.output_path
  source_code_hash = data.archive_file.lambda_zip_file_get_person_history.output_base64sha256
  handler          = "app.handler"
  role             = aws_iam_role.lambda_iam_role_get_person_history.arn
  runtime          = "nodejs14.x"
  environment {
    variables = {
      LEDGER_NAME = aws_qldb_ledger.ledger.id
      AWS_NODEJS_CONNECTION_REUSE_ENABLED = 1
    }
  }
}

data "archive_file" "lambda_zip_file_get_person_history" {
  type        = "zip"
  source_file = "${path.module}/src/get-person-history.js"
  output_path = "${path.module}/lambda-get-person-history.zip"
}

resource "aws_iam_role" "lambda_iam_role_get_person_history" {
  name_prefix = "LambdaGetPersonHistoryRole-"
  managed_policy_arns = [
    data.aws_iam_policy.lambda_basic_execution_role_policy.arn,
    aws_iam_policy.lambda_policy_get_person_history.arn
  ]

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

data "aws_iam_policy_document" "lambda_policy_document_get_person_history" {
  statement {
  
    effect = "Allow"
  
    actions = [
      "qldb:SendCommand"
    ]

    resources = [
      aws_qldb_ledger.ledger.arn
    ]
  }
  
  statement {
    effect = "Allow"
    
    actions = [
      "qldb:PartiQLHistoryFunction"
    ]
    
    resources = [
      "${aws_qldb_ledger.ledger.arn}/*"
    ]
  }
}

resource "aws_iam_policy" "lambda_policy_get_person_history" {
  name_prefix   = "lambda_policy_get_person_history-"
  path          = "/"
  policy        = data.aws_iam_policy_document.lambda_policy_document_get_person_history.json
}

# Update Person

resource "aws_lambda_function" "lambda_function_update_person" {
  function_name    = "UpdatePerson"
  filename         = data.archive_file.lambda_zip_file_update_person.output_path
  source_code_hash = data.archive_file.lambda_zip_file_update_person.output_base64sha256
  handler          = "app.handler"
  role             = aws_iam_role.lambda_iam_role_update_person.arn
  runtime          = "nodejs14.x"
  environment {
    variables = {
      LEDGER_NAME = aws_qldb_ledger.ledger.id
      AWS_NODEJS_CONNECTION_REUSE_ENABLED = 1
    }
  }
}

data "archive_file" "lambda_zip_file_update_person" {
  type        = "zip"
  source_file = "${path.module}/src/update-person.js"
  output_path = "${path.module}/lambda-update-person.zip"
}

resource "aws_iam_role" "lambda_iam_role_update_person" {
  name_prefix = "LambdaUpdatePersonRole-"
  managed_policy_arns = [
    data.aws_iam_policy.lambda_basic_execution_role_policy.arn,
    aws_iam_policy.lambda_policy_update_person.arn
  ]

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

data "aws_iam_policy_document" "lambda_policy_document_update_person" {
  statement {
  
    effect = "Allow"
  
    actions = [
      "qldb:SendCommand"
    ]

    resources = [
      aws_qldb_ledger.ledger.arn
    ]
  }
  
  statement {
    effect = "Allow"
    
    actions = [
      "qldb:PartiQLSelect",
      "qldb:PartiQLUpdate"
    ]
    
    resources = [
      "${aws_qldb_ledger.ledger.arn}/*"
    ]
  }
}

resource "aws_iam_policy" "lambda_policy_update_person" {
  name_prefix   = "lambda_policy_update_person-"
  path          = "/"
  policy        = data.aws_iam_policy_document.lambda_policy_document_update_person.json
}

# Delete Person

resource "aws_lambda_function" "lambda_function_delete_person" {
  function_name    = "DeletePerson"
  filename         = data.archive_file.lambda_zip_file_delete_person.output_path
  source_code_hash = data.archive_file.lambda_zip_file_delete_person.output_base64sha256
  handler          = "app.handler"
  role             = aws_iam_role.lambda_iam_role_delete_person.arn
  runtime          = "nodejs14.x"
  environment {
    variables = {
      LEDGER_NAME = aws_qldb_ledger.ledger.id
      AWS_NODEJS_CONNECTION_REUSE_ENABLED = 1
    }
  }
}

data "archive_file" "lambda_zip_file_delete_person" {
  type        = "zip"
  source_file = "${path.module}/src/delete-person.js"
  output_path = "${path.module}/lambda-delete-person.zip"
}

resource "aws_iam_role" "lambda_iam_role_delete_person" {
  name_prefix = "LambdaDeletePersonRole-"
  managed_policy_arns = [
    data.aws_iam_policy.lambda_basic_execution_role_policy.arn,
    aws_iam_policy.lambda_policy_delete_person.arn
  ]

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

data "aws_iam_policy_document" "lambda_policy_document_delete_person" {
  statement {
  
    effect = "Allow"
  
    actions = [
      "qldb:SendCommand"
    ]

    resources = [
      aws_qldb_ledger.ledger.arn
    ]
  }
  
  statement {
    effect = "Allow"
    
    actions = [
      "qldb:PartiQLSelect"
    ]
    
    resources = [
      "${aws_qldb_ledger.ledger.arn}/*"
    ]
  }
}

resource "aws_iam_policy" "lambda_policy_delete_person" {
  name_prefix   = "lambda_policy_delete_person-"
  path          = "/"
  policy        = data.aws_iam_policy_document.lambda_policy_document_delete_person.json
}

# API Gateway

resource "aws_api_gateway_rest_api" "api" {
  name  = "qldb-api"
  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

resource "aws_api_gateway_resource" "person" {
  parent_id   = aws_api_gateway_rest_api.api.root_resource_id
  path_part   = "person"
  rest_api_id = aws_api_gateway_rest_api.api.id
}

resource "aws_api_gateway_resource" "personid" {
  parent_id   = aws_api_gateway_resource.person.id
  path_part   = "{personid}"
  rest_api_id = aws_api_gateway_rest_api.api.id
}

resource "aws_api_gateway_resource" "person_history" {
  parent_id   = aws_api_gateway_resource.person.id
  path_part   = "history"
  rest_api_id = aws_api_gateway_rest_api.api.id
}

resource "aws_api_gateway_resource" "person_history_personid" {
  parent_id   = aws_api_gateway_resource.person_history.id
  path_part   = "{personid}"
  rest_api_id = aws_api_gateway_rest_api.api.id
}

resource "aws_api_gateway_method" "person_post" {
  authorization = "NONE"
  http_method   = "POST"
  resource_id   = aws_api_gateway_resource.person.id
  rest_api_id   = aws_api_gateway_rest_api.api.id
}

resource "aws_api_gateway_integration" "person_post" {
  http_method = aws_api_gateway_method.person_post.http_method
  resource_id = aws_api_gateway_resource.person.id
  rest_api_id = aws_api_gateway_rest_api.api.id
  type        = "AWS_PROXY"
  uri         = aws_lambda_function.lambda_function_create_person.invoke_arn
  integration_http_method = "POST"
}

resource "aws_lambda_permission" "apigw_lambda_function_create_person" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_function_create_person.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.api.execution_arn}/*/${aws_api_gateway_method.person_post.http_method}${aws_api_gateway_resource.person.path}"
}

resource "aws_api_gateway_method" "personid_get" {
  authorization = "NONE"
  http_method   = "GET"
  resource_id   = aws_api_gateway_resource.personid.id
  rest_api_id   = aws_api_gateway_rest_api.api.id
}

resource "aws_api_gateway_method" "person_history_personid_get" {
  authorization = "NONE"
  http_method   = "GET"
  resource_id   = aws_api_gateway_resource.person_history_personid.id
  rest_api_id   = aws_api_gateway_rest_api.api.id
}

resource "aws_api_gateway_method" "personid_post" {
  authorization = "NONE"
  http_method   = "POST"
  resource_id   = aws_api_gateway_resource.personid.id
  rest_api_id   = aws_api_gateway_rest_api.api.id
}

resource "aws_api_gateway_method" "personid_delete" {
  authorization = "NONE"
  http_method   = "DELETE"
  resource_id   = aws_api_gateway_resource.personid.id
  rest_api_id   = aws_api_gateway_rest_api.api.id
}

output "PersonLedger" {
  value       = aws_qldb_ledger.ledger.id
  description = "QLDB Ledger for the sample application"
}
