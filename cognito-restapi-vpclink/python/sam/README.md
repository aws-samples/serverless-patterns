# API Gateway private REST API with private integration and Cognito authentication

This SAM template implements an Amazon API Gateway private REST API with private integration. It can be used if you have a private API inside a VPC which is currently open to unauthenticated clients and you want to protect it by adding an authentication and authorization layer without having to modify the API itself.

The template creates a private REST API in Amazon API Gateway which sits in front of the original backend API. Requests will go through the API Gateway endpoint and will be authorized using a Cognito authorizer. The integration with the backend resource is done via a VPC link to connect to private resources inside the VPC. The API Gateway API is configured with a greedy proxy ("{proxy+}") which means that everything in the URL path will be passed to the backend without any modification. The API has an "ANY" method to accept all methods such as GET or POST. Finally, the OPTIONS method is configured so that the API can process preflight requests from browsers making cross-origin requests (CORS).

The backend API to be protected is simulated by an ECS Fargate cluster running nginx.

Note: when deploying this pattern, both *CAPABILITY_AUTO_EXPAND* and *CAPABILITY_IAM* are required.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-vpclink-fargate

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.


## Architecture

![Architecture diagram](./images/diagram.png "Architecture diagram")


## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* VPC with at least one private subnet

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd cognito-restapi-vpclink
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy -g --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the VPC ID (i.e. vpc-01a81eec6eexample)
    * Enter the private subnet IDs separated by commas (i.e. subnet-0b58b8b621example,subnet-0f56f9b73example)
    * Enter the allowed CIRDR range (i.e. 10.0.0.0/8)
    * Allow SAM to create roles with the required permissions.

    Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.


## Testing

The stack will output the **Cognito User Pool ID** and **Client ID** required to get an authorization token from Cognito. We will be using the AWS CLI to obtain the token. For a web application running on a browser, you can use a framework such as Amplify to get the identity token or access token and then call the deployed API Gateway API and supply the appropriate token in the Authorization header.

1. Run the following AWS CLI commands from your laptop (substitute the region, user-pool-id and client-id values as appropriate)


```
aws cognito-idp admin-create-user --user-pool-id <USER_POOL_ID> --username testuser --user-attributes Name=email,Value=youremail@yourdomain.com --message-action SUPPRESS --region <REGION>
```

```
aws cognito-idp admin-set-user-password --user-pool-id <USER_POOL_ID> --username testuser --password <PASSWORD> --permanent --region <REGION>
```

```
aws cognito-idp initiate-auth --region <REGION> --auth-flow USER_PASSWORD_AUTH --client-id <CLIENT_ID> --auth-parameters USERNAME=testuser,PASSWORD=<PASSWORD> --query AuthenticationResult.IdToken --output text
```


2. Copy the id token from the output of the last command

3. Launch an EC2 instance in the same VPC.

Since the API is private, you will be able to connect to it only from the VPC or from a network that can reach the VPC. Launch an instance in the same VPC to perform tests.

4. Log in to the EC2 instance in the same VPC and run the following:


```
API_URL=https://fkbexample-vpce-0b7bf1da2dexample.execute-api.us-east-1.amazonaws.com/api  (copy your endpoint from output)
```

```
TOKEN=eyJraWQiOiJJOW9US1Ny... (copy the full token obtained from the cognito-idp command)
```

```
curl -i -H "Authorization: Bearer ${TOKEN}" "${API_URL}/"
```

You should receive a response similar to the one below:


```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

Note that you're connecting to the backend resource via the API Gateway endpoint. If you try to connect directly either to the NLB or ALB endpoint you'll be blocked by security groups. You will also get Unauthorized error messages if you don't provide a valid token.


For more information about Amazon API Gateway private APIs and how to invoke them using different endpoints, please refer to links below.

* How to invoke a private API
https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-api-test-invoke-url.html

* Creating a private API in Amazon API Gateway
https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html


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
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
