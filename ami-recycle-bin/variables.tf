variable "rbin_retention_period_value" {
  type = number
  default = 30
  description = "The period value for which the retention rule is to retain resources"
}

variable "rbin_retention_period_unit" {
  type = string
  default = "DAYS"
  description = "The unit of time in which the retention period is measured. Currently, only DAYS is supported"
}

variable "resource_tag_key" {
    type = string
    default = "Project"
    description = "The tag key"
}

variable "resource_tag_value" {
    type = string
    default = "Test-Retention"
    description = "The tag value"
}

variable "cw_retention_period" {
    type = number
    default = 14
    description = "Specifies the number of days you want to retain log events in the specified log group"
}

variable "dry_run" {
  type = bool
  default = true
  description = "If set to true, the script will not delete any resources"
}