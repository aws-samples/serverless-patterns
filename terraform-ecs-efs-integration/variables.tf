variable "env" {
  type        = string
  description = "Name of the environment the infrastructure is for"
}

variable "organization" {
  type        = string
  description = "Name of the organization the infrastructure is for"
}

variable "vpc_id" {
  type        = string
  description = "VPC ID for ECS Task and EFS"
}

variable "task_cpu" {
  type        = number
  description = "VCPUs for ECS Task"
}

variable "task_memory" {
  type        = number
  description = "Memory for ECS Task"
}