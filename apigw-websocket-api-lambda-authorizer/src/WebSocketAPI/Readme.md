# WebSocket API Project

This starter project consists of:
* serverless.template - an AWS CloudFormation Serverless Application Model template file for declaring your Serverless functions and other AWS resources
* Functions.cs - class file containing the 3 separate Lambda function handlers for connecting, disconnecting and sending messages.
* aws-lambda-tools-defaults.json - default argument settings for use with Visual Studio and command line deployment tools for AWS

You may also have a test project depending on the options selected.

The generated project contains a Serverless template which declares 3 Lambda functions to connect, disconnect and send messages for the WebSocket API. 
The template then declares the WebSocket API with API Gateway and a DynamoDB table to manage connection ids for the open WebSocket connections.

An easy way to test the WebSocket after deploying is to use the tool [wscat](https://github.com/websockets/wscat) from NPM. To install the tool from NPM
use the following command:
```
npm install -g wscat
```

Then to test then open multiple console windows and each console run the following command to connect.
```
wscat -c wss://{YOUR-API-ID}.execute-api.{YOUR-REGION}.amazonaws.com/{STAGE}
```
Note: The url to connect to can also be found as the output parameter of the CloudFormation stack.

In one of the windows use the following command to send a message to the WebSocket which will broadcast the message to all other open console windows:
```
$ wscat -c wss://{YOUR-API-ID}.execute-api.{YOUR-REGION}.amazonaws.com/prod
connected (press CTRL+C to quit)
> {"message":"sendmessage", "data":"hello world"}
< hello world
```

In .NET you can access the WebSocket API using the `System.Net.WebSockets.ClientWebSocket` class. Here is a snippet showing how to send a message to the WebSocketAPI.
```csharp
static async Task Main(string[] args)
{
    var cws = new ClientWebSocket();

    var cancelSource = new CancellationTokenSource();
    var connectionUri = new Uri("wss://{YOUR-API-ID}.execute-api.{YOUR-REGION}.amazonaws.com/prod");
    await cws.ConnectAsync(connectionUri, cancelSource.Token);

    ArraySegment<byte> message = new ArraySegment<byte>(UTF8Encoding.UTF8.GetBytes("{\"message\":\"sendmessage\", \"data\":\"Hello from .NET ClientWebSocket\"}"));
    await cws.SendAsync(message, WebSocketMessageType.Text, true, cancelSource.Token);
}
```

For more information about this demo and and API Gateway WebSocket check out the following blog post which had the original version of 
this demo written in Node.js: https://aws.amazon.com/blogs/compute/announcing-websocket-apis-in-amazon-api-gateway/


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
    cd "WebSocketAPI/test/WebSocketAPI.Tests"
    dotnet test
```

Deploy application
```
    cd "WebSocketAPI/src/WebSocketAPI"
    dotnet lambda deploy-serverless
```
