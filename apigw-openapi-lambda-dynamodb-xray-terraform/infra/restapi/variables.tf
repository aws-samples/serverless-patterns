# This code declars common variables to be used in rest api.  
# © 2023 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.  
# This AWS Content is provided subject to the terms of the AWS Customer Agreement available at  
# http://aws.amazon.com/agreement or other written agreement between Customer and either
# Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

######################### API Gateway ########################
variable "name" {
  type    = string
  default = ""
}

variable "desc" {
  type    = string
  default = ""
}

variable "body" {
  type    = string
  default = ""
}

variable "stage_name" {
  type    = string
  default = ""
}

variable "xray_tracing_enabled" {
  type    = bool
  default = false
}

variable "access_log_enabled" {
  type    = bool
  default = false
}

variable "log_format" {
  type    = string
  default = "$context.identity.sourceIp - - [$context.requestTime] \"$context.httpMethod $context.routeKey $context.protocol\" $context.status $context.responseLength $context.requestId $context.integrationErrorMessage"
}

variable "kms_key_id" {
  type = string
}
##############################################################