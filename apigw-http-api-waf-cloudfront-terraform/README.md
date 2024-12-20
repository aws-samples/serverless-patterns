# Protect Amazon API Gateway with Amazon CloudFront and AWS WAF

This pattern demonstrates how to increase the security posture of Amazon API Gateway against common attack patterns such as SQL injection, cross-site scripting (XSS) or DDOS attacks

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-http-api-waf-cloudfront-terraform

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Python 3.12](https://www.python.org/downloads/release/python-3120/) installed
* [Terraform](https://developer.hashicorp.com/terraform/install) (Terraform) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd apigw-http-api-waf-cloudfront-terraform
    ```
3. Install the Terraform dependencies

    ```bash
    terraform init -input=false
    ```

4. Preview the resources that will be deployed with Terraform in your AWS account

    ```bash
    terraform plan \
    -var "region=#your-region#" \ #region where resources will be deployed (default is us-east-1)
    -var "cloudfront_domain_name=#your-cloudfront-domain-name#" \ #domain name for your CloudFront distribution (optional)
    -var "cloudfront_certificate_arn=arn:aws:acm:#region#:#accountid#:certificate/#certificateid#" \ #cloudfront certificate arn (required only if cloudfront_domain_name is set)
    -var "domain_name=#your-api-domain-name#" \ #domain name for your API Gateway (optional)
    -var "certificate_arn=arn:aws:acm:#region#:#accountid#:certificate/#certificateid#" \ #certificate arn (required only if domain_name is set)
    -var "zone_id=#zoneid#" #hosted zone id (required only if domain_name is set)
    ```

5. Provision resources with Terraform in your AWS account

    ```bash
    terraform apply -auto-approve \
    -var "region=#your-region#" \ #region where resources will be deployed (default is us-east-1)
    -var "cloudfront_domain_name=#your-cloudfront-domain-name#" \ #domain name for your CloudFront distribution (optional)
    -var "cloudfront_certificate_arn=arn:aws:acm:#region#:#accountid#:certificate/#certificateid#" \ #cloudfront certificate arn (required only if cloudfront_domain_name is set)
    -var "domain_name=#your-api-domain-name#" \ #domain name for your API Gateway (optional)
    -var "certificate_arn=arn:aws:acm:#region#:#accountid#:certificate/#certificateid#" \ #certificate arn (required only if domain_name is set)
    -var "zone_id=#zoneid#" #hosted zone id (required only if domain_name is set)
    ```

## How it works

Requests sent to a HTTP API Gateway are protected by an Amazon CloudFront distribution and AWS WAF's web ACL.

The below diagram illustrates the solution.

![Solution diagram](/apigw-http-api-waf-cloudfront-terraform/img/solution_overview.png)

When a request is sent to an Amazon CloudFront distribution (Step 1), it is evaluated by a AWS WAF's web ACL (Step 2).

Then a unique key is retrieved from Secrets Manager by an Amazon CloudFront's Lambda@Edge function (Step 3) and is added as a header (x-origin-verify) in the request (Step 4) before being passed to the API Gateway.

Once the HTTP API Gateway receives the request (Step 5), a Lambda authorizer checks the header (Step 6 & Step 7) and confirm its validity (checks if this is the same value as the one in Secrets Manager).

Finally, the request is sent to a backend Lambda function (Step 8) and a response is returned back to the requester.

If the request is sent directly to the HTTP API Gateway, the request fails as the request is not coming from the Amazon CloudFront distribution (the request doesn't include the header x-origin-verify with the unique key from Secrets Manager).

Note: The unique key in Secrets Manager is rotated periodically as shown on the above diagram (Step A, B and C)

## Testing

After deployment, enter the URL of the CloudFront distribution in your navigator: this should return a successful response ("Hello from Lambda!").

If you enter the URL of the API Gateway: this should return a failure response.

## Cleanup
 
In order to delete the solution, the follow the steps below.


1. Destroy the resources via Terraform

```bash
terraform destroy -auto-approve \
-var "region=#your-region#" \ #region where resources will be deployed (default is us-east-1)
-var "cloudfront_domain_name=#your-cloudfront-domain-name#" \ #domain name for your CloudFront distribution (optional)
-var "cloudfront_certificate_arn=arn:aws:acm:#region#:#accountid#:certificate/#certificateid#" \ #cloudfront certificate arn (required only if cloudfront_domain_name is set)
-var "domain_name=#your-api-domain-name#" \ #domain name for your API Gateway (optional)
-var "certificate_arn=arn:aws:acm:#region#:#accountid#:certificate/#certificateid#" \ #certificate arn (required only if domain_name is set)
-var "zone_id=#zoneid#" #hosted zone id (required only if domain_name is set)
```

2. Re-run terraform destroy if you the Lambda@Edge function failed to be deleted

(Note: When the Lambda@Edge function fails to be deleted, you may see the following error message: "Lambda was unable to delete arn:aws:lambda:#region#:#account-id#:function:http-edge-lambda:#version# because it is a replicated function. Please see our documentation for Deleting Lambda@Edge Functions and Replicas")

```bash
terraform destroy -auto-approve \
-var "region=#your-region#" \ #region where resources will be deployed (default is us-east-1)
-var "cloudfront_domain_name=#your-cloudfront-domain-name#" \ #domain name for your CloudFront distribution (optional)
-var "cloudfront_certificate_arn=arn:aws:acm:#region#:#accountid#:certificate/#certificateid#" \ #cloudfront certificate arn (required only if cloudfront_domain_name is set)
-var "domain_name=#your-api-domain-name#" \ #domain name for your API Gateway (optional)
-var "certificate_arn=arn:aws:acm:#region#:#accountid#:certificate/#certificateid#" \ #certificate arn (required only if domain_name is set)
-var "zone_id=#zoneid#" #hosted zone id (required only if domain_name is set)
```

3. Delete the secret

(Note: The secret will not be immediately deleted after Step 1. It will only be scheduled for deletion. To fully delete the secret, you will need to use the below command)

```bash
aws secretsmanager delete-secret --secret-id waf-http-api --force-delete-without-recovery
```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
