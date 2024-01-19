# This code declars common variables to be used in terraform resource defintions.  
# © 2023 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.  
# This AWS Content is provided subject to the terms of the AWS Customer Agreement available at  
# http://aws.amazon.com/agreement or other written agreement between Customer and either
# Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

########################### Common ###########################
variable "region" {
  type    = string
  default = "us-east-1"
}

variable "tag_environment" {
  type    = string
  default = "prod"
}

variable "tag_project" {
  type    = string
  default = "openapi-demo"
}
##############################################################
########################## DynamoDB ##########################
variable "customer_ddb_table_name" {
  type    = string
  default = "customer-db"
}
##############################################################
####################### Lambda Common ########################
variable "lambda_runtime" {
  type    = string
  default = "nodejs18.x"
}

variable "lambda_handler" {
  type    = string
  default = "index.handler"
}

variable "compatible_runtimes" {
  description = "A list of Runtimes this layer is compatible with. Up to 5 runtimes can be specified."
  type        = list(string)
  default     = ["nodejs18.x"]
}

variable "default_log_level" {
  description = "Default Log level setting for lambdas"
  type        = string
  default     = "INFO"
}

variable "default_api_timeout" {
  description = "Default timeout in seconds for lambda API's"
  type        = number
  default     = 10
}
##############################################################
######################## AWS SDK Layer #######################
variable "aws_sdk_layer_src" {
  type    = string
  default = "../dist/layer/aws-sdk/"
}

variable "aws_sdk_layer_name" {
  type    = string
  default = "aws-sdk"
}

variable "aws_sdk_layer_desc" {
  type    = string
  default = "This layer provides necessary AWS SDK libraries for lambdas"
}
##############################################################
################### External lib layer ##################
variable "ext_libs_layer_src" {
  type    = string
  default = "../dist/layer/ext-libs/"
}

variable "ext_libs_layer_name" {
  type    = string
  default = "ext-libs"
}

variable "ext_libs_layer_desc" {
  type    = string
  default = "This layer provides requied external libs across all lambdas"
}
##############################################################
############### AWS Lambda Powertools with middy #############
variable "lambda_powertools_layer_src" {
  type    = string
  default = "../dist/layer/lambda-powertools/"
}

variable "lambda_powertools_layer_name" {
  type    = string
  default = "aws-lambda-powertools"
}

variable "lambda_powertools_layer_desc" {
  type    = string
  default = "This layer offers structured logging, tracing and metric generation in lambdas"
}
##############################################################
######################## Common Code Layer #######################
variable "common_code_layer_src" {
  type    = string
  default = "../dist/layers/"
}

variable "common_code_layer_name" {
  type    = string
  default = "common-utils"
}

variable "common_code_layer_desc" {
  type    = string
  default = "Shared code across lambdas"
}
##############################################################
####################### API Demo Lambda ######################
variable "openapi_demo_lambda_src" {
  type    = string
  default = "../dist/lambdas/openapi-demo/"
}

variable "openapi_demo_lambda_name" {
  type    = string
  default = "openapi-demo"
}

variable "openapi_demo_lambda_desc" {
  type    = string
  default = "OpenAPI spec demo lambda"
}

variable "openapi_demo_service_name" {
  type    = string
  default = "OpenAPI Demo Service"
}
##############################################################
#################### OpenAPI Spec Rest API ###################
variable "apigw_name" {
  type    = string
  default = "open-api-demo"
}

variable "apigw_desc" {
  type    = string
  default = "API gateway with open api spec"
}

variable "apigw_stage_name" {
  type    = string
  default = "prod"
}

variable "origin_domain" {
  type    = string
  default = ""
}
##############################################################
