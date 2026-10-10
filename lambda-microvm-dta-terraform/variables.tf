variable "region" {
  description = "AWS region where Lambda MicroVMs is available."
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name prefix for created resources."
  type        = string
  default     = "microvm-dta-sample"
}

variable "artifact_bucket_name" {
  description = "Optional explicit S3 bucket name. Empty lets AWS generate one."
  type        = string
  default     = ""
}

variable "enable_github_oidc_role" {
  description = "Create the optional GitHub Actions OIDC CI role (carrying the lambda:* MicroVM control-plane policy). Off by default; the core pattern only needs the build/execution roles + artifact bucket, so `terraform apply` works with no required inputs."
  type        = bool
  default     = false
}

variable "github_org" {
  description = "GitHub org or user that owns the repository (only used when enable_github_oidc_role = true)."
  type        = string
  default     = "YOUR_GITHUB_ORG"
}

variable "github_repo" {
  description = "GitHub repository name (for OIDC trust)."
  type        = string
  default     = "aws-lambda-microvm-dta-sample"
}

variable "github_branch" {
  description = "Branch allowed to assume the CI role via OIDC."
  type        = string
  default     = "main"
}

variable "create_github_oidc_provider" {
  description = "Create the GitHub Actions OIDC provider. Set false if it already exists in the account."
  type        = bool
  default     = true
}

variable "enable_vpc_egress" {
  description = "Create a VPC + restricted egress for the production-oriented network profile."
  type        = bool
  default     = false
}

variable "vpc_cidr" {
  description = "CIDR for the egress VPC (only used when enable_vpc_egress = true)."
  type        = string
  default     = "10.20.0.0/16"
}

variable "enable_vpc_flow_logs" {
  description = "Enable VPC Flow Logs to CloudWatch for network-flow evidence (requires enable_vpc_egress)."
  type        = bool
  default     = false
}

variable "tags" {
  description = "Extra tags applied to all resources."
  type        = map(string)
  default     = {}
}
