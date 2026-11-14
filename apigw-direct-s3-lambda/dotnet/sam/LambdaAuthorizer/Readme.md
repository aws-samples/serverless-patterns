# AWS Lambda Authorizer Function Project

This starter project consists of:
* AuthorizerFunction.cs - This funciton is intended to contain your custom authorization logic. The example code illustrates how to enforce that all incoming HTTP requests pass an HTTP header ```Authorization```  with the value of ```mytesttoken```. Harcoding the token value is for demonstration purposes only. In a real world scenario, the Authorization token would be a JSON Web Toke (JWT) or a custom token you'd use to validate against your application's authorization logic.
* aws-lambda-tools-defaults.json - default argument settings for use with Visual Studio and command line deployment tools for AWS

You may also have a test project depending on the options selected.

The generated function handler is a simple method accepting a string argument that returns the uppercase equivalent of the input string. Replace the body of this method, and parameters, to suit your needs. 

## Here are some steps to follow from Visual Studio:

To deploy your function to AWS Lambda, right click the project in Solution Explorer and select *Publish to AWS Lambda*.

To view your deployed function open its Function View window by double-clicking the function name shown beneath the AWS Lambda node in the AWS Explorer tree.

To perform testing against your deployed function use the Test Invoke tab in the opened Function View window.

To configure event sources for your deployed function, for example to have your function invoked when an object is created in an Amazon S3 bucket, use the Event Sources tab in the opened Function View window.

To update the runtime configuration of your deployed function use the Configuration tab in the opened Function View window.

To view execution logs of invocations of your function use the Logs tab in the opened Function View window.

## Here are some steps to follow to get started from the command line:

Once you have edited your template and code you can deploy your application using the [Amazon.Lambda.Tools Global Tool](https://github.com/aws/aws-extensions-for-dotnet-cli#aws-lambda-amazonlambdatools) from the command line.

Install Amazon.Lambda.Tools Global Tools if not already installed.
```
    dotnet tool install -g Amazon.Lambda.Tools
```

If already installed check if new version is available.
```
    dotnet tool update -g Amazon.Lambda.Tools
```

Execute unit tests
```
    cd "lambda-authorizer/test/lambda-authorizer.Tests"
    dotnet test
```

Deploy function to AWS Lambda
```
    cd "lambda-authorizer/src/lambda-authorizer"
    dotnet lambda deploy-function
```
