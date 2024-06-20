# Retrieve details about the VPC
data "aws_vpc" "vpc" {
 tags = {
   Environment = var.short_env
 }
}

# Retrieve subnets within the VPC
data "aws_subnets" "subnets_group" {
 filter {
   name   = "vpc-id"
   values = [data.aws_vpc.vpc.id]
 }
}

data "aws_subnet" "subnets" {
 for_each = toset(data.aws_subnets.subnets_group.ids)
 id       = each.value
}

# Retrieve a KMS key
data "aws_kms_key" "s3_server_side" {
 key_id = "alias/${data.aws_iam_account_alias.current.account_alias}-s3-server-side"
}

# Retrieve an SSM parameter
data "aws_ssm_parameter" "ec2_user_ssh" {
 name = "/${var.short_env}/passwords/ssh/ec2-user"
}


# Retrieve an AMI based on filters
data "aws_ami" "amzn2" {
 owners      = ["amazon"] # Use the official Amazon owner ID for Amazon Linux AMIs
 most_recent = true


 filter {
   name   = "name"
   values = ["amzn2-ami-hvm-*-x86_64-gp2"] # Adjust this filter to match the AMI you want
 }
}
