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
  handler       = "app.lambda_handler"
  runtime       = "python3.8"
  publish       = true

  source_path = "${path.module}/src/app.py"

  layers = [
    module.lambda_layer.lambda_layer_arn,
  ]

  tags = {
    Pattern = "terraform-lambda-layer"
    Module  = "lambda_function"
  }
}

#############################################
# Lambda Layer (install Python dependencies)
#############################################

module "lambda_layer" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "~> 4.0"

  create_layer = true

  layer_name          = "${random_pet.this.id}-layer"
  description         = "My amazing lambda layer (pip install)"
  compatible_runtimes = ["python3.8"]

  runtime = "python3.8" # Runtime is required for "pip install" to work

  source_path = [
    {
      path             = "${path.module}/dependencies/mysql-connector-python"
      pip_requirements = true     # Will run "pip install" with default "requirements.txt" from the path
      prefix_in_zip    = "python" # required to get the path correct
    }
  ]

  tags = {
    Pattern = "terraform-lambda-layer"
    Module  = "lambda_layer"
  }
}

##################
# Extra resources
##################

resource "random_pet" "this" {
  length = 2
}
