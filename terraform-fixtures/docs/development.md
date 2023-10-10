# Development of Terraform Serverless Patterns

This document describes some steps required to verify quality of the Terraform Serverless Patterns located in this repository.

## Running pre-commit hooks manually

Since this repository contains not just Terraform configurations, `pre-commit` hooks should be executed manually before commit (without centralized configurations).

1. Clone `pre-commit-terraform` repository locally:
```bash
git clone https://github.com/antonbabenko/pre-commit-terraform ~/Sites/pre-commit-terraform
cd ~/Sites/pre-commit-terraform
```

1. Run hooks in the current directory where Terraform configurations are located (path starts with `terraform-`):
    ```bash
    run_pre_commit_hooks_serverless_patterns () {
      PRE_COMMIT_HOOKS_DIR=~/Sites/pre-commit-terraform/hooks
      $PRE_COMMIT_HOOKS_DIR/terraform_fmt.sh .
      $PRE_COMMIT_HOOKS_DIR/terraform_validate.sh .
      $PRE_COMMIT_HOOKS_DIR/terraform_docs.sh --args=--lockfile=false .
      $PRE_COMMIT_HOOKS_DIR/terraform_tflint.sh --args=--only=terraform_deprecated_interpolation --args=--only=terraform_deprecated_index --args=--only=terraform_unused_declarations --args=--only=terraform_comment_syntax --args=--only=terraform_documented_outputs --args=--only=terraform_documented_variables --args=--only=terraform_typed_variables --args=--only=terraform_module_pinned_source --args=--only=terraform_naming_convention --args=--only=terraform_required_version --args=--only=terraform_required_providers --args=--only=terraform_standard_module_structure --args=--only=terraform_workspace_remote .
    }
   
    run_pre_commit_hooks_serverless_patterns
    ```

1. Verify and commit changes.
