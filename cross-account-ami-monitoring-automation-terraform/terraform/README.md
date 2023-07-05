# Setup auditing and monitoring for cross account shared Amazon Machine Image(AMI)
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | >= 4.20.1 |

## Providers

No providers.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_ami_creator"></a> [ami\_creator](#module\_ami\_creator) | ./modules/ami_creator | n/a |
| <a name="module_consumer_account_A"></a> [consumer\_account\_A](#module\_consumer\_account\_A) | ./modules/ami_consumer | n/a |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_account_email_mapping"></a> [account\_email\_mapping](#input\_account\_email\_mapping) | Account id and email id mapping of AMI Consumer AWS Account's | <pre>list(object({<br>    account = string<br>    email   = string<br>  }))</pre> | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_AWS_Account_Owners"></a> [AWS\_Account\_Owners](#output\_AWS\_Account\_Owners) | Email list of AWS account owners. Note: These email id's needs to be verified. |