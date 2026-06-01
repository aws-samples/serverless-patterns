variable "connection_arn" {
  type        = string
  description = "ARN of the EventBridge connection"
}

variable "connection_secret_arn" {
  type        = string
  description = "ARN of the secret for EventBridge connection"
}

variable "api_domain_name" {
  type        = string
  description = "Domain name for the API"
}

variable "log_retention_days" {
  type        = number
  description = "Number of days to retain logs"
  default     = 30
}