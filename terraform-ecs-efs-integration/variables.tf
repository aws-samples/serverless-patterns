####################################################
# Variables with Defaults
####################################################
variable "env" {
  type        = string
  description = "Name of the environment this infrastructure is for"
  default     = "testing"
}

variable "organization" {
  type        = string
  description = "Name of the organization this infrastructure is for"
  default     = "serverlessland"
}

variable "task_cpu" {
  type        = number
  description = "VCPUs for ECS Task"
  default     = 512
}

variable "task_memory" {
  type        = number
  description = "Memory for ECS Task"
  default     = 2048
}

####################################################
# Variables without Defaults
####################################################
variable "aws_vpc_id" {
  type        = string
  description = "VPC ID for ECS Task and EFS"
}

variable "aws_subnets" {
  type        = set(any)
  description = "A list of subnets inside the VPC"
}