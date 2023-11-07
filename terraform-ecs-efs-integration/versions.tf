terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.24"
    }
    external = {
      source  = "hashicorp/external"
      version = ">= 2.3"
    }
    null = {
      source  = "hashicorp/null"
      version = ">= 3.2"
    }
  }
}