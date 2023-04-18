# Replace default value with your desired AWS Region
variable "aws_region" {
  type    = string
  default = "us-east-1"
}

# Tags
variable "tags" {
  type        = map(any)
  description = "Tags to apply to resources"
  default = {
    IAC_PROVIDER = "Terraform"
  }
}
