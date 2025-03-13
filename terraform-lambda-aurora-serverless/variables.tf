variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.100.0.0/16"
}

variable "db_username" {
  description = "Database administrator username"
  type        = string
  default     = "admin"
}

# Example of valid password: "MyDBPassword123!"
variable "db_password" {
  description = "Database administrator password, please change it"
  type        = string
  sensitive   = true
}

variable "database_name" {
  description = "Name of the database"
  type        = string
  default     = "mydb"
}

variable "aurora_min_capacity" {
  description = "Minimum Aurora capacity unit"
  type        = number
  default     = 1
}

variable "aurora_max_capacity" {
  description = "Maximum Aurora capacity unit"
  type        = number
  default     = 2
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
  default     = "aurora-lambda"
}

variable "lambda_src_path" {
  description = "Path to the Lambda function zip file"
  type        = string
  default     = "src/function"
}

variable "lambda_handler" {
  description = "Lambda function handler"
  type        = string
  default     = "app.lambda_handler"
}

variable "lambda_runtime" {
  description = "Lambda function runtime"
  type        = string
  default     = "python3.12"
}

variable "lambda_timeout" {
  description = "Lambda function timeout in seconds"
  type        = number
  default     = 30
}

variable "lambda_memory_size" {
  description = "Lambda function memory size in MB"
  type        = number
  default     = 128
}
