## Amazon Elastic Container Service(ECS) and Amazon Bedrock Integration

This setup involves setting up Amazon Elastic Container Registry (ECR) to store containers, pushing code into the registry, and using Amazon ECS to host a sample web application.

During the build process, a container will be created, pushed to ECR, and deployed as an Amazon ECS Service. Users accessing the web application can upload a PDF document ( alternatively they can download a sample PDF applicaiton from the application and then upload it to summzarize ) and request the application to summarize it. The application makes API calls to Amazon Bedrock to generate answers using its foundation model. Logs are sent to AWS CloudWatch, and security is managed through KMS Keys and IAM Roles.

## Getting started with Terraform Serverless Patterns

Read more about general requirements and deployment instructions for Terraform Serverless Patterns [here](https://github.com/aws-samples/serverless-patterns/blob/main/terraform-fixtures/docs/README.md).

Before attempting this pattern, you must enable [model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) in your AWS Account. To provide you flexibility with foundation models, you can enable all or some of the foundation models. This pattern employs the anthropic.claude-v2 model by default so that's must be enabled for this pattern to work

You also need [docker](https://www.docker.com/) and md5 to be installed on your testing machine

## Deployment and Testing Instructions

To deploy this setup, you must provide the AWS VPC ID and the Subnet ID(s) where you plan to deploy this configuration. This setup assumes you will specify a public subnet for accessing the application over the internet. If you opt for a private subnet, ensure there's a VPN connection to your VPC. Please note that the subnet type defaults to public as specified in the variables.tf file. It's mandatory that the specified subnets have internet connectivity, usually by a NAT Gateway for private subnets or alternative methods where necessary.

Additionally, You can use AWS PrivateLink to create a private connection between your VPC and Amazon Bedrock. You can access Amazon Bedrock as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. You establish this private connection by creating an interface endpoint, powered by AWS PrivateLink. For more information, see [ Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the AWS PrivateLink Guide.

Optionally, you can also specify memory, cpu and number of service started by Amazon ECS. These values default to entires in the variable.tf file if not provided at deployment.

```shell
# terraform init
terraform init

# terraform plan with sample values for vpc and subnet
terraform plan  -var="aws_vpc_id=vpc-xxxx" -var='aws_subnets=["subnet-xxxx","subnet-xxxx","subnet-xxxx"]' 

# terraform apply
terraform apply -var="aws_vpc_id=vpc-xxxx" -var='aws_subnets=["subnet-xxxx","subnet-xxxx","subnet-xxxx"]' 

# Once deployed, as part of the output, you will get a web-url which you can use to access the application
dns_record_for_application = http://testing-serverlessland-genai-app-xxxxxxxxxx.us-east-1.elb.amazonaws.com:8080

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
| <a name="provider_terraform"></a> [terraform](#provider\_terraform) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_alb.this_aws_alb_front_end](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/alb) | resource |
| [aws_alb_listener.this_aws_alb_listener_front_end](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/alb_listener) | resource |
| [aws_cloudwatch_log_group.this_aws_cloudwatch_log_group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_group) | resource |
| [aws_ecr_lifecycle_policy.ecr_lifecycle_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecr_lifecycle_policy) | resource |
| [aws_ecr_repository.this_aws_ecr_repository](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecr_repository) | resource |
| [aws_ecs_cluster.this_aws_ecs_cluster](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_cluster) | resource |
| [aws_ecs_service.this_aws_ecs_service](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_service) | resource |
| [aws_ecs_task_definition.this_aws_ecs_task_definition](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_task_definition) | resource |
| [aws_iam_policy.this_aws_iam_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_policy_attachment.this_aws_iam_policy_attachment](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy_attachment) | resource |
| [aws_iam_role.this_aws_iam_role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_kms_alias.this_aws_kms_alias](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/kms_alias) | resource |
| [aws_kms_key.this_aws_kms_key](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/kms_key) | resource |
| [aws_lb_target_group.this_aws_lb_target_group_front_end](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb_target_group) | resource |
| [aws_security_group.this_aws_security_group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group) | resource |
| [terraform_data.this_terraform_data_build_ecr_image](https://registry.terraform.io/providers/hashicorp/terraform/latest/docs/resources/data) | resource |
| [aws_caller_identity.current](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/caller_identity) | data source |
| [aws_ecr_image.this_aws_ecr_image](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/ecr_image) | data source |
| [aws_region.current](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/region) | data source |
| [external_external.this_external](https://registry.terraform.io/providers/hashicorp/external/latest/docs/data-sources/external) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_aws_subnets"></a> [aws\_subnets](#input\_aws\_subnets) | A list of subnets inside the VPC | `set(any)` | n/a | yes |
| <a name="input_aws_vpc_id"></a> [aws\_vpc\_id](#input\_aws\_vpc\_id) | VPC ID for ECS Servcie and Task | `string` | n/a | yes |
| <a name="input_desired_count"></a> [desired\_count](#input\_desired\_count) | The number of instances of the task definition to place and keep running | `number` | `1` | no |
| <a name="input_env"></a> [env](#input\_env) | Name of the environment this infrastructure is for | `string` | `"testing"` | no |
| <a name="input_launch_type"></a> [launch\_type](#input\_launch\_type) | Launch type for the service. | `string` | `"FARGATE"` | no |
| <a name="input_organization"></a> [organization](#input\_organization) | Name of the organization this infrastructure is for | `string` | `"serverlessland"` | no |
| <a name="input_subnet_type"></a> [subnet\_type](#input\_subnet\_type) | The type of subnet which you are providing(private or public) | `string` | `"public"` | no |
| <a name="input_task_cpu"></a> [task\_cpu](#input\_task\_cpu) | VCPUs for task task | `number` | `512` | no |
| <a name="input_task_memory"></a> [task\_memory](#input\_task\_memory) | Memory for task task | `number` | `2048` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_dns_record_for_application"></a> [dns\_record\_for\_application](#output\_dns\_record\_for\_application) | DNS Address to Access the Application |
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
