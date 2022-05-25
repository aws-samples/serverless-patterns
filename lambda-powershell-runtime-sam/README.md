# AWS Lambda Custom Runtime for PowerShell

Use this pattern to build a custom PowerShell runtime for Lambda along with example Lambda function.

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
    cd lambda-powershell-runtime-sam
    ```

To build the custom runtime, AWS SAM uses a Makefile. This downloads the specified version of [PowerShell](https://github.com/PowerShell/PowerShell/releases/). Makefiles are not natively supported in Windows. When using Windows, you can use either [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/about) or [Docker Desktop](https://docs.docker.com/get-docker/).

From the command line, use AWS SAM with one of the *"Build"* options, A or B depending on your operating system and tools.

*A) Build using Linux or WSL*

Build the custom runtime, Lambda layer, and function packages using native Linux or WSL.
```
sam build --parallel
```
*B) Build using Docker*

You can build the custom runtime, Lambda layer, and function packages using Docker. This uses a linux-based Lambda-like Docker container to build the packages. Use this option for Windows without WSL or as an isolated Mac/Linux build environment.

```
sam build --parallel --use-container
````
Once the build process is complete, you can use AWS SAM to test the function locally. 
```
sam local invoke
```
This runs the Lambda function locally using a Lambda-like environment and returns the function response which is the result of `Get-AWSRegion`.

 From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
```
sam deploy --guided
````
During the prompts:

    * Enter a stack name, for example `aws-lambda-powershell-runtime`.
    * Enter the desired AWS Region.
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Accept the remaining default values.

Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file `samconfig.toml`, you can use `sam deploy` in future to use these defaults.

Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

You invoke a PowerShell function that uses the custom runtime which returns the version of PowerShell.

## Testing

Use the Cloudformation Output `PowerShellFunction` from the `sam deploy` command to test your Lambda function.

From a command prompt invoke the function. Amend the `--function-name` and `--region` values for your function. This should return `"StatusCode": 200` for a successful invoke.

````
aws lambda invoke --function-name "aws-lambda-powershell-runtime-Function-6W3bn1znmW8G" --region us-east-1 invoke-result 
````

View the function result `Hello from PowerShell version 7.2.4 on Lambda` which is outputted to `invoke-result`.

````
cat invoke-result
````

You can invoke the Lambda function using the AWS Tools for PowerShell and capture the response in a variable. The response is available in the `Payload` property of the `$Response` object, which can be read using the .NET `StreamReader` class.
````
$Response = Invoke-LMFunction -FunctionName aws-lambda-powershell-runtime-PowerShellFunction-HHdKLkXxnkUn -LogType Tail
[System.IO.StreamReader]::new($Response.Payload).ReadToEnd()
````
This outputs the same result as previously of `Hello from PowerShell version 7.2.4 on Lambda`.

## Cleanup
 
1. Delete the stack, Enter `Y` to confirm deleting the stack and folder.
    ```
    sam delete
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0