// This is a template file for a advanced deployment.
// Modify the parameters below with actual values
module "sample-qs" {
  // location of the module - can be local or git repo
  source = "./modules/sample-module"

  # - Amplify App -
  create_amplify_app         = true
  sample_create_codecommit_repo  = true
  sample_enable_gitlab_mirroring = false

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
