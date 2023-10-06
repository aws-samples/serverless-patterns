# This code deploys all the components of merch shop app.  
# © 2023 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.  
# This AWS Content is provided subject to the terms of the AWS Customer Agreement available at  
# http://aws.amazon.com/agreement or other written agreement between Customer and either
# Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

############ KMS key for OpenAPI demo project #############
resource "aws_kms_key" "root_key" {
  description             = "Encryption key for the openapi demo project"
  deletion_window_in_days = 7
  key_usage               = "ENCRYPT_DECRYPT"
  is_enabled              = true
  enable_key_rotation     = true
  # Need to include CloudWatch Logs permission here to prevent access denied error during
  # deployment.
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid" : "EnableKeyAdmin",
        "Effect" : "Allow",
        "Principal" : {
          "AWS" : "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        },
        "Action" : "kms:*",
        "Resource" : "*"
      },
      {
        "Effect" : "Allow",
        "Principal" : {
          "Service" : "logs.${var.region}.amazonaws.com"
        },
        "Action" : [
          "kms:Encrypt*",
          "kms:Decrypt*",
          "kms:ReEncrypt*",
          "kms:GenerateDataKey*",
          "kms:Describe*"
        ],
        "Resource" : "*",
        "Condition" : {
          "ArnEquals" : {
            "kms:EncryptionContext:aws:logs:arn" : "arn:aws:logs:${var.region}:${data.aws_caller_identity.current.account_id}:*"
          }
        }
      },
    ]
  })
  lifecycle {
    ignore_changes = [
      policy
    ]
  }
}
###########################################################
################ Customer DynamoDB Table ##################
module "customer_dynamodb_table" {
  source    = "github.com/terraform-aws-modules/terraform-aws-dynamodb-table?ref=03b38ee3c52250c7d606f6a21e04624a41be52f7"
  name      = var.customer_ddb_table_name
  hash_key  = "pk"
  range_key = "sk"
  attributes = [
    {
      name = "pk"
      type = "S"
    },
    {
      name = "sk"
      type = "S"
    }
  ]
  deletion_protection_enabled        = false
  point_in_time_recovery_enabled     = true
  server_side_encryption_enabled     = true
  server_side_encryption_kms_key_arn = aws_kms_key.root_key.arn
  tags = {
    Name = var.customer_ddb_table_name
  }
}
###########################################################
###################### AWS SDK Layer ######################
module "aws_sdk_lambda_layer" {
  source                  = "github.com/terraform-aws-modules/terraform-aws-lambda?ref=9acd3227087db56abac5f78d1a660b08ee159a9c"
  create_layer            = true
  layer_name              = var.aws_sdk_layer_name
  description             = var.aws_sdk_layer_desc
  compatible_runtimes     = var.compatible_runtimes
  source_path             = var.aws_sdk_layer_src
  ignore_source_code_hash = false
  tags = {
    Name = var.aws_sdk_layer_name
  }
}
###########################################################
############### AWS Lambda Powetools Layer ################
module "aws_powertools_lambda_layer" {
  source                  = "github.com/terraform-aws-modules/terraform-aws-lambda?ref=9acd3227087db56abac5f78d1a660b08ee159a9c"
  create_layer            = true
  layer_name              = var.lambda_powertools_layer_name
  description             = var.lambda_powertools_layer_desc
  compatible_runtimes     = var.compatible_runtimes
  source_path             = var.lambda_powertools_layer_src
  ignore_source_code_hash = false
  tags = {
    Name = var.lambda_powertools_layer_name
  }
}
###########################################################
################## External Libs Layer ####################
module "ext_libs_lambda_layer" {
  source                  = "github.com/terraform-aws-modules/terraform-aws-lambda?ref=9acd3227087db56abac5f78d1a660b08ee159a9c"
  create_layer            = true
  layer_name              = var.ext_libs_layer_name
  description             = var.ext_libs_layer_desc
  compatible_runtimes     = var.compatible_runtimes
  source_path             = var.ext_libs_layer_src
  ignore_source_code_hash = false
  tags = {
    Name = var.ext_libs_layer_name
  }
}
###########################################################
#################### Common Code Layer ####################
module "common_code_lambda_layer" {
  source                  = "github.com/terraform-aws-modules/terraform-aws-lambda?ref=9acd3227087db56abac5f78d1a660b08ee159a9c"
  create_layer            = true
  layer_name              = var.common_code_layer_name
  description             = var.common_code_layer_desc
  compatible_runtimes     = var.compatible_runtimes
  source_path             = var.common_code_layer_src
  ignore_source_code_hash = false
  tags = {
    Name = var.common_code_layer_name
  }
}
###########################################################
############### Open API Spec Demo Lambda #################
module "openapi_demo_lambda_function" {
  source                  = "github.com/terraform-aws-modules/terraform-aws-lambda?ref=9acd3227087db56abac5f78d1a660b08ee159a9c"
  function_name           = var.openapi_demo_lambda_name
  description             = var.openapi_demo_lambda_desc
  handler                 = var.lambda_handler
  runtime                 = var.lambda_runtime
  timeout                 = var.default_api_timeout
  source_path             = var.openapi_demo_lambda_src
  ignore_source_code_hash = false
  layers = [
    module.aws_sdk_lambda_layer.lambda_layer_arn,
    module.aws_powertools_lambda_layer.lambda_layer_arn,
    module.ext_libs_lambda_layer.lambda_layer_arn,
    module.common_code_lambda_layer.lambda_layer_arn,
  ]
  tracing_mode = "Active"
  ######################
  # Additional policies
  ######################
  attach_policy_statements = true
  policy_statements = {
    dynamodb_read_write = {
      effect    = "Allow",
      actions   = ["dynamodb:GetItem", "dynamodb:Query", "dynamodb:PutItem", "dynamodb:UpdateItem", "dynamodb:DeleteItem"],
      resources = [module.customer_dynamodb_table.dynamodb_table_arn]
    }
    kms_perm = {
      effect  = "Allow",
      actions = ["kms:Decrypt", "kms:Encrypt"],
      resources = [
        aws_kms_key.root_key.arn
      ]
    }
    xray_perm = {
      effect  = "Allow",
      actions = [
        "xray:PutTraceSegments",
        "xray:PutTelemetryRecords",
        "xray:GetSamplingRules",
        "xray:GetSamplingTargets",
        "xray:GetSamplingStatisticSummaries"
      ],
      resources = ["*"]
    }
  }
  create_current_version_allowed_triggers = false
  allowed_triggers = {
    apigw_invoke = {
      service    = "apigateway"
      source_arn = "${module.openapi_demo_rest_api.apigateway_restapi_execution_arn}/*/*"
    }
  }
  environment_variables = {
    "CUSTOMER_DDB_ARN"  = module.customer_dynamodb_table.dynamodb_table_arn
    "CUSTOMER_DDB_NAME" = var.customer_ddb_table_name
    "ACCOUNT_ID"        = data.aws_caller_identity.current.account_id
    "LOG_LEVEL"         = var.default_log_level
    "ENVIRONMENT"       = var.tag_environment
    "PROJECT"           = var.tag_project
    "SERVICE_NAME"      = var.openapi_demo_service_name
  }
  tags = {
    Name = var.openapi_demo_lambda_name
  }
}
###########################################################
################# OpenAPI Spec Rest API ###################
module "openapi_demo_rest_api" {
  source               = "./restapi"
  name                 = var.apigw_name
  desc                 = var.apigw_desc
  body                 = data.template_file.open_api_spec.rendered
  stage_name           = var.apigw_stage_name
  access_log_enabled   = true
  xray_tracing_enabled = true
  kms_key_id           = aws_kms_key.root_key.arn
}
###########################################################