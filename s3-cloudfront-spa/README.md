# S3 Hosted Website Served by a CloudFront Distribution restricted by Cloudfront Origin Access Control (OAC)

This repo contains serverless patterns showing how to setup a S3 website hosting bucket that is served by a CloudFront distribution that also obfuscates the CloudFront Distribution domain via Cloudfront Origin Access Control (OAC).

![Demo Project Solution Architecture Diagram](diagram.PNG)

- Learn more about these patterns at https://serverlessland.com/patterns.
- To learn more about submitting a pattern, read the [publishing guidelines page](https://github.com/aws-samples/serverless-patterns/blob/main/PUBLISHING.md).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform Install](https://www.terraform.io/)

## Deployment Instructions
1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd s3-cloudfront-spa
    ```
3. Initilize terraform
    ```
    Run terraform init
    ```
4. Create terrform plan
    ```
    Run terraform plan
    ```
5. Create AWS resources
    ```
    Run terraform apply
    ```
    During the prompts:
    * Enter yes
    
6. Copy your front end assests

## Testing
    "Go to your hosting Amazon S3 bucket ",
    "Upload your front end content or Copy index.html from "s3-cloudfront-spa" pattern "src" folder for testing",
    "Go to AWS Console",
    "Go to AWS Cloudfront",
    "Go to Distributions",
    "Select your distribution domain and browse it. e.g ***********.cloudfront.net/index.html"
    
### Removing the resources

1. To destory deployed resources
    ```
    Run terraform destroy
    ```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.
----

