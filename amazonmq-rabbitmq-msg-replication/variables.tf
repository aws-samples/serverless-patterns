
variable "env_name" {
  description = "the name of your stack, e.g. \"demo\""
  default     = "demo"
}

variable "region" {
  description = "the AWS region in which primary resources are created"
  default     = "us-east-1"
}

variable "sec_region" {
  description = "the AWS region in which secondary resources are created"
  default     = "us-east-2"
}

variable "user" {
  description = "Admin user for the brokers"
  default     = "exampleuser"
}

variable "password" {
  description = "Admin user password"
  default     = "examplepassword"
}

variable "regex" {
  description = "Regular expression filter for federation"
  default     = "^amq\\."
}

variable "ttl" {
  description = "Time to live of messages in the second region, default is set low for demo purposes to see queue clear"
  default = 60000
}