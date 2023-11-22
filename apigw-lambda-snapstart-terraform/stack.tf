provider "aws" {}
data "aws_region" "current" {}
data "aws_caller_identity" "current" {}
variable "SourceCodePath" {
  type = string
  default = "./UnicornStockLambda/target/UnicornStockBroker-1.0-aws.jar"
}

resource "aws_dynamodb_table" "transactions_table" {

  name         = "TransactionsTable"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "transactionId"

  attribute {
    name = "transactionId"
    type = "S"
  }
}

resource "aws_api_gateway_rest_api" "unicornstockbroker_apigw" {
  name        = "unicornstockbroker_apigw"
  description = "Unicorn Stock Broker API Gateway"
  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

resource "aws_api_gateway_resource" "transactions" {
  rest_api_id = aws_api_gateway_rest_api.unicornstockbroker_apigw.id
  parent_id   = aws_api_gateway_rest_api.unicornstockbroker_apigw.root_resource_id
  path_part   = "transactions"
}

resource "aws_api_gateway_method" "createtransactions" {
  rest_api_id   = aws_api_gateway_rest_api.unicornstockbroker_apigw.id
  resource_id   = aws_api_gateway_resource.transactions.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_s3_bucket" "validationfiles-bucket" {
  bucket = "validationfiless3bucket"
}
resource "aws_s3_bucket_server_side_encryption_configuration" "bucketsseconfig"{
  bucket = aws_s3_bucket.validationfiles-bucket.bucket
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}


resource "aws_iam_role" "UnicornStockBrokerFunctionRole" {
  name               = "UnicornStockBrokerFunctionRole"
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

data "aws_iam_policy_document" "unicornstockbrokerfunctionpolicy" {
  statement {
    effect  = "Allow"
    actions = [
      "dynamodb:GetItem",
      "dynamodb:DeleteItem",
      "dynamodb:PutItem",
      "dynamodb:Scan",
      "dynamodb:Query",
      "dynamodb:UpdateItem",
      "dynamodb:BatchWriteItem",
      "dynamodb:BatchGetItem",
      "dynamodb:DescribeTable",
      "dynamodb:ConditionCheckItem"
    ]
    resources = [
      "arn:aws:dynamodb:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:table/${aws_dynamodb_table.transactions_table.name}",
      "arn:aws:dynamodb:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:table/${aws_dynamodb_table.transactions_table.name}/index/*",
    ]
  }
  statement {
    effect  = "Allow"
    actions = [
      "s3:GetObject",
      "s3:ListBucket",
      "s3:GetBucketLocation",
      "s3:GetObjectVersion",
      "s3:GetLifecycleConfiguration"
    ]
    resources = [
      "arn:aws:s3:::${aws_s3_bucket.validationfiles-bucket.id}",
      "arn:aws:s3:::${aws_s3_bucket.validationfiles-bucket.id}/*"
    ]
  }
}
resource "aws_iam_policy" "UnicornStockBrokerFunctionPolicy" {
  name        = "UnicornStockBrokerFunctionPolicy"
  path        = "/"
  description = "IAM policy for Stock Broker lambda functions"
  policy      = data.aws_iam_policy_document.unicornstockbrokerfunctionpolicy.json
}

resource "aws_iam_role_policy_attachment" "UnicornStockBrokerFunctionRolePolicy" {
  role       = aws_iam_role.UnicornStockBrokerFunctionRole.name
  policy_arn = aws_iam_policy.UnicornStockBrokerFunctionPolicy.arn
}
resource "aws_iam_role_policy_attachment" "UnicornStockBrokerFunctionRolePolicy2" {
  role       = aws_iam_role.UnicornStockBrokerFunctionRole.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "UnicornStockBrokerFunction" {

  function_name = "UnicornStockBrokerFunction"

  filename = var.SourceCodePath

  handler = "org.springframework.cloud.function.adapter.aws.FunctionInvoker::handleRequest"
  runtime = "java11"

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.transactions_table.name
      BUCKET_NAME = aws_s3_bucket.validationfiles-bucket.id
      JAVA_TOOL_OPTIONS = "-XX:+TieredCompilation -XX:TieredStopAtLevel=1"
    }
  }

  source_code_hash = filebase64sha256(var.SourceCodePath)

  role = aws_iam_role.UnicornStockBrokerFunctionRole.arn

  timeout     = "200"
  memory_size = "2048"
  snap_start {
    apply_on ="PublishedVersions"
  }
  publish = true
}
resource "aws_lambda_alias" "UnicornStockBrokerFunction_SnapStartAlias" {
  name             = "SnapStart"
  description      = "Alias for SnapStart"
  function_name    = aws_lambda_function.UnicornStockBrokerFunction.function_name
  function_version = aws_lambda_function.UnicornStockBrokerFunction.version
}

resource "aws_api_gateway_integration" "createproduct-lambda" {

  rest_api_id = aws_api_gateway_rest_api.unicornstockbroker_apigw.id
  resource_id = aws_api_gateway_method.createtransactions.resource_id
  http_method = aws_api_gateway_method.createtransactions.http_method

  integration_http_method = "POST"
  type                    = "AWS_PROXY"

  uri = aws_lambda_alias.UnicornStockBrokerFunction_SnapStartAlias.invoke_arn
}

resource "aws_lambda_permission" "apigw-CreateProductHandler" {

  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.UnicornStockBrokerFunction.function_name
  qualifier = aws_lambda_alias.UnicornStockBrokerFunction_SnapStartAlias.name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.unicornstockbroker_apigw.execution_arn}/*/${aws_api_gateway_method.createtransactions.http_method}${aws_api_gateway_resource.transactions.path}"
}

resource "aws_api_gateway_deployment" "productapistageprod" {

  depends_on = [
    aws_api_gateway_integration.createproduct-lambda
  ]

  rest_api_id = aws_api_gateway_rest_api.unicornstockbroker_apigw.id
  stage_name  = "prod"
}

output "apigw-url" {
  value = aws_api_gateway_deployment.productapistageprod.invoke_url
}
