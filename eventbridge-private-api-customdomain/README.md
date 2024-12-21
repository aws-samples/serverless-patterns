# Invoke Private REST API gateway custom domain from EventBridge schedule

The SAM template deploys a EventBridge schedule that invokes a Private REST API gateway custom domain using Eventbridge connection, API destinations, Amazon VPC Lattice and AWS PrivateLink. The SAM template contains all the required resources with IAM permission to invoke the private endpoint.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-private-api-customdomain

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Private REST API gateway custom domain](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-tutorial.html)
* [Public Route 53 Hosted zone for your domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/AboutHZWorkingWith.html)


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd eventbridge-private-api-customdomain
    ```

3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
5. During the prompts:

    * Enter **stack name**.
    * Enter desired **AWS Region**.
    * Enter **Private Custom Domain Name** (e.g. private.mydomain.com) for the Domainname parameter.
    * Enter **PrivateAPIInvokeURL**  (e.g. https://private.mydomain.com/<apigw-resource-path>) which is complete API invocation url.
    * Enter **VPC Id** for the VPCId parameter to create VPC latticre resource gateway in VPC. Recommendation: use same VPC as of API Gateway VPC endpoint attached to private api gateway. 
    * Enter **Subnet Id's** for the SubnetIds parameter (comma seperated e.g. subnet1,subnet2) to create resource gateway. Recommendation: use same subnets as of API gateway VPC endpoint. 
    * Enter **SecurityGroup Id's** for the SecurityGroup parameter which allows inbound access on port 443 from your VPC's CIDR range.
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

7. **Imp Note** : Once the stack is deployed, Create a 'A' record in your Public Route53 hosted zone for the 'Domainname' with below target:
        
        a) Target type - alias
        b) Alis - VPC Endpoint
        c) Endpoint - select the VPC Endpoint which is attached to your Private API. Eg: vpce-1123444556666-avx567.execute-api.<AWS-region>.vpce.amazonaws.com


## Testing

1. Eventbridge schedule will invoke the Private API every 5 minutes as configured in the scheduled expression.

2. Check the Private API stage or integration logs to verify invocations, invocations from eventbridge will contain a custom added header 'invokedby: eventbridgeinvoke' & 'User-Agent:Amazon/EventBridge/ApiDestinations'.


### Example output in API Gateway logs:

```bash
Endpoint request body after transformations: {"resource":"/lambda-resource","path":"/lambda-resource","httpMethod":"GET","headers":{"Accept-Encoding":"gzip, x-gzip, deflate, br","Content-Type":"application/json; charset=utf-8","Host":"HOSTNAME","invokedby":"eventbridgeinvoke","User-Agent":"Amazon/EventBridge/ApiDestinations","x-amzn-vpc-id":"vpc-1111222c123456c","x-amzn-vpce-config":"1","x-amzn-vpce-id":"vpce-112233c3344bb4",},"
```


## Cleanup
 
Delete the stack
```bash
    sam delete
```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
