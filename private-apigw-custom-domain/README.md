# Private Amazon API Gateway with Private Custom Domain Name

The SAM template deploys a Private Amazon API Gateway with a Private Custom Domain Name mapped to deployed stage. This template also create a Route53 CNAME record in a Private Hosted Zone to map the Private Custom Domain Name (e.g. private.mydomain.com) to the Target VPC Endpoint DNS Name. (e.g. vpce-abcdefgh123456789-abcd1234.execute-api.us-east-1.vpce.amazonaws.com).

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/private-apigw-custom-domain)

## Requirements

* An [AWS account](https://signin.aws.amazon.com/signup?request_type=register) with an IAM user or role that has sufficient permissions to make the necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed.
* An [execute-api VPC Endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html).
* A Route 53 [Private Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html).
* An SSL/TLS certificate in [AWS Certificate Manager](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-specify-certificate-for-custom-domain-name.html#how-to-specify-certificate-for-custom-domain-name-setup).

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```bash
    cd serverless-patterns/private-apigw-custom-domain
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```bash
    sam deploy --guided
    ```
4. During the prompts:
    - Enter **stack name** and desired **AWS Region**.
    - Enter **DNS Name** of the **execute-api** VPC endpoint for the VpcEndpointDNSName parameter. (e.g. vpce-abcdefgh123456789-abcd1234.execute-api.us-east-1.vpce.amazonaws.com)
    - Enter **Private Custom Domain Name** (e.g. private.mydomain.com) for the CustomDomainName parameter.
    - Enter **ACM Certificate ARN** from the same region as Private Amazon API Gateway for the CertificateArn parameter. The certificate must cover the Private Custom Domain name entered in the previous step.
    - Enter **Private Hosted Zone ID** that has the domain name you would like to use (e.g. mydomain.com) for the parameter PrivateHostedZoneId. 
    - Allow SAM to create roles with the required permissions if needed.

    Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. This contain the curl command to test the Private Custom Domain Name.

## Testing

The stack will output the **Private Custom Domain Name**. You can use `curl` to send a HTTP request to the Private Custom Domain endpoint to test the correct mapping to your API.
   
```bash
curl https://{PrivateCustomDomainName}/
```

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
