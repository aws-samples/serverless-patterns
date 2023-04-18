## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | n/a |
| <a name="provider_local"></a> [local](#provider\_local) | n/a |
| <a name="provider_random"></a> [random](#provider\_random) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_amplify_app.sample_app](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/amplify_app) | resource |
| [aws_appsync_datasource.sample_appsync_dynamodb_datasource](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/appsync_datasource) | resource |
| [aws_appsync_graphql_api.sample_appsync_graphql_api](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/appsync_graphql_api) | resource |
| [aws_appsync_resolver.sample_appsync_resolver_mutation_delete_one_object](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/appsync_resolver) | resource |
| [aws_appsync_resolver.sample_appsync_resolver_query_get_all_objects](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/appsync_resolver) | resource |
| [aws_appsync_resolver.sample_appsync_resolver_query_get_object](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/appsync_resolver) | resource |
| [aws_cloudwatch_event_bus.sample_event_bus](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_bus) | resource |
| [aws_cloudwatch_event_rule.default_event_bus_to_sample_event_bus](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_rule) | resource |
| [aws_cloudwatch_event_rule.sample_landing_bucket_object_created](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_rule) | resource |
| [aws_cloudwatch_event_rule.sns_default_event_bus_to_sample_event_bus](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_rule) | resource |
| [aws_cloudwatch_event_target.default_event_bus](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_target) | resource |
| [aws_cloudwatch_event_target.sample_step_function](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_target) | resource |
| [aws_codecommit_repository.sample_codecommit_repo](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/codecommit_repository) | resource |
| [aws_cognito_identity_pool.sample_identity_pool](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_identity_pool) | resource |
| [aws_cognito_identity_pool_roles_attachment.sample_identity_pool_auth_roles_attachment](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_identity_pool_roles_attachment) | resource |
| [aws_cognito_user.sample_admin_cognito_users](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_user) | resource |
| [aws_cognito_user.sample_standard_cognito_users](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_user) | resource |
| [aws_cognito_user_group.sample_admin_cognito_user_group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_user_group) | resource |
| [aws_cognito_user_group.sample_standard_cognito_user_group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_user_group) | resource |
| [aws_cognito_user_in_group.sample_admin_cognito_user_group_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_user_in_group) | resource |
| [aws_cognito_user_in_group.sample_standard_cognito_user_group_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_user_in_group) | resource |
| [aws_cognito_user_pool.sample_user_pool](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_user_pool) | resource |
| [aws_cognito_user_pool_client.sample_user_pool_client](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cognito_user_pool_client) | resource |
| [aws_dynamodb_table.sample_output](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dynamodb_table) | resource |
| [aws_iam_policy.sample_dynamodb_restricted_access_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_policy.sample_dynamodb_restricted_access_read_only_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_policy.sample_eventbridge_invoke_custom_sample_event_bus_restricted_access_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_policy.sample_eventbridge_invoke_sfn_state_machine_restricted_access_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_policy.sample_s3_restricted_access_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_policy.sample_ssm_restricted_access_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_role.sample_amplify_codecommit](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role.sample_appsync_dynamodb_restricted_access](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role.sample_cognito_admin_group_restricted_access](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role.sample_cognito_authrole_restricted_access](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role.sample_cognito_standard_group_restricted_access](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role.sample_cognito_unauthrole_restricted_access](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role.sample_eventbridge_invoke_custom_sample_event_bus_restricted_access](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role.sample_eventbridge_invoke_sfn_state_machine_restricted_access](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role.sample_step_functions_master_restricted_access](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_user.sample_gitlab_mirroring](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_user) | resource |
| [aws_iam_user_policy.sample_gitlab_mirroring_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_user_policy) | resource |
| [aws_s3_bucket.sample_app_storage_bucket](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket) | resource |
| [aws_s3_bucket.sample_input_bucket](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket) | resource |
| [aws_s3_bucket.sample_landing_bucket](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket) | resource |
| [aws_s3_bucket.sample_output_bucket](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket) | resource |
| [aws_s3_bucket_cors_configuration.sample_app_storage_bucket_cors](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_cors_configuration) | resource |
| [aws_s3_bucket_cors_configuration.sample_input_bucket_cors](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_cors_configuration) | resource |
| [aws_s3_bucket_cors_configuration.sample_landing_bucket_cors](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_cors_configuration) | resource |
| [aws_s3_bucket_cors_configuration.sample_output_bucket_cors](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_cors_configuration) | resource |
| [aws_s3_bucket_lifecycle_configuration.sample_input_bucket_lifecycle_config](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_lifecycle_configuration) | resource |
| [aws_s3_bucket_lifecycle_configuration.sample_landing_bucket_lifecycle_config](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_lifecycle_configuration) | resource |
| [aws_s3_bucket_lifecycle_configuration.sample_output_bucket_lifecycle_config](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_lifecycle_configuration) | resource |
| [aws_s3_bucket_notification.sample_app_storage_bucket_events](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_notification) | resource |
| [aws_s3_bucket_notification.sample_input_bucket_events](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_notification) | resource |
| [aws_s3_bucket_notification.sample_landing_bucket_events](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_notification) | resource |
| [aws_s3_bucket_notification.sample_output_bucket_events](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_notification) | resource |
| [aws_s3_bucket_policy.sample_app_storage_bucket_restrict_file_types](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_policy) | resource |
| [aws_s3_bucket_policy.sample_input_bucket_restrict_file_types](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_policy) | resource |
| [aws_s3_bucket_policy.sample_landing_bucket_restrict_file_types](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_policy) | resource |
| [aws_s3_bucket_policy.sample_output_bucket_restrict_file_types](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_policy) | resource |
| [aws_s3_bucket_public_access_block.sample_app_storage_bucket_block_public_access](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_public_access_block) | resource |
| [aws_s3_bucket_public_access_block.sample_input_bucket_block_public_access](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_public_access_block) | resource |
| [aws_s3_bucket_public_access_block.sample_landing_bucket_block_public_access](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_public_access_block) | resource |
| [aws_s3_bucket_public_access_block.sample_output_bucket_block_public_access](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_public_access_block) | resource |
| [aws_sfn_state_machine.sample_sfn_state_machine](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sfn_state_machine) | resource |
| [aws_ssm_parameter.sample_app_storage_bucket_name](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ssm_parameter) | resource |
| [aws_ssm_parameter.sample_dynamodb_output_table_name](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ssm_parameter) | resource |
| [aws_ssm_parameter.sample_input_bucket_name](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ssm_parameter) | resource |
| [aws_ssm_parameter.sample_output_bucket_name](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ssm_parameter) | resource |
| [local_file.tf_outputs](https://registry.terraform.io/providers/hashicorp/local/latest/docs/resources/file) | resource |
| [random_uuid.sample_app_storage_bucket_uuid](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/uuid) | resource |
| [random_uuid.sample_event_bus_uuid](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/uuid) | resource |
| [random_uuid.sample_file_uuid](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/uuid) | resource |
| [random_uuid.sample_input_bucket_uuid](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/uuid) | resource |
| [random_uuid.sample_landing_bucket_uuid](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/uuid) | resource |
| [random_uuid.sample_output_bucket_uuid](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/uuid) | resource |
| [random_uuid.sample_output_uuid](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/uuid) | resource |
| [aws_caller_identity.current](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/caller_identity) | data source |
| [aws_iam_policy_document.sample_amplify_trust_relationship](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_app_storage_bucket_restrict_file_types](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_appsync_trust_relationship](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_cognito_admin_group_trust_relationship](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_cognito_authrole_trust_relationship](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_cognito_standard_group_trust_relationship](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_cognito_unauthrole_trust_relationship](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_dynamodb_restricted_access_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_dynamodb_restricted_access_read_only_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_eventbridge_invoke_custom_sample_event_bus_restricted_access_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_eventbridge_invoke_sfn_state_machine_restricted_access_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_eventbridge_trust_relationship](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_input_bucket_restrict_file_types](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_landing_bucket_restrict_file_types](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_output_bucket_restrict_file_types](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_s3_restricted_access_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_ssm_restricted_access_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.sample_step_function_trust_relationship](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_region.current](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/region) | data source |
| [aws_ssm_parameter.ssm_github_access_token](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/ssm_parameter) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_app_name"></a> [app\_name](#input\_app\_name) | The name of the Amplify Application | `string` | `"sample-App"` | no |
| <a name="input_create_amplify_app"></a> [create\_amplify\_app](#input\_create\_amplify\_app) | Conditional creation of AWS Amplify Web Application | `bool` | `true` | no |
| <a name="input_create_restricted_access_roles"></a> [create\_restricted\_access\_roles](#input\_create\_restricted\_access\_roles) | Conditional creation of restricted access roles | `bool` | `true` | no |
| <a name="input_create_sample_amplify_domain_association"></a> [create\_sample\_amplify\_domain\_association](#input\_create\_sample\_amplify\_domain\_association) | n/a | `bool` | `false` | no |
| <a name="input_create_sample_sfn_state_get_sample_input_file"></a> [create\_sample\_sfn\_state\_get\_sample\_input\_file](#input\_create\_sample\_sfn\_state\_get\_sample\_input\_file) | Enables creation of GetSampleInputFile sfn state | `bool` | `true` | no |
| <a name="input_dynamodb_ttl_attribute"></a> [dynamodb\_ttl\_attribute](#input\_dynamodb\_ttl\_attribute) | n/a | `string` | `"TimeToExist"` | no |
| <a name="input_dynamodb_ttl_enable"></a> [dynamodb\_ttl\_enable](#input\_dynamodb\_ttl\_enable) | - DynamoDB - | `bool` | `false` | no |
| <a name="input_github_access_token"></a> [github\_access\_token](#input\_github\_access\_token) | Optional GitHub access token. Only required if using GitHub repo. | `string` | `null` | no |
| <a name="input_lookup_ssm_github_access_token"></a> [lookup\_ssm\_github\_access\_token](#input\_lookup\_ssm\_github\_access\_token) | *IMPORTANT!*<br>Conditional data fetch of SSM parameter store for GitHub access token.<br>To ensure security of this token, you must manually add it via the AWS console<br>before using. | `bool` | `false` | no |
| <a name="input_s3_enable_force_destroy"></a> [s3\_enable\_force\_destroy](#input\_s3\_enable\_force\_destroy) | n/a | `string` | `"true"` | no |
| <a name="input_sample_admin_cognito_user_group_description"></a> [sample\_admin\_cognito\_user\_group\_description](#input\_sample\_admin\_cognito\_user\_group\_description) | n/a | `string` | `"Admin Group"` | no |
| <a name="input_sample_admin_cognito_user_group_name"></a> [sample\_admin\_cognito\_user\_group\_name](#input\_sample\_admin\_cognito\_user\_group\_name) | n/a | `string` | `"Admin"` | no |
| <a name="input_sample_admin_cognito_users"></a> [sample\_admin\_cognito\_users](#input\_sample\_admin\_cognito\_users) | Admin Users | `map(any)` | `{}` | no |
| <a name="input_sample_amplify_app_domain_name"></a> [sample\_amplify\_app\_domain\_name](#input\_sample\_amplify\_app\_domain\_name) | The name of your domain. Ex. naruto.ninja | `string` | `"example.com"` | no |
| <a name="input_sample_amplify_app_framework"></a> [sample\_amplify\_app\_framework](#input\_sample\_amplify\_app\_framework) | n/a | `string` | `"React"` | no |
| <a name="input_sample_app_storage_bucket_name"></a> [sample\_app\_storage\_bucket\_name](#input\_sample\_app\_storage\_bucket\_name) | Bucket used for Amplify app storage. Max 27 characters | `string` | `"sample-app-storage-bucket"` | no |
| <a name="input_sample_appsync_graphql_api_name"></a> [sample\_appsync\_graphql\_api\_name](#input\_sample\_appsync\_graphql\_api\_name) | AppSync - GraphQL | `string` | `"sample-graphql-api"` | no |
| <a name="input_sample_auto_branch_creation_patterns"></a> [sample\_auto\_branch\_creation\_patterns](#input\_sample\_auto\_branch\_creation\_patterns) | Automated branch creation glob patterns for the Amplify app. Ex. feat*/* | `list(any)` | <pre>[<br>  "main",<br>  "dev"<br>]</pre> | no |
| <a name="input_sample_codecommit_repo_default_branch"></a> [sample\_codecommit\_repo\_default\_branch](#input\_sample\_codecommit\_repo\_default\_branch) | n/a | `string` | `"main"` | no |
| <a name="input_sample_codecommit_repo_description"></a> [sample\_codecommit\_repo\_description](#input\_sample\_codecommit\_repo\_description) | n/a | `string` | `"The CodeCommit repo created in the sample deployment"` | no |
| <a name="input_sample_codecommit_repo_name"></a> [sample\_codecommit\_repo\_name](#input\_sample\_codecommit\_repo\_name) | n/a | `string` | `"sample_codecommit_repo"` | no |
| <a name="input_sample_create_codecommit_repo"></a> [sample\_create\_codecommit\_repo](#input\_sample\_create\_codecommit\_repo) | CodeCommit | `bool` | `false` | no |
| <a name="input_sample_email_verification_message"></a> [sample\_email\_verification\_message](#input\_sample\_email\_verification\_message) | The Cognito email verification message | `string` | `"\nThank you for registering with the Sample App. This is your email confirmation.\nVerification Code: {####}\n\n"` | no |
| <a name="input_sample_email_verification_subject"></a> [sample\_email\_verification\_subject](#input\_sample\_email\_verification\_subject) | The Cognito email verification subject | `string` | `"Sample App Verification"` | no |
| <a name="input_sample_enable_amplify_app_pr_preview"></a> [sample\_enable\_amplify\_app\_pr\_preview](#input\_sample\_enable\_amplify\_app\_pr\_preview) | Enables pull request previews for the autocreated branch | `bool` | `false` | no |
| <a name="input_sample_enable_auto_branch_creation"></a> [sample\_enable\_auto\_branch\_creation](#input\_sample\_enable\_auto\_branch\_creation) | Enables automated branch creation for the Amplify app | `bool` | `true` | no |
| <a name="input_sample_enable_auto_branch_deletion"></a> [sample\_enable\_auto\_branch\_deletion](#input\_sample\_enable\_auto\_branch\_deletion) | Automatically disconnects a branch in the Amplify Console when you delete a branch from your Git repository | `bool` | `true` | no |
| <a name="input_sample_enable_auto_build"></a> [sample\_enable\_auto\_build](#input\_sample\_enable\_auto\_build) | Enables auto-building of autocreated branches for the Amplify App. | `bool` | `true` | no |
| <a name="input_sample_enable_gitlab_mirroring"></a> [sample\_enable\_gitlab\_mirroring](#input\_sample\_enable\_gitlab\_mirroring) | Enables GitLab mirroring to the option AWS CodeCommit repo. | `bool` | `false` | no |
| <a name="input_sample_enable_performance_mode"></a> [sample\_enable\_performance\_mode](#input\_sample\_enable\_performance\_mode) | Enables performance mode for the branch. This keeps cache at Edge Locations for up to 10min after changes | `bool` | `false` | no |
| <a name="input_sample_existing_repo_url"></a> [sample\_existing\_repo\_url](#input\_sample\_existing\_repo\_url) | URL for the existing repo | `string` | `null` | no |
| <a name="input_sample_framework"></a> [sample\_framework](#input\_sample\_framework) | Framework for the autocreated branch | `string` | `"React"` | no |
| <a name="input_sample_gitlab_mirroring_iam_user_name"></a> [sample\_gitlab\_mirroring\_iam\_user\_name](#input\_sample\_gitlab\_mirroring\_iam\_user\_name) | The IAM Username for the GitLab Mirroring IAM User. | `string` | `"sample_gitlab_mirroring"` | no |
| <a name="input_sample_gitlab_mirroring_policy_name"></a> [sample\_gitlab\_mirroring\_policy\_name](#input\_sample\_gitlab\_mirroring\_policy\_name) | The name of the IAM policy attached to the GitLab Mirroring IAM User | `string` | `"sample_gitlab_mirroring_policy"` | no |
| <a name="input_sample_identity_pool_allow_classic_flow"></a> [sample\_identity\_pool\_allow\_classic\_flow](#input\_sample\_identity\_pool\_allow\_classic\_flow) | n/a | `bool` | `false` | no |
| <a name="input_sample_identity_pool_allow_unauthenticated_identites"></a> [sample\_identity\_pool\_allow\_unauthenticated\_identites](#input\_sample\_identity\_pool\_allow\_unauthenticated\_identites) | n/a | `bool` | `false` | no |
| <a name="input_sample_identity_pool_name"></a> [sample\_identity\_pool\_name](#input\_sample\_identity\_pool\_name) | The name of the Cognito Identity Pool created | `string` | `"sample_identity_pool"` | no |
| <a name="input_sample_input_bucket_create_nuke_everything_lifecycle_config"></a> [sample\_input\_bucket\_create\_nuke\_everything\_lifecycle\_config](#input\_sample\_input\_bucket\_create\_nuke\_everything\_lifecycle\_config) | Conditional create of the lifecycle config to remove all objects from the bucket | `bool` | `true` | no |
| <a name="input_sample_input_bucket_days_until_objects_expiration"></a> [sample\_input\_bucket\_days\_until\_objects\_expiration](#input\_sample\_input\_bucket\_days\_until\_objects\_expiration) | The number of days until objects in the bucket are deleted | `number` | `1` | no |
| <a name="input_sample_input_bucket_enable_cors"></a> [sample\_input\_bucket\_enable\_cors](#input\_sample\_input\_bucket\_enable\_cors) | Contiditional enabling of CORS | `bool` | `true` | no |
| <a name="input_sample_input_bucket_name"></a> [sample\_input\_bucket\_name](#input\_sample\_input\_bucket\_name) | Name of the S3 bucket for transcribe job source. Max 27 characters | `string` | `"sample-input-bucket"` | no |
| <a name="input_sample_invite_email_message"></a> [sample\_invite\_email\_message](#input\_sample\_invite\_email\_message) | n/a | `string` | `"You have been invited to the Sample App App! Your username is \"{username}\" and\ntemporary password is \"{####}\". Please reach out to an admin if you have issues signing in.\n\n"` | no |
| <a name="input_sample_invite_email_subject"></a> [sample\_invite\_email\_subject](#input\_sample\_invite\_email\_subject) | n/a | `string` | `"You've been CHOSEN.\n"` | no |
| <a name="input_sample_invite_sms_message"></a> [sample\_invite\_sms\_message](#input\_sample\_invite\_sms\_message) | n/a | `string` | `"You have been invited to the Sample App! Your username is \"{username}\" and\ntemporary password is \"{####}\".\n\n"` | no |
| <a name="input_sample_landing_bucket_create_nuke_everything_lifecycle_config"></a> [sample\_landing\_bucket\_create\_nuke\_everything\_lifecycle\_config](#input\_sample\_landing\_bucket\_create\_nuke\_everything\_lifecycle\_config) | Conditional create of the lifecycle config to remove all objects from the bucket | `bool` | `true` | no |
| <a name="input_sample_landing_bucket_days_until_objects_expiration"></a> [sample\_landing\_bucket\_days\_until\_objects\_expiration](#input\_sample\_landing\_bucket\_days\_until\_objects\_expiration) | The number of days until objects in the bucket are deleted | `number` | `1` | no |
| <a name="input_sample_landing_bucket_enable_cors"></a> [sample\_landing\_bucket\_enable\_cors](#input\_sample\_landing\_bucket\_enable\_cors) | Contiditional enabling of CORS | `bool` | `true` | no |
| <a name="input_sample_landing_bucket_name"></a> [sample\_landing\_bucket\_name](#input\_sample\_landing\_bucket\_name) | Name of the S3 bucket for audio file upload. Max 27 characters | `string` | `"sample-landing-bucket"` | no |
| <a name="input_sample_number_schemas"></a> [sample\_number\_schemas](#input\_sample\_number\_schemas) | A container with the number schema attributes of a user pool. Maximum of 50 attributes | `list(any)` | `[]` | no |
| <a name="input_sample_output_billing_mode"></a> [sample\_output\_billing\_mode](#input\_sample\_output\_billing\_mode) | n/a | `string` | `"PROVISIONED"` | no |
| <a name="input_sample_output_bucket_create_nuke_everything_lifecycle_config"></a> [sample\_output\_bucket\_create\_nuke\_everything\_lifecycle\_config](#input\_sample\_output\_bucket\_create\_nuke\_everything\_lifecycle\_config) | Conditional create of the lifecycle config to remove all objects from the bucket | `bool` | `true` | no |
| <a name="input_sample_output_bucket_days_until_objects_expiration"></a> [sample\_output\_bucket\_days\_until\_objects\_expiration](#input\_sample\_output\_bucket\_days\_until\_objects\_expiration) | The number of days until objects in the bucket are deleted | `number` | `1` | no |
| <a name="input_sample_output_bucket_enable_cors"></a> [sample\_output\_bucket\_enable\_cors](#input\_sample\_output\_bucket\_enable\_cors) | Contiditional enabling of CORS | `bool` | `true` | no |
| <a name="input_sample_output_bucket_name"></a> [sample\_output\_bucket\_name](#input\_sample\_output\_bucket\_name) | Output bucket for completed transcriptions. Max 27 characters | `string` | `"sample-output-bucket"` | no |
| <a name="input_sample_output_read_capacity"></a> [sample\_output\_read\_capacity](#input\_sample\_output\_read\_capacity) | n/a | `number` | `20` | no |
| <a name="input_sample_output_write_capacity"></a> [sample\_output\_write\_capacity](#input\_sample\_output\_write\_capacity) | n/a | `number` | `20` | no |
| <a name="input_sample_password_policy_min_length"></a> [sample\_password\_policy\_min\_length](#input\_sample\_password\_policy\_min\_length) | The minimum nmber of characters for Cognito user passwords | `number` | `8` | no |
| <a name="input_sample_password_policy_require_lowercase"></a> [sample\_password\_policy\_require\_lowercase](#input\_sample\_password\_policy\_require\_lowercase) | Whether or not the Cognito user password must have at least 1 lowercase character | `bool` | `true` | no |
| <a name="input_sample_password_policy_require_numbers"></a> [sample\_password\_policy\_require\_numbers](#input\_sample\_password\_policy\_require\_numbers) | Whether or not the Cognito user password must have at least 1 number | `bool` | `true` | no |
| <a name="input_sample_password_policy_require_symbols"></a> [sample\_password\_policy\_require\_symbols](#input\_sample\_password\_policy\_require\_symbols) | Whether or not the Cognito user password must have at least 1 special character | `bool` | `true` | no |
| <a name="input_sample_password_policy_require_uppercase"></a> [sample\_password\_policy\_require\_uppercase](#input\_sample\_password\_policy\_require\_uppercase) | Whether or not the Cognito user password must have at least 1 uppercase character | `bool` | `true` | no |
| <a name="input_sample_password_policy_temp_password_validity_days"></a> [sample\_password\_policy\_temp\_password\_validity\_days](#input\_sample\_password\_policy\_temp\_password\_validity\_days) | The number of days a temp password is valid. If user does not sign-in during this time, will need to be reset by an admin | `number` | `7` | no |
| <a name="input_sample_s3_block_public_access"></a> [sample\_s3\_block\_public\_access](#input\_sample\_s3\_block\_public\_access) | Conditional enabling of the block public access S3 feature | `bool` | `true` | no |
| <a name="input_sample_s3_block_public_acls"></a> [sample\_s3\_block\_public\_acls](#input\_sample\_s3\_block\_public\_acls) | Conditional enabling of the block public ACLs S3 feature | `bool` | `true` | no |
| <a name="input_sample_s3_block_public_policy"></a> [sample\_s3\_block\_public\_policy](#input\_sample\_s3\_block\_public\_policy) | Conditional enabling of the block public policy S3 feature | `bool` | `true` | no |
| <a name="input_sample_s3_enable_bucket_policy"></a> [sample\_s3\_enable\_bucket\_policy](#input\_sample\_s3\_enable\_bucket\_policy) | Conditional creation of S3 bucket policies | `bool` | `true` | no |
| <a name="input_sample_schemas"></a> [sample\_schemas](#input\_sample\_schemas) | A container with the schema attributes of a user pool. Maximum of 50 attributes | `list(any)` | `[]` | no |
| <a name="input_sample_sfn_state_generate_uuid_name"></a> [sample\_sfn\_state\_generate\_uuid\_name](#input\_sample\_sfn\_state\_generate\_uuid\_name) | Name for SFN State that generates a UUID that is appended to the object key of the file copied from sample\_landing to sample\_input bucket | `string` | `"GenerateUUID"` | no |
| <a name="input_sample_sfn_state_generate_uuid_next_step"></a> [sample\_sfn\_state\_generate\_uuid\_next\_step](#input\_sample\_sfn\_state\_generate\_uuid\_next\_step) | } | `string` | `"GetSampleInputFile"` | no |
| <a name="input_sample_sfn_state_get_sample_input_file_name"></a> [sample\_sfn\_state\_get\_sample\_input\_file\_name](#input\_sample\_sfn\_state\_get\_sample\_input\_file\_name) | Generates a UUID that is appended to the object key of the file copied from sample\_landing to sample\_input bucket | `string` | `"GetSampleInputFile"` | no |
| <a name="input_sample_sfn_state_machine_name"></a> [sample\_sfn\_state\_machine\_name](#input\_sample\_sfn\_state\_machine\_name) | Name of the state machine used to orchestrate pipeline | `string` | `"sample-state-machine"` | no |
| <a name="input_sample_standard_cognito_user_group_description"></a> [sample\_standard\_cognito\_user\_group\_description](#input\_sample\_standard\_cognito\_user\_group\_description) | n/a | `string` | `"Standard Group"` | no |
| <a name="input_sample_standard_cognito_user_group_name"></a> [sample\_standard\_cognito\_user\_group\_name](#input\_sample\_standard\_cognito\_user\_group\_name) | n/a | `string` | `"Standard"` | no |
| <a name="input_sample_standard_cognito_users"></a> [sample\_standard\_cognito\_users](#input\_sample\_standard\_cognito\_users) | Standard Users | `map(any)` | `{}` | no |
| <a name="input_sample_string_schemas"></a> [sample\_string\_schemas](#input\_sample\_string\_schemas) | A container with the string schema attributes of a user pool. Maximum of 50 attributes | `list(any)` | <pre>[<br>  {<br>    "attribute_data_type": "String",<br>    "developer_only_attribute": false,<br>    "mutable": false,<br>    "name": "email",<br>    "required": true,<br>    "string_attribute_constraints": {<br>      "max_length": 25,<br>      "min_length": 7<br>    }<br>  },<br>  {<br>    "attribute_data_type": "String",<br>    "developer_only_attribute": false,<br>    "mutable": true,<br>    "name": "given_name",<br>    "required": true,<br>    "string_attribute_constraints": {<br>      "max_length": 25,<br>      "min_length": 1<br>    }<br>  },<br>  {<br>    "attribute_data_type": "String",<br>    "developer_only_attribute": false,<br>    "mutable": true,<br>    "name": "family_name",<br>    "required": true,<br>    "string_attribute_constraints": {<br>      "max_length": 25,<br>      "min_length": 1<br>    }<br>  },<br>  {<br>    "attribute_data_type": "String",<br>    "developer_only_attribute": false,<br>    "mutable": true,<br>    "name": "IAC_PROVIDER",<br>    "required": false,<br>    "string_attribute_constraints": {<br>      "max_length": 10,<br>      "min_length": 1<br>    }<br>  }<br>]</pre> | no |
| <a name="input_sample_user_pool_client_name"></a> [sample\_user\_pool\_client\_name](#input\_sample\_user\_pool\_client\_name) | The name of the Cognito User Pool Client created | `string` | `"sample_user_pool_client"` | no |
| <a name="input_sample_user_pool_name"></a> [sample\_user\_pool\_name](#input\_sample\_user\_pool\_name) | The name of the Cognito User Pool created | `string` | `"sample_user_pool"` | no |
| <a name="input_ssm_github_access_token_name"></a> [ssm\_github\_access\_token\_name](#input\_ssm\_github\_access\_token\_name) | The name (key) of the SSM parameter store of your GitHub access token | `string` | `null` | no |
| <a name="input_tags"></a> [tags](#input\_tags) | Tags to apply to resources | `map(any)` | <pre>{<br>  "IAC_PROVIDER": "Terraform"<br>}</pre> | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_aws_current_region"></a> [aws\_current\_region](#output\_aws\_current\_region) | AWS Current Region |
| <a name="output_sample_app_storage_bucket_arn"></a> [sample\_app\_storage\_bucket\_arn](#output\_sample\_app\_storage\_bucket\_arn) | The ARN of the S3 app storage bucket |
| <a name="output_sample_app_storage_bucket_id"></a> [sample\_app\_storage\_bucket\_id](#output\_sample\_app\_storage\_bucket\_id) | The name of the S3 app storage bucket |
| <a name="output_sample_appsync_graphql_api_id"></a> [sample\_appsync\_graphql\_api\_id](#output\_sample\_appsync\_graphql\_api\_id) | n/a |
| <a name="output_sample_appsync_graphql_api_region"></a> [sample\_appsync\_graphql\_api\_region](#output\_sample\_appsync\_graphql\_api\_region) | AppSync (GraphQL) |
| <a name="output_sample_appsync_graphql_api_uris"></a> [sample\_appsync\_graphql\_api\_uris](#output\_sample\_appsync\_graphql\_api\_uris) | n/a |
| <a name="output_sample_dynamodb_output_table_name"></a> [sample\_dynamodb\_output\_table\_name](#output\_sample\_dynamodb\_output\_table\_name) | DynamoDB |
| <a name="output_sample_identity_pool_id"></a> [sample\_identity\_pool\_id](#output\_sample\_identity\_pool\_id) | n/a |
| <a name="output_sample_input_bucket_arn"></a> [sample\_input\_bucket\_arn](#output\_sample\_input\_bucket\_arn) | The Arn of the S3 input bucket |
| <a name="output_sample_input_bucket_id"></a> [sample\_input\_bucket\_id](#output\_sample\_input\_bucket\_id) | The name of the S3 input bucket |
| <a name="output_sample_output_bucket_arn"></a> [sample\_output\_bucket\_arn](#output\_sample\_output\_bucket\_arn) | The Arn of the S3 input bucket |
| <a name="output_sample_output_bucket_id"></a> [sample\_output\_bucket\_id](#output\_sample\_output\_bucket\_id) | The name of the S3 output bucket |
| <a name="output_sample_step_function_arn"></a> [sample\_step\_function\_arn](#output\_sample\_step\_function\_arn) | Step Function |
| <a name="output_sample_user_pool_client_id"></a> [sample\_user\_pool\_client\_id](#output\_sample\_user\_pool\_client\_id) | n/a |
| <a name="output_sample_user_pool_id"></a> [sample\_user\_pool\_id](#output\_sample\_user\_pool\_id) | n/a |
| <a name="output_sample_user_pool_region"></a> [sample\_user\_pool\_region](#output\_sample\_user\_pool\_region) | Cognito |
