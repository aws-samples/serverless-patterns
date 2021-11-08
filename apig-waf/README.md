
# Amazon API Gateway integration with WAF

This pattern in CDK offers a example to generate an Amazon API Gateway with a greedy proxy ("{proxy+}") and "ANY" method from the specified path, meaning it will accept by default any method and any path. The VPC Lambda function provided in JavaScript only returns the path.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-waf-cdk

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
      cd apig-waf/src
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


  *  Locate WAFAPIGatewayApi.ApiUrl from output printed by cdk, this is the api endpoint to be invoked
    In a browser

    ```https://<api_id>.execute-api.<region>.amazonaws.com/prod```

    You should see: ```Success path: "/"```



## Cleanup
 
1. From the command line, use the following in the source folder
    ```bash
    npx cdk destroy --app 'ts-node .' --all
    ```
2. Confirm the removal and wait for the resource deletion to complete.
