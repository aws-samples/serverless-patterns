variable "region" {
  type        = string
  default     = "eu-west-2"
  description = "Region where the stack is deployed"
}

variable "s3_compression_format" {
  type        = string
  default     = "GZIP"
  description = "May be GZIP, Snappy, Zip, or Hadoop-Compatiable Snappy. See https://docs.aws.amazon.com/firehose/latest/dev/create-configure.html"

  validation {
    condition = contains(["GZIP",
      "Snappy",
      "Zip",
      "Hadoop-Compatible Snappy"],
    var.s3_compression_format)
    error_message = "Not an allowed compression format."
  }
}

variable "output_format" {
  type        = string
  default     = "json"
  description = "Output format of metrics. You should probably not modify this value; the default format is supported, but others may not be."

  validation {
    condition     = contains(["json", "opentelemetry0.7"], var.output_format)
    error_message = "Not an allowed output format."
  }
}

variable "tags" {
  type        = map(string)
  default     = {}
  description = "A map of tags to apply to resources created by this module."
}
