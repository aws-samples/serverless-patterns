variable "account_email_mapping" {
  description = "Account id and email id mapping of AMI Consumer AWS Account's"
  type = list(object({
    account = string
    email   = string
  }))
}