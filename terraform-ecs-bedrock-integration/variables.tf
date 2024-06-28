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
  description = "VCPUs for task task"
  default     = 512
}

variable "task_memory" {
  type        = number
  description = "Memory for task task"
  default     = 2048
}

variable "launch_type" {
  type        = string
  description = "Launch type for the service."
  default     = "FARGATE"
}

variable "desired_count" {
  type        = number
  description = "The number of instances of the task definition to place and keep running"
  default     = 1
}

variable "subnet_type" {
  type        = string
  description = "The type of subnet which you are providing(private or public)"
  default     = "public"
}

####################################################
# Variables without Defaults
####################################################
variable "aws_vpc_id" {
  type        = string
  description = "VPC ID for ECS Servcie and Task"
}

variable "aws_subnets" {
  type        = set(any)
  description = "A list of subnets inside the VPC"
}