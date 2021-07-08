
# Amazon API Gateway Private API with AWS VPC Lambda proxy integration

This pattern in CDK offers a example to generate an Amazon API Gateway Private API endpoint with a greedy proxy ("{proxy+}") and "ANY" method from the specified path, meaning it will accept by default any method and any path. The VPC Lambda function provided in JavaScript only returns the path.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/private-apigw-lambda-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory its source code folder:
    ```bash
      cd private-apigw-lambda-cdk/src
    ```
3. From the command line, use npm to install the development dependencies:
    ```bash
      npm install
    ```
4. To deploy from the command line use the following:
    ```bash
      npx cdk bootstrap aws://accountnumber/region
      npx cdk deploy --app 'ts-node .' --all
    ```

## Testing

* Since the API Gateway is private it can't be accessed from internet. 
  * The api can be invoked from an EC2 Instance VPC
    1. This example creates an EC2 instance in the VPC 
    2. Log into AWS Account and navigte to EC2 
    3. Select the EC2 instance created by this example
    4. Hit the "Connect" button on top right 
    5. On the connect page navigate to "Session Manager" Tab and hit "Connect" Button
    6. On the web shell run curl the output for PrivateAPIGatewayApi.ApiUrl
    ```curl https://<api_id>-<vpcid>.execute-api.<region>.amazonaws.com/prod```
    7. You should see: ```Success path: "/"```.
  * The Private API Gateway API can also be accessed from a VPN Connection or AWS Direct Connect


## Cleanup
 
1. From the command line, use the following in the source folder
    ```bash
    npx cdk destroy --app 'ts-node .' --all
    ```
2. Confirm the removal and wait for the resource deletion to complete.
