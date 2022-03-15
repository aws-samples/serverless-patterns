# Amazon Route 53 Latency policy

This pattern deploys an Amazon Route 53 Latency policy route front of Amazon API Gateway.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/route53-latency](https://serverlessland.com/patterns/route53-latency)

Important: 
With Amazon Route 53, you don’t have to pay any upfront fees or commit to the number of queries the service answers for your domain. - please see the [AWS Pricing page](https://aws.amazon.com/route53/pricing/) for details.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## How it works

If your application is hosted in multiple AWS Regions, you can improve performance for your users by serving their requests from the AWS Region that provides the lowest latency


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd route53-latency
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided --parameter-overrides Route53HostedZoneId={Your_Route53HostedZoneId} Route53DomainName={Your_Route53DomainName} ApiGermanyHostedZoneId={Your_ApiGermanyHostedZoneId} ApiGermanyDomainName={Your_ApiGermanyDomainName} ApiGermanyEndpoint={Your_ApiGermanyEndpoint} ApiIrelandHostedZoneId={Your_ApiIrelandHostedZoneId} ApiIrelandDomainName={Your_ApiIrelandDomainName} ApiIrelandEndpoint={Your_ApiIrelandEndpoint}
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Pass all the required parameters
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.


## Testing

The health check is the key for the routing policies because Route53 will move to the best next latency endpoint only when the health check status is unhealthy and to do so for example the Amazon API Gateway should retun 500 error status.

## Cleanup

1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----

## Additional resources

- [Latency routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency)

---

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
