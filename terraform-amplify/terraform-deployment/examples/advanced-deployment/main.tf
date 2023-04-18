// This is a template file for a advanced deployment.
// Modify the parameters below with actual values
module "sample-qs" {
  // location of the module - can be local or git repo
  source = "./modules/sample-module"


  # - S3 -
  # These are created by default - Adding for context
  sample_input_bucket_name       = "sample-input"       // default value
  sample_output_bucket_name      = "sample-output"      // default value
  sample_app_storage_bucket_name = "sample-app-storage" // default value

  # - Amplify -
  # If this is set to true, you must either specific a URL for 'sample_existing_repo_url'
  # or set the variable 'sample_create_codecommit_repo to true. Not doing so will return
  # a BadRequestException error
  create_amplify_app                = true // default value
  create_sample_amplify_branch_main = true // default value
  create_sample_amplify_branch_dev  = true // default value - set this to false to bypass creation of this additional branch

  lookup_ssm_github_access_token = false                                // default value. Set to true if relevant
  ssm_github_access_token_name   = "Enter-Your-SSM-Parameter-Store-Key" // name of parameter store item (recommended method if using GitHub repo)
  github_access_token            = "abcdefg123456"                      // Optional - Manual value of GitHub Access Token (less secure)

  # - CodeCommit -
  sample_codecommit_repo_name = "sample_codecommit_repo" // default value

  # GitLab Mirroring
  sample_enable_gitlab_mirroring = true // Enables GitLab Mirroring

  # - Cognito -
  # Admin Users to create
  sample_admin_cognito_users = {
    NarutoUzumaki : {
      username       = "nuzumaki"
      given_name     = "Naruto"
      family_name    = "Uzumaki"
      email          = "naruto@rasengan.com"
      email_verified = true
    },
    SasukeUchiha : {
      username       = "suchiha"
      given_name     = "Sasuke"
      family_name    = "Uchiha"
      email          = "sasuke@chidori.com"
      email_verified = true
    }
  }
  # Standard Users to create
  sample_standard_cognito_users = {
    DefaultStandardUser : {
      username       = "default"
      given_name     = "Default"
      family_name    = "User"
      email          = "example@example.com"
      email_verified = false
    }
  }

}
