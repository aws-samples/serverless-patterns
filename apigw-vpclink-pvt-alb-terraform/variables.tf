variable "vpc_id" {
  type = string
  //fake
  default = "vpc-123a45b6"
}
variable "private_subnets" {
  type = list(any)
  //fake
  default = [
      "subnet-5432bca1",
      "subnet-1abc2345"
  ]
}