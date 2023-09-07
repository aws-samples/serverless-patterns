/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- provider.tf ---

terraform {
    required_version = ">= 1.4.0"

    required_providers {
        aws = {
        source  = "hashicorp/aws"
        version = ">= 4.60.0"
        }
    }
}

provider "aws" {
    region = var.region

    default_tags {
        tags = {
            environment: var.region
            purpose: var.purpose
        }
    }
}
