variable "create" {
  default = true
}


variable "role_arn" {
  default =""
}

variable "connections" {
  type    = list(string)
  default = []
}

variable "dpu" {
  default = 2
}

variable "script_location" {}

variable "command_name" {
  default = ""
}

variable "language" {
  default = "python"
}

variable "bookmark" {
  default     = "disabled"
  description = "It can be enabled, disabled or paused."
}

variable "bookmark_options" {
  type = map(string)

  default = {
    enabled  = "job-bookmark-enable"
    disabled = "job-bookmark-disable"
    paused   = "job-bookmark-pause"
  }
}

variable "temp_dir" {
}

variable "description" {
  default = ""
}

variable "max_retries" {
  default = 0
}

variable "timeout" {
  default = 2880
}

variable "max_concurrent" {
  default = 5
}

variable "arguments" {
  type    = map(string)
  default = {}
}

variable "s3_bucket_name" {}
variable "s3_bucket_arn" {}