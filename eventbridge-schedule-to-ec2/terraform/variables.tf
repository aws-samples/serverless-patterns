variable "region" {
    type=string
    description = "AWS Region where deploying resources"
    default = "us-east-1"
}

variable "aws_profile_name" {
    type=string
    description = "AWS CLI credentials profile name"
    default="default"
}

variable "vpc_cidr" {
    type=string
    description = "CIDR block for VPC"
    default = "10.0.0.0/16"
}

variable "subnet_cidr" {
    type=string
    description = "CIDR block for the subnet"
    default = "10.0.0.0/24"
}
