variable "http_api_description" {
  type = string
  default = "WAF HTTP API"
}

variable "http_api_name" {
  type = string
  default = "waf-http-api"
}

variable "http_api_stage" {
  type = string
  default = "$default"
}

variable "function_name" {
  type = string
  default = "http-api-lambda"
}

variable "auth_function_name" {
  type = string
  default = "http-auth-lambda"
}

variable "edge_function_name" {
  type = string
  default = "http-edge-lambda"
}

variable "secret_rotation_function_name" {
  type = string
  default = "http-secret-rotation-lambda"
}

variable "secret_rotation_lambda_memory" {
  type = number
  default = 1024
}

variable "function_runtime" {
  type = string
  default = "python3.12"
}

variable "min_ttl" {
  type = number
  default = 0
}

variable "default_ttl" {
  type = number
  default = 3600
}

variable "max_ttl" {
  type = number
  default = 86400
}

variable "region" {
  type = string
  default = "us-east-1"
}

variable "waf_webacl_name" {
  type = string
  default = "http_api_webacl"
}

variable "waf_rule_name" {
  type = string
  default = "http_api_rule"
}

variable "cloudfront_domain_name" {
  type = string
  default = ""
}

variable "domain_name" {
  type = string
  default = ""
}

variable "cloudfront_certificate_arn" {
  type = string
  default = ""
}

variable "certificate_arn" {
  type = string
  default = ""
}

variable "zone_id" {
  type = string
  default = ""
}

variable "cloudfront_api_secret_name" {
  type = string
  default = "waf-http-api"
}

variable "unique_key_length" {
  type = string
  default = "32"
}

variable "throttling_burst_limit" {
  type = number
  default = 1000
}

variable "throttling_rate_limit" {
  type = number
  default = 1000
}