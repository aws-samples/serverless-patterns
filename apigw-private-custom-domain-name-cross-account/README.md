# Invoking a Private Custom Domain Name cross-account

## Architecture Overview

This architecture enables the invocation of a Private Custom Domain Name deployed for a Private API Gateway cross-account. The solution leverages [Amazon Private API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html), [Execute-API VPC Endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html), and the Private Custom Domain N [Private Custom Domain name](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains.html). 

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/apigw-private-custom-domain-name-cross-account).

You can update the template to add AWS resources through the same deployment process that updates your application code.

Important: This application uses various AWS Services and there are costs associated with these services after the Free Tier Usage - please see the [AWS Pricing Page](https://aws.amazon.com/pricing/) for more details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

### Requirements

- Two [AWS accounts](https://signin.aws.amazon.com/signup?request_type=register). IAM users or roles with sufficient permissions to make the necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed and configured.
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)  (AWS SAM) installed.
- Setup .aws/credentials [named profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) namely **accountA** and **accountB** so you can run CLI and AWS SAM commands against them.
- An [Amazon Execute-API VPC Endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) needed to invoke your private custom domain name.
- A [Public ACM Certificate issued](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html) so that API Gateway can prove its identity to clients establishing secure HTTPS connections

### How it works

This pattern utilizes two AWS Accounts and their respective templates. 

1. **Account A** : Hosts the Private API Gateway and the Private Custom Domain Name:
    -  **Amazon API Gateway (Private)**: Receives requests from the Account B via the Execute VPC Endpoint deployed in Account B
    - **Custom Domain Name** which is hit by the client in Account B to invoke the API Gateway
    - The **Custom Domain Name** is then shared with Account B via AWS Resource Access Manager (AWS RAM)

2. **Account B** : Hosts the Private Hosted Zone, the Execute API VPC Endpoint and creates the Domain Name Access association. A client in the VPC where the VPC Endpoint is deployed can then send requests to the Private API Gateway in Account A using the Custom Domain Name


### Deployment Instructions

**Note**: Please make sure to follow the below steps in order to make sure the deployment is successful. 

1.  Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```bash
    cd serverless-patterns/apigw-private-custom-domain-name-cross-account
    ```

#### AccountA

1. In account A, where you would like to create **Private API Gateway**, along with its Private Custom Domain Name, navigate to the `accountA` directory from the main directory and deploy using *(if you are in a different directory, then run `cd ..` before entering the below command)*:
    ```bash
    cd accountA
    
    sam deploy --guided --profile accountA

2. During the prompts:
    -  Enter **stack name** and desired **AWS Region**.
    -  Enter **the AccountB VPC Endpoint**. 
    -  Enter **the AWS ACM Certificate ARN**.
    -  Enter the **Custom Domain Name** which is covered by the aforementioned certificate.
    - Enter the **AccountB ID**. This will be used to share the Custom Domain Name resource with.
    -  Allow SAM CLI to create IAM roles with the required permissions.
3. Note the outputs from the SAM deployment process. This contains both the `Custom Domain Name` and `Custom Domain Name ARN`, which will be used as inputs for the second account's stack deployment.

#### Accept the Resource Share Invitation
Upon deploying the first template, you can get the invitation ARN from the AWS CLI by running the following command:
    ```
    aws ram get-resource-share-invitations --profile <target-account-profile>
    ```

Copy the invitation ARN, and paste it in the following command:
    ```
    aws ram accept-resource-share-invitation \
    --resource-share-invitation-arn arn:aws:ram:region:account-id:resource-share-invitation/invitation-id \
    --profile <target-account-profile>
    ```

#### AccountB
1. In account B, where you would like to create the **Custom Domain Name Access Association** and the **Private Hosted Zone**, navigate to the `accountB` directory from the main directory and deploy using *(if you are in a different directory, then run `cd ..` before entering the below command)*:
    ```bash
    cd accountB
    
    sam deploy --guided --profile accountB
    ```
2. During the prompts:
    -  Enter **stack name** and desired **AWS Region**.
    -  Enter the **VPC ID** where the Hosted Zone will be created
    -  Enter the **VPC Endpoint DNS Name**. It will be used to create the Alias record in the Private Hosted Zone
    -  Enter the **Custom Domain Name** created in the first template
    -  Enter the **Custom Domain Name ARN** created in the first template
    -  Enter the **VPC Endpoint Hosted Zone ID**
    -  Allow SAM CLI to create IAM roles with the required permissions.


## Cleanup
To avoid incurring future charges, it's important to delete the resources in the correcct order. Follow these steps to clean up the resources created by the four templates *(Make sure to navigate to the directory containing the template before running the below commands)*:

1. Delete Account A template 
    ```bash
    sam delete --stack-name STACK_NAME --profile PROFILE_NAME
    ```
2. Delete Account B template 
    ```bash
    sam delete --stack-name STACK_NAME_ACCOUNT_B --profile accountB
    ```