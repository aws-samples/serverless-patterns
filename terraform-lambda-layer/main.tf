provider "aws" {
  region = "eu-west-1"
}

####################################################
# Lambda Function (building locally)
####################################################

module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"
  version = "~> 4.0"

  function_name          = "${random_pet.this.id}-lambda1"
  description            = "My awesome lambda function"
  handler       = "index.lambda_handler"
  runtime       = "python3.8"
  publish       = true

  source_path = "${path.module}/../terraform-fixtures/python"

  layers = [
    module.lambda_layer_local.lambda_layer_arn,
  ]

  tags = {
    Pattern = "terraform-lambda-layer"
    Module = "lambda_function"
  }
}

#################################
# Lambda Layer (prepackaged and stored locally)
#################################

module "lambda_layer_local" {
  source = "terraform-aws-modules/lambda/aws"
  version = "~> 4.0"

  create_layer = true

  layer_name               = "${random_pet.this.id}-layer-local"
  description              = "My amazing lambda layer (deployed from local)"
  compatible_runtimes      = ["python3.8"]

  create_package         = false
  local_existing_package = "${path.module}/../terraform-fixtures/packages/python_src.zip"

  tags = {
    Pattern = "terraform-lambda-layer"
    Module = "lambda_layer_local"
  }
}

##################
# Extra resources
##################

resource "random_pet" "this" {
  length = 2
}
