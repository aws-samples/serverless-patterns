/*output "subnet_ids" {
  value = aws_subnet.subnet[*].id
  #value = aws_subnet.example.id
}*/
# Outputs for various retrieved data
output "amis" {
  value = local.amis
}

output "ec2_user_ssh" {
  value = data.aws_ssm_parameter.ec2_user_ssh.insecure_value
}

output "kms_s3_server_side" {
  value = data.aws_kms_key.s3_server_side.arn
}

output "subnet_cidr_blocks" {
  value = [for s in data.aws_subnet.subnet : s.cidr_block]
}