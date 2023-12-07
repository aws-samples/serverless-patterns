## Amazon EFS and Amazon ECS Integration

This pattern creates an Amazon EFS file system and integrates with ECS for a persisent file storage in a containerized environment.

You will build a container as part of the build, publish it into ECR, and then publish it as an ECS Task in the end. A sample file will be created in the EFS (persistent file system) after the task has been completed. The security component is likewise handled by KMS Keys and IAM Roles.

## Getting started with Terraform Serverless Patterns

Read more about general requirements and deployment instructions for Terraform Serverless Patterns [here](https://github.com/aws-samples/serverless-patterns/blob/main/terraform-fixtures/docs/README.md).

You also need [docker](https://www.docker.com/) and md5 to be installed on your testing machine

## Deployment and Testing Instructions

The deployment will require you to provide the AWS VPC id along with the Subnet id(s) where you want this pattern to be deployed. 

Optionally, you can also specify env and organization (tagging purposes) and task_cpu and task_memory (Amazon ECS Task compute purposes). These values default to entires in the variable.tf file if not provided at deployment.

```shell
# terraform init
terraform init

# terraform plan with sample values for vpc and subnet
terraform plan  -var="aws_vpc_id=vpc-xxxx" -var='aws_subnets=["subnet-xxxx","subnet-xxxx","subnet-xxxx"]' 

# terraform apply
terraform apply -var="aws_vpc_id=vpc-xxxx" -var='aws_subnets=["subnet-xxxx","subnet-xxxx","subnet-xxxx"]' 
```

Once deployed you can run the ECS task from the ECS Console or via AWS CLI which will create a sample file on the persistent storage using Amazon EFS

```shell
aws ecs run-task \
    --cluster testing-serverlessland-efs-updater \
    --task-definition testing-serverlessland-efs-updater:1 \
    --network-configuration "awsvpcConfiguration={subnets=[subnet-xxxx],securityGroups=[sg-xxxx],assignPublicIp=DISABLED}" \
    --count 1 \
    --launch-type FARGATE
```


<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | >= 5.24 |
| <a name="requirement_external"></a> [external](#requirement\_external) | >= 2.3 |
| <a name="requirement_null"></a> [null](#requirement\_null) | >= 3.2 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | >= 5.24 |
| <a name="provider_external"></a> [external](#provider\_external) | >= 2.3 |
| <a name="provider_null"></a> [null](#provider\_null) | >= 3.2 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_cloudwatch_log_group.aws_cloudwatch_log_group_efs_updater](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_group) | resource |
| [aws_ecr_lifecycle_policy.ecr_lifecycle_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecr_lifecycle_policy) | resource |
| [aws_ecr_repository.aws_ecr_repository_efs_updater](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecr_repository) | resource |
| [aws_ecs_cluster.this_ecs_cluster](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_cluster) | resource |
| [aws_ecs_task_definition.aws_ecs_task_definition_efs_updater](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_task_definition) | resource |
| [aws_efs_file_system.efs_volume](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/efs_file_system) | resource |
| [aws_efs_mount_target.ecs_space_az](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/efs_mount_target) | resource |
| [aws_iam_policy.this_iam_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_policy_attachment.this_aws_iam_policy_attachment](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy_attachment) | resource |
| [aws_iam_role.this_task_role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_kms_alias.aws_kms_key_alias](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/kms_alias) | resource |
| [aws_kms_key.aws_kms_key](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/kms_key) | resource |
| [aws_security_group.this_security_group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group) | resource |
| [null_resource.null_resource_efs_updater](https://registry.terraform.io/providers/hashicorp/null/latest/docs/resources/resource) | resource |
| [aws_caller_identity.current](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/caller_identity) | data source |
| [aws_region.current](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/region) | data source |
| [external_external.external_efs_updater](https://registry.terraform.io/providers/hashicorp/external/latest/docs/data-sources/external) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_aws_subnets"></a> [aws\_subnets](#input\_aws\_subnets) | A list of subnets inside the VPC | `set(any)` | n/a | yes |
| <a name="input_aws_vpc_id"></a> [aws\_vpc\_id](#input\_aws\_vpc\_id) | VPC ID for ECS Task and EFS | `string` | n/a | yes |
| <a name="input_env"></a> [env](#input\_env) | Name of the environment this infrastructure is for | `string` | `"testing"` | no |
| <a name="input_organization"></a> [organization](#input\_organization) | Name of the organization this infrastructure is for | `string` | `"serverlessland"` | no |
| <a name="input_task_cpu"></a> [task\_cpu](#input\_task\_cpu) | VCPUs for ECS Task | `number` | `512` | no |
| <a name="input_task_memory"></a> [task\_memory](#input\_task\_memory) | Memory for ECS Task | `number` | `2048` | no |

## Outputs

No outputs.
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
