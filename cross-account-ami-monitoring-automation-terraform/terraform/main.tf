module "ami_creator" {
  providers = {
    aws = aws.ami-creation-account
  }
  source                = "./modules/ami_creator"
  account_email_mapping = var.account_email_mapping
  consumer              = true
}


module "consumer_account_A" {
  providers = {
    aws = aws.ami-consumer-account_1
  }
  source               = "./modules/ami_consumer"
  configuration_inputs = module.ami_creator.configurations_details
}

output "AWS_Account_Owners" {
  description = "Email list of AWS account owners. Note: These email id's needs to be verified."
  value       = var.account_email_mapping
}
