# Use if you have remote state setup, other leave commented out
# terraform {
#  backend "s3" {
#    region  = "us-east-1"
#    bucket = "fargano-statefiles"
#    key    = "tf-demo/variables-demo.tfstate"
#    encrypt        = "true"
#   dynamodb_table = "fargano-tflock"
#  }
#}

terraform {
  required_providers {
    rabbitmq = {
      source  = "cyrilgdn/rabbitmq"
    }
  }
}

provider "aws"{
  region = var.region
}

provider "aws"{
  alias = "sec"
  region = var.sec_region
}

provider "rabbitmq" {
  endpoint = aws_mq_broker.primary.instances.0.console_url
  username = var.user
  password = var.password
}

provider "rabbitmq" {
  alias = "secondary"
  endpoint = aws_mq_broker.secondary.instances.0.console_url
  username = var.user
  password = var.password
}