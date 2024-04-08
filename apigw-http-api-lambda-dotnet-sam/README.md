# ASP.NET Core Web API Serverless Application with AWS SAM

This project shows how to use AWS SAM for an ASP.NET Core Web API project using a AWS Lambda function exposed through Amazon API Gateway. 


## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [.Net 6.0](https://dotnet.microsoft.com/en-us/download/dotnet/6.0)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-http-api-lambda-dotnet-sam 
    ```
1. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works
- 

==============================================

## Testing
The Cloudformation stack deployment will output your API endpoint URL
```bash
CloudFormation outputs from deployed stack
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Outputs                                                                                                                                                     
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Key                 ApiURL                                                                                                                                  
Description         API endpoint URL for Prod environment                                                                                                   
Value               https://hr029dslcf.execute-api.ap-southeast-2.amazonaws.com/Prod/                                                                       
-------------------------------------------------------------------------------------------------------------------------------------------------------------


Successfully created/updated stack - dotnet-http-api in ap-southeast-2
```

You can use this endpoint to test the HTTP response

```bash
export ApiUrl=https://hr029dslcf.execute-api.ap-southeast-2.amazonaws.com/Prod/                                                            

curl $ApiUrl
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

## Resources

For more .NET templates, view the .NET Lambda Tools Blueprints https://github.com/aws/aws-lambda-dotnet/tree/master/Blueprints
The NuGet package [Amazon.Lambda.AspNetCoreServer](https://www.nuget.org/packages/Amazon.Lambda.AspNetCoreServer) contains a Lambda function that is used to translate requests from API Gateway into the ASP.NET Core framework and then the responses from ASP.NET Core back to API Gateway.

For more information about how the Amazon.Lambda.AspNetCoreServer package works and how to extend its behavior view its [README](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.AspNetCoreServer/README.md) file in GitHub.

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
