# S3 Hosted Website Served by a CloudFront Distribution restricted by Cloudfront Origin Access Control (OAC)

This repo contains serverless patterns showing how to setup a S3 website hosting bucket that is served by a CloudFront distribution that also obfuscates the CloudFront Distribution domain via Cloudfront Origin Access Control (OAC).

![Demo Project Solution Architecture Diagram](diagram.PNG)

- Learn more about these patterns at https://serverlessland.com/patterns.
- To learn more about submitting a pattern, read the [publishing guidelines page](https://github.com/aws-samples/serverless-patterns/blob/main/PUBLISHING.md).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS Account
* AWS CLI already configured with Administrator permission
* Terraform
* Clone this repo!

## Deployment Instructions

1. Go to s3-cloudfront-spa and copy template.tf to your project
2. Setup terraform backend and define your state file S3 bucket by replacing your bucket name with "my-projects-terraform-state" in template.tf
3. Run terraform init
4. Run terraform plan
5. Run terraform apply

### Removing the resources

1. Run terraform apply -destroy

```
git clone https://github.com/aws-samples/serverless-patterns/s3-cloudfront-spa
```

Each subdirectory contains additional installation and usage instructions. 

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
----

