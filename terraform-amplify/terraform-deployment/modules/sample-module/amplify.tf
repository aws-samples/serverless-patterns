# Relevant values:
# - AWS Region
# - Cognito User Pool ID
# - Cognito Web Client ID
# - Cognito Identity Pool ID
# - AppSync GraphQL Region
# - AppSync GraphQL Endpoint ID
# - AppSync GraphQL Authentication Type ('AMAZON_COGNITO_USER_POOLS')
# - Relevant S3 Buckets

resource "aws_amplify_app" "sample_app" {
  count      = var.create_amplify_app ? 1 : 0
  name       = var.app_name
  repository = var.sample_create_codecommit_repo ? aws_codecommit_repository.sample_codecommit_repo[0].clone_url_http : var.sample_existing_repo_url
  # enable_branch_auto_build = true


  enable_auto_branch_creation   = var.sample_enable_auto_branch_creation
  enable_branch_auto_deletion   = var.sample_enable_auto_branch_deletion
  auto_branch_creation_patterns = var.sample_auto_branch_creation_patterns // default is just main
  auto_branch_creation_config {
    enable_auto_build           = var.sample_enable_auto_build
    enable_pull_request_preview = var.sample_enable_amplify_app_pr_preview
    enable_performance_mode     = var.sample_enable_performance_mode
    framework                   = var.sample_framework
  }
  # OPTIONAL - Necessary if not using oauth_token or access_token (used for GitLab and GitHub repos)
  iam_service_role_arn = var.sample_create_codecommit_repo ? aws_iam_role.sample_amplify_codecommit[0].arn : null
  access_token         = var.lookup_ssm_github_access_token ? data.aws_ssm_parameter.ssm_github_access_token[0].value : var.github_access_token // optional, only needed if using github repo

  build_spec = file("${path.root}/../amplify.yml")
  # Redirects for Single Page Web Apps (SPA)
  # https://docs.aws.amazon.com/amplify/latest/userguide/redirects.html#redirects-for-single-page-web-apps-spa
  custom_rule {
    source = "</^[^.]+$|\\.(?!(css|gif|ico|jpg|js|png|txt|svg|woff|ttf|map|json)$)([^.]+$)/>"
    status = "200"
    target = "/index.html"
  }

  environment_variables = {
    sample_REGION              = "${data.aws_region.current.id}"
    sample_CODECOMMIT_REPO_ID  = "${var.sample_create_codecommit_repo ? aws_codecommit_repository.sample_codecommit_repo[0].repository_id : null}" //return null if no cc repo is created
    sample_USER_POOL_ID        = "${aws_cognito_user_pool.sample_user_pool.id}"
    sample_IDENTITY_POOL_ID    = "${aws_cognito_identity_pool.sample_identity_pool.id}"
    sample_APP_CLIENT_ID       = "${aws_cognito_user_pool_client.sample_user_pool_client.id}"
    sample_GRAPHQL_ENDPOINT    = "${aws_appsync_graphql_api.sample_appsync_graphql_api.uris.GRAPHQL}"
    sample_GRAPHQL_API_ID      = "${aws_appsync_graphql_api.sample_appsync_graphql_api.id}"
    sample_LANDING_BUCKET_NAME = "${aws_s3_bucket.sample_landing_bucket.id}"
  }
}

# resource "aws_amplify_domain_association" "example" {
#   count       = var.create_sample_amplify_domain_association ? 1 : 0
#   app_id      = aws_amplify_app.sample_app[0].id
#   domain_name = var.sample_amplify_app_domain_name

#   # https://example.com
#   sub_domain {
#     branch_name = aws_amplify_branch.sample_amplify_branch_main[0].branch_name
#     prefix      = ""
#   }

#   # https://www.example.com
#   sub_domain {
#     branch_name = aws_amplify_branch.sample_amplify_branch_main[0].branch_name
#     prefix      = "www"
#   }
#   # https://dev.example.com
#   sub_domain {
#     branch_name = aws_amplify_branch.sample_amplify_branch_dev[0].branch_name
#     prefix      = "dev"
#   }
#   # https://www.dev.example.com
#   sub_domain {
#     branch_name = aws_amplify_branch.sample_amplify_branch_dev[0].branch_name
#     prefix      = "www.dev"
#   }
# }
