terraform {
  required_version = ">= 1.0.0" # Ensure that the Terraform version is 1.0.0 or higher

  required_providers {
    aws = {
      source = "hashicorp/aws" # Specify the source of the AWS provider
      version = ">= 5.0.0"        # Use a version of the AWS provider that is compatible with version
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

module "eventbridge_connection" {
  source = "./modules/eventbridge_connection"

  vpc_id       = var.vpc_id
  on_premises_cidr    = var.on_premises_cidr
  api_domain_name    = var.api_domain_name
  private_subnet_ids = var.private_subnet_ids
  api_key_secret_arn         = var.api_key_secret_arn
}

module "state_machine" {
  source = "./modules/state_machine"

  connection_arn        = module.eventbridge_connection.connection_arn
  connection_secret_arn = module.eventbridge_connection.connection_secret_arn
  api_domain_name       = var.api_domain_name
  log_retention_days    = 30
}
