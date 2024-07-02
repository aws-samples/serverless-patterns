provider "aws" {
  region = "us-east-1"
}

# Passing data to sub-module
module "my_module" {
  source = "./default_module"
  #vpc_id   = data.aws_vpc.main.id
  #vpc_cidr = data.aws_vpc.main.cidr_block
  #ami      = var.ami
}

# Receiving data from sub-module
/*output "subnet_ids" {
  value = module.my_module.subnet_ids
}*/

output "amis" {
  value = module.my_module.amis
}

output "ec2_user_ssh" {
  value     = module.my_module.ec2_user_ssh
  #sensitive = true
}

output "kms_s3_server_side" {
  value = module.my_module.kms_s3_server_side
}

output "subnet_cidr_blocks" {
  value = module.my_module.subnet_cidr_blocks
}
/*output "My_Instance_ID" {
  value = module.my_module.my_instance_id
} */