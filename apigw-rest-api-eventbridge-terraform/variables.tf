# Input variable definitions

variable "aws_region" {
  description = "AWS region for all resources."

  type    = string
  default = "us-east-1"
}

variable "eventbus_name" {
  description = "the name of the custom event bus"

  type    = string
  default = "MyIntegrationCustomBus"
}

variable "apigw_name" {
  description = "the name of the api gateway"
  type = string
  default = "rest-api-eb"
}

variable "catchall_log_retention" {
  description = "cw log retention in days"
  type = number
  default = 7
}