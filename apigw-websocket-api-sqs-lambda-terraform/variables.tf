# Input variable definitions

variable "aws_region" {
  description = "AWS region for all resources."

  type    = string
  default = "us-east-1"
}

variable "s3_bucket_prefix" {
  description = "the name of the prefix for s3 bucket"
  type    = string
  default = "apigw-websocket"
}

variable "lambda_name" {
  description = "name of the lambda function"
  type = string
  default = "apigw-websocket-response"
}

variable "sqs_name" {
  description = "the name of the sqs queue"
  type    = string
  default = "tf-APIGWWebsocketQueue.fifo"
}

variable "apigwy_name" {
  description = "name of the apigateway"
  type = string
  default = "APIGWWebsocketSQSLambda"
}

variable "lambda_log_retention" {
  description = "lambda log retention in days"
  type = number
  default = 7
}