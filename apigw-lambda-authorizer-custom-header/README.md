# Amazon API Gateway API using Lambda Token Authorizer and Mapping Template to add custom header

The SAM template deploys an Amazon API Gateway API endpoint that uses a Lambda Token Authorizer for access control as well as added logic in the Authorizer function to enrich the request with additional data. 

This aproach can be used to inject data that downstream legacy systems expect and that is dependent on data that is available to authorizer.

* If the request to the endpoint does not include a 'authorizationToken' header, the Lambda Authorizer will not be invoked and API Gateway will return a 401 Forbidden. 
* If the request to the endpoint includes a 'authorizationToken' header, the Lambda Authorizer will be invoked and its response will depend on the value of the 'authorizationToken' header. 
* If the value of 'authorizationToken' header is 'unauthorized', API Gateway will return a 401 Unauthorized error. 
* If the value of 'authorizationToken' header is 'deny', API Gateway will return a 403 error. 
* Only if the value of 'authorizationToken' header is 'allow', API Gateway will successfully call the HTTP backend and return a 200. 
* For any other case, API Gateway will return a 403 error.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-lambda-authorizer-custom-header](https://serverlessland.com/patterns/apigw-lambda-authorizer-custom-header)

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
2. Change directory to the pattern directory:
    ```
    TODO cd apigw-lambda-authorizer
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy -g
    ```
1. During the prompts:
    * Enter a stack name
    * Select the desired AWS Region
    * Allow SAM to create roles with the required permissions if needed.

    Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

The stack will output the **api endpoint**. Use *curl* to make a HTTP request to the API Gateway that includes a header with the authorization token to test the Resource Lambda Token Authorizer.
   
```
curl -i https://12345abcde.execute-api.{region}.amazonaws.com/Prod -H "authorizationToken: allow"
```

will successfully return a 200 HTTP code and the request from API Gateway to the HTTP endpoint in the response body. You should see a header named `enrichmentHeader` with a string provided from the Lambda Token Authorizer `This data comes from Lambda Authorizer`


## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----

## Author bio
Shaun Guo
https://www.linkedin.com/in/shaun-guo/
Senior Technical Account Manager
