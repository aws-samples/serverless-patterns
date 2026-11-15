# Input variable definitions

variable "aws_region" {
  description = "AWS region for all resources."
  type    = string
  default = "us-east-1"
}

variable "vpc_cidr" {
  description = "CIDR block for the vpc"
  type    = string
  default = "10.0.0.0/16"
}

variable "public_cidr" {
	type = list
	default = ["10.0.11.0/24", "10.0.12.0/24"]
}

variable "app_cidr" {
	type = list
	default = ["10.0.21.0/24", "10.0.22.0/24"]
}

variable "db_cidr" {
	type = list
	default = ["10.0.31.0/24", "10.0.32.0/24", "10.0.33.0/24"]
}

variable "azs" {
	type = list
	default = ["us-east-1a", "us-east-1b"]
}

variable "db_azs" {
	type = list
	default = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

variable "username" {
	type = string
	default = "lambda"
}

variable "ami_id" {
	type = string
	default = "ami-0c02fb55956c7d316"
}

variable "rds_proxy_name" {
	type = string
	default = "test-aurora-mysql"
}

variable "log_retention" {
  description = "log retention in days"
  type = number
  default = 7
}