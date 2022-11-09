provider "aws" {
  region = "eu-west-1"
}

#############################################
# Lambda Function (building package locally)
#############################################

module "lambda_function" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "~> 4.0"

  function_name = "${random_pet.this.id}-lambda"
  description   = "My awesome lambda function"
  handler       = "index.lambda_handler"
  runtime       = "python3.8"
  publish       = true

  source_path = "${path.module}/../terraform-fixtures/python"

  allowed_triggers = {
    dynamodb = {
      principal  = "dynamodb.amazonaws.com"
      source_arn = module.dynamodb_table.dynamodb_table_stream_arn
    }
  }

  event_source_mapping = {
    dynamodb = {
      event_source_arn  = module.dynamodb_table.dynamodb_table_stream_arn
      starting_position = "LATEST"
      filter_criteria = {
        pattern = jsonencode({
          eventName : ["INSERT"]
        })
      }
    }
  }

  attach_policies    = true
  number_of_policies = 1

  policies = [
    "arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole",
  ]

  tags = {
    Pattern = "terraform-dynamodb-streams-lambda"
    Module  = "lambda_function"
  }
}

#############################################
# DynamoDB Table with stream enabled
#############################################
module "dynamodb_table" {
  source  = "terraform-aws-modules/dynamodb-table/aws"
  version = "~> 1.0"

  name             = "${random_pet.this.id}-table-with-stream"
  hash_key         = "id"
  table_class      = "STANDARD"
  stream_view_type = "NEW_AND_OLD_IMAGES"
  stream_enabled   = true

  attributes = [
    {
      name = "id"
      type = "N"
    }
  ]

  tags = {
    Pattern = "terraform-dynamodb-streams-lambda"
    Module  = "dynamodb_table"
  }
}

##################
# Extra resources
##################

resource "random_pet" "this" {
  length = 2
}
