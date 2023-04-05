# Application Load balancer with AWS Lambda as target with Pulumi

This pattern demonstrates how to create an Application Load Balancer with AWS Lambda as target. Implemented in Pulumi.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/alb-lambda-pulumi-js

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [Pulumi](https://www.pulumi.com/docs/get-started/install/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd alb-lambda-pulumi-js
    ```
1. Run below command to install required dependancies:
    ```
    npm install
    ```
1. Set the region that you want to deploy the load balancer and Lambda function to:
    ```
    pulumi config set aws:region {region}
    ```
1. From the command line, run:
    ```
    pulumi up
    ```

## Testing

1. In the stack output, you can see `url`. To access this using the Pulumi CLI you can run `curl $(pulumi stack output url)`.

** Please note: Application Load Balancer's default settings for health check are 5 consecutive health check successes with 35 seconds interval. So, it will take couple of minutes for the target to be healthy.

## Cleanup
 
1. To delete the stack, run:
    ```bash
    pulumi destroy
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0