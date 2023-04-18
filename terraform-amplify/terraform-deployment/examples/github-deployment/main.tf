// This is a template file for a advanced deployment.
// Modify the parameters below with actual values
module "sample-qs" {
  // location of the module - can be local or git repo
  source = "./modules/sample-module"

  # - Amplify App -
  # Connect Amplify to GitHub
  sample_existing_repo_url       = "https://github.com/your-repo-url"
  lookup_ssm_github_access_token = true                                 // set to true if the resource exists in your AWS Account
  ssm_github_access_token_name   = "Enter-Your-SSM-Parameter-Store-Key" // name of the paramater in SSM

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
