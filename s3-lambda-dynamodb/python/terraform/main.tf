provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      Project         = var.project
      Team            = var.team
      CostCentre      = var.costcentre
    }
  }
}

module "s3_event" {
    source = "./modules/s3_event"
    table_name = module.dynamodb.table_name
}

module "dynamodb" {
    source = "./modules/dynamodb"
}