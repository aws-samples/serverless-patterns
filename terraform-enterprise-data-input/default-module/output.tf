# Outputs for various retrieved data
output "amis" {
 value = local.amis
}


output "ec2_user_ssh" {
 value = data.aws_ssm_parameter.ec2_user_ssh.value
}


output "kms_s3_server_side" {
 value = data.aws_kms_key.s3_server_side.arn
}
