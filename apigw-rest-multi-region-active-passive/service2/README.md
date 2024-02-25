# Serverless patterns - Multi-Region REST API Failover: Service 2

Service2 consists of a regional rest API with a single root path calling a Lambda function.

This pattern deploys service2 on a primary and secondaty region. It will also setup Route53 public failover records and Route 53 ARC routing controls for you.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd aws-apigw-multi-region/service2
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file on the primary region:
    ```
    sam deploy --guided --config-env primary
    ```
1. During the prompts:
    * **Stack Name:** Enter a stack name.
    * **AWS Region:** Enter the desired AWS Region. This pattern has been tested with both us-east-1 and us-east-2.
    * **PublicHostedZoneId:** You must have a public hosted zone in Route 53 with your domain name (i.e. mydomain.com). Enter the Hosted Zone Id for this hosted zone.
    * **DomainName:** Enter your custom domain name (i.e. service2.mydomain.com).
    * **CertificateArn** You must have a ACM Certificate that covers your Custom Domain namespace (i.e. *.mydomain.com) on the region your are deploying this stack. Enter the ARN for this certificate here. **Make sure you are getting the certificate arn for the right region**.
    * **Route53ArcClusterArn:** Before deploy this stack, you should deploy the Route 53 infrastructure. Add here the Route 53 Cluster Arn created during that deployment.
    * **Service2ControlPlaneArn**: Before deploy this stack, you should deploy the Route 53 infrastructure. Add here the  Route 53 ARC control pane Arn for service 2.
    * **Stage:** Enter the name of the stage within your API Gateway that you would like to map to your custom domain name.
    * **FailoverType:** Accept the defauls and use **PRIMARY** here.
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Allow SAM CLI to create the Service2LambdaRegionalApi Lambda function.
    * **SAM configuration environment** Accept the **primary** default value.

    Once you have run `sam deploy --guided --config-env primary` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy --config-env primary` in future to use these defaults.

1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file on the primary region:
    ```
    sam deploy --guided --config-env secondary
    ```
1. During the prompts:
    * **Stack Name:** Enter a stack name.
    * **AWS Region:** Enter the desired AWS Region. This pattern has been tested with both us-east-1 and us-east-2. **Make sure to use a different region from the prymary one**.
    * **PublicHostedZoneId:** You must have a public hosted zone in Route 53 with your domain name (i.e. mydomain.com). Enter the Hosted Zone Id for this hosted zone.
    * **DomainName:** Enter your custom domain name (i.e. service2.mydomain.com).
    * **CertificateArn** You must have a ACM Certificate that covers your Custom Domain namespace (i.e. *.mydomain.com) on the region your are deploying this stack. Enter the ARN for this certificate here. **Make sure you are getting the certificate arn for the right region**.
    * **Route53ArcClusterArn:** Before deploy this stack, you should deploy the Route 53 infrastructure. Add here the Route 53 Cluster Arn created during that deployment.
    * **Service2ControlPlaneArn**: Before deploy this stack, you should deploy the Route 53 infrastructure. Add here the  Route 53 ARC control pane Arn for service 2.
    * **Stage:** Enter the name of the stage within your API Gateway that you would like to map to your custom domain name.
    * **FailoverType:** Accept the defauls and use **SECONDARY** here.
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Allow SAM CLI to create the Service2LambdaRegionalApi Lambda function.
    * **SAM configuration environment** Accept the **primary** default value.

    Once you have run `sam deploy --guided --config-env secondary` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy --config-env secondary` in future to use these defaults.
    
1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This stack will deploy an Amazon API Gateway Rest Regional API with a Lambda integration. The AWS Lambda function is written in Python3.9. The function returns a small message with the service name and the region it is deployed at. The inline code of the lambda is written in the template itself.

## Testing

Once the stack is deployed, get the API endpoint from the EndpointUrl output parameter.
Paste the URL in a browser, or in Postman, or using the curl command.
Eg: 
```bash
curl https://aabbccddee.execute-api.us-east-1.amazonaws.com/prod
```

You should see a response similar to:
```json
{"service": "service2", "region": "your-selected-region"}
```


Now test that one of your regional services is accessible via your custom fomain.
You can get that URL from the **CustomDomainNameEndpoint** output parameter.
Eg: 
```bash
curl https://service2.mydomain.com
```

You should see a response similar to:
```json
{"service": "service2", "region": "your-primary-region"}
```

You can failover service 2 from the primary to the secondary region using Route53 ARC
> Notes: Service 2 have its own Route 53 ARC control pannel. To manage [routing controls](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html), you need to use its specific control panels. You can check the [route53 stack](./route53/README.md) outputs to see the details for the service 2 control panel.

After 1 or 2 minutes, you should see responses to service 2 custom domain endpoint (i.e https://service2.mydomain.com) being serverd from the secondary region:
```json
{"service": "service2", "region": "your-secondary-region"}
```

## Cleanup
 
1. Delete the stack on the primary region.
    ```bash
    sam delete --config-env primary
    ```
1. Delete the stack on the secondary region.
    ```bash
    sam delete --config-env secondary
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0