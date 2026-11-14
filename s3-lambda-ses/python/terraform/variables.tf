variable aws_region {
  type        = string
  # default     = "us-east-1"
  description = "Please provide a region name to deploy the resources ex: us-east-1"
}

variable bucket_name {
  type        = string
  default     = ""
  description = " (Required) Please provide the bucket name or else a new bucket will be created for you"
}

variable acl_value {
  default = "private"
}

variable lambda_role_name {
  type        = string
  default     = "S3_Lambda_SES"
  description = "Provide a Lambda Role name or else leave the default value"
}

variable lambda_iam_policy_name {
  type        = string
  default     = "LambdaAccessForS3AndSES"
  description = "Provide a Lambda Policy name or else leave the default value"
}

variable timeout {
  type        = number
  default     = 5
  description = "(Optional) Provide Lambda timeout value in seconds"
}

variable environment {
  type        = string
  default     = "Dev"
  description = "(Optional) Provide environment value tag"
}

variable sender_email {
  type        = string
  # default     = "xyz@gmail.com"
  description = "(Required) Provide SES verifed sender email address to send notifications"
}

variable receiver_email {
  type        = string
  # default     = "xyz@gmail.com"
  description = "(Required) Provide verified receiver email address if SES in sandbox envrionment if in production provide a valid value"
}

variable prefix {
  type        = string
  default     = ""
  description = "Enter a single optional prefix to limit the notifications to objects with keys that starts with matching characters, ex: images/"
}

variable suffix {
  type        = string
  default     = ""
  description = "Enter a single optional suffix to limit the notifications to objects with keys that end with matching characters, ex: .jpg"
}

variable function_name {
    type        = string
    default     = "LambdaSES"
    description = "Enter a Lambda Function name or else you can use the default name"
}