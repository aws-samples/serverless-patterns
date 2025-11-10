variable "vpc_id" {
  type        = string
  description = "ID of the VPC linked to on-premises network"
}

variable "private_subnet_ids" {
  type        = list(string)
  description = "List of private subnet IDs in the VPC"
}

variable "on_premises_cidr" {
  type        = string
  description = "CIDR block of the on-premises network"
}

# Choose either a domain name if you have one configured for your API, or and IP address
variable "api_domain_name" {
  type        = string
  description = "Domain name of the on-premises API"
}

# variable "api_ip_address" {
#   type        = string
#   description = "IP address of the on-premises API"
# }

# If using Basic or OAuth, change the authentication mechanism
variable "api_key_secret_arn" {
  type        = string
  description = "ARN of the existing secret containing the API key"
}