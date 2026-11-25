variable "region" {
  description = "AWS Region to deploy into. Lambda MicroVMs must be available in it."
  type        = string
  default     = "us-east-1"
}

variable "name_prefix" {
  description = "Prefix for all resource names."
  type        = string
  default     = "gha-microvm-runner"
}

# The webhook function's preconditions (main.tf) enforce the required
# GitHub variables for each runner_scope.

variable "runner_scope" {
  description = "Register runners at 'repo' or 'org' level."
  type        = string
  default     = "repo"

  validation {
    condition     = contains(["repo", "org"], var.runner_scope)
    error_message = "runner_scope must be 'repo' or 'org'."
  }
}

variable "github_owner" {
  description = "GitHub user or org that owns the repo. Required when runner_scope = \"repo\"."
  type        = string
  default     = ""
}

variable "github_repo" {
  description = "GitHub repo name. Required when runner_scope = \"repo\"."
  type        = string
  default     = ""
}

variable "github_org" {
  description = "GitHub org. Required when runner_scope = \"org\"; leave empty for repo scope."
  type        = string
  default     = ""
}

variable "runner_labels" {
  description = "Labels the runner registers with. Jobs target them with runs-on and must request all of them."
  type        = list(string)
  default     = ["self-hosted", "lambda"]
}

variable "microvm_max_duration_seconds" {
  description = <<-EOT
    Maximum MicroVM lifespan in seconds, passed to RunMicrovm
    (maximumDurationInSeconds, 1-28800). The platform kills the VM at this
    limit, so a job that runs longer is cut off. Default 900 (15 minutes).
  EOT
  type        = number
  default     = 900
}
