terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">=5.0.0, < 6.0.0"
    }
  }
  required_version = ">= 1.5.0"
}
