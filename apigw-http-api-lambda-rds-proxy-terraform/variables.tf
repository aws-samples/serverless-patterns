# Input variable definitions

variable "aws_region" {
  description = "AWS region for all resources."
  type    = string
  default = "us-east-1"
}

variable "lambda_name" {
  description = "name of the lambda function"
  type    = string
  default = "RdsProxyFunction"
}

variable "lambda_log_retention" {
  description = "cloudwatch log retention setting"
  type    = number
  default = 7
}

variable "bucket_name" {
  description = "name of the s3 bucket"
  type    = string
  default = "lambda-rdsproxy"
}

variable "rds_proxy_resourceid" {
  description = "name resource id of the rds proxy for lambda policy;  e.g. prx-some-hash"
  type    = string
  #default = "prx-0c....."
}

variable "vpc_id" {
  description = "vpc id for lambda fucntion"
  type    = string
  #default = "vpc-05d..."
}

variable "vpc_subnets" {
  description = "vpc subnets for lambda function"
  type    = list(string)
  #default = ["subnet-0fd2a7ab62...", "subnet-01f7f012..."]
}

variable "security_group" {
  description = "security group associated with lambda function"
  type        = string
  #default = "sg-077875c8...."
}

variable "rds_proxy_endpoint" {
  description = "the rds proxy endpoint"
  type        = string
  #default = "lambda-aurora-proxy.endpoint.proxy...."
}

variable "secret_name" {
  description = "the name you of the secret that stores the database user credentials"
  type        = string
  #default = "lambda_secret"
}

