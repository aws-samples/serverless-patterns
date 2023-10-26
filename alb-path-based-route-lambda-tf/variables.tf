variable "region" {
    type=string
    description = "AWS Region where deploying resources"
    default = "us-east-2"
}

variable "vpc_cidr" {
    type=string
    description = "CIDR block for Batch VPC"
    default = "10.0.0.0/16"
}
