variable "lambda_root" {
  type        = string
  description = "The relative path to the source of the lambda"
  default     = "../lambda"
}

variable "layers_root" {
  type        = string
  description = "The relative path to the source of the lambda layers code"
  default     = "../layers"
}

variable "default_tags" {
  type        = map(string)
  description = "Default tags for the module"
  default = {
    Environment = "AFT"
    Owner       = "RealmIDX"
    Project     = "AFT"
    CostCenter  = "RealmIDX"
  }
}

variable "cloudwatch_log_group_retention" {
  description = "Lambda CloudWatch log group retention period"
  type        = string
  default     = "365"
  validation {
    condition     = contains(["1", "3", "5", "7", "14", "30", "60", "90", "120", "150", "180", "365", "400", "545", "731", "1827", "3653", "0"], var.cloudwatch_log_group_retention)
    error_message = "Valid values for var: cloudwatch_log_group_retention are (1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 3653, and 0)."
  }
}

variable "private1_subnet_id" {
  type        = string
  description = "Private Subnet 1"
  default     = "subnet-0a24b06696515e696"
}

variable "private2_subnet_id" {
  type        = string
  description = "Private Subnet 2"
  default     = "subnet-0ffc68b0ddebae39e"
}


variable "private_sg_id" {
  type        = string
  description = "Private Subnet Security Group"
  default     = "sg-075705e6fc88af432"
}