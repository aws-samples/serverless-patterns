# Multi-tenant API with Amazon API Gateway and AWS Lambda Tenant Isolation

![architecture](architecture/architecture.png)

This pattern implements a serverless multi-tenant counter API using Amazon API Gateway, AWS Lambda and Amazon DynamoDB. It deploys two parallel endpoints, one without tenant isolation and one with full per-tenant isolation, to demonstrate how shared state leads to cross-tenant data leakage in multi-tenant applications.

When a request hits the standard endpoint, the Lambda function increments a single shared counter in DynamoDB, exposing activity across all tenants. The isolated endpoint requires a tenant ID header, which maps to a dedicated Lambda execution environment and a tenant-specific DynamoDB row. Each tenant gets an independent counter, ensuring complete data separation. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-ddb-tenant-isolation-terraform

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.cxom/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-ddb-tenant-isolation-terraform
    ```
1. From the command line, initialize terraform to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply -auto-approve
    ```
1. During the prompts
    #var.aws_region
    - Enter a value: {enter the region for deployment}

    #var.prefix
    - Enter a value: {enter any prefix to associate with resources}

1. Note the outputs from the Terraform deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

Use [curl](https://curl.se/) to send a HTTP GET request to the API.

1. Make a GET request to the Standard API endpoint using the following cURL command:
```
curl -H "x-tenant-id: TENANT_ID" "STANDARD_API_ENDPOINT"
```
Note: Replace the `TENANT_ID` with a unique Tenant ID of your choice and `STANDARD_API_ENDPOINT` with the generated `standard_multi_tenant_api_endpoint_url` from Terraform (refer to the Terraform Outputs section)

For ex,
```
curl -H "x-tenant-id: Tenant-1" "https://1234abcde.execute-api.us-east-1.amazonaws.com/dev/standard"
```

The response would be,
```
{"counter": 1, "tenant_id": "Tenant-1", "isolation_enabled": false, "message": "This function does NOT provide tenant isolation and every tenant reads and writes the same DynamoDB row. Incremented counter is shared across all the tenants"}
```

Test this for another Tenant ID. For ex,
```
curl -H "x-tenant-id: Tenant-2" "https://1234abcde.execute-api.us-east-1.amazonaws.com/dev/standard"
```

The response would be,
```
{"counter": 2, "tenant_id": "Tenant-2", "isolation_enabled": false, "message": "This function does NOT provide tenant isolation and every tenant reads and writes the same DynamoDB row. Incremented counter is shared across all the tenants"}
```

1. Now make a GET request to the Isolated API endpoint using the following cURL command:
```
curl -H "x-tenant-id: TENANT_ID" "ISOLATED_API_ENDPOINT"
```
Note: Replace the `TENANT_ID` with a unique Tenant ID of your choice and `ISOLATED_API_ENDPOINT` with the generated `isolated_tenant_api_endpoint_url` from Terraform (refer to the Terraform Outputs section)

For ex,
```
curl -H "x-tenant-id: Tenant-1" "https://1234abcde.execute-api.us-east-1.amazonaws.com/dev/isolated"
```

The response would be,
```
{"counter": 1, "tenant_id": "Tenant-1", "isolation_enabled": true, "message": "Counter incremented for tenant Tenant-1"}
```

Test this for another Tenant ID. For ex,
```
curl -H "x-tenant-id: Tenant-2" "https://1234abcde.execute-api.us-east-1.amazonaws.com/dev/isolated"
```

The response would be,
```
{"counter": 2, "tenant_id": "Tenant-2", "isolation_enabled": true, "message": "Counter incremented for tenant Tenant-2"}
```

## Cleanup

1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-ddb-tenant-isolation-terraform
    ```

1. Delete all created resources
    ```
    terraform destroy -auto-approve
    ```
    
1. During the prompts:
    ```
    Enter all details as entered during creation.
    ```

1. Confirm all created resources has been deleted
    ```
    terraform show
    ```
----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0