# AWS Lambda S3 Function Project

This starter project consists of:
* S3Function.cs - file containing a class with a single function handler method that will be invoked when a file is uploaded to the S3 bucket. The S3 bucket name and object key are passed in the functions ```S3Event evnt``` parameter.


You may also have a test project depending on the options selected.

The generated function handler responds to events on an Amazon S3 bucket. The handler receives the bucket and object key details in an S3Event instance and returns the content type of the object as the function output. Replace the body of this method, and parameters, to suit your needs.

After deploying your function you must configure an Amazon S3 bucket as an event source to trigger your Lambda function.

## Here are some steps to follow from Visual Studio:

To deploy your Serverless application, right click the project in Solution Explorer and select *Publish to AWS Lambda*.

To view your deployed application open the Stack View window by double-clicking the stack name shown beneath the AWS CloudFormation node in the AWS Explorer tree. The Stack View also displays the root URL to your published application.

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
    cd "lambda-file-processor/test/lambda-file-processor.Tests"
    dotnet test
```

Deploy function to AWS Lambda
```
    cd "lambda-file-processor/src/lambda-file-processor"
    dotnet lambda deploy-serverless
```
