variable "domain_name" {
  type    = string
  default = " " // private custom domaiun name
  validation {
    condition     = can(regex("^[a-zA-Z0-9.-]+$", var.domain_name))
    error_message = "Domain name can only contain alphanumeric characters, dots, and hyphens."
  }
}

variable "region" {
  type    = string
  default = " " //region
}