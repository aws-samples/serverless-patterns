# ASP.NET Core Web API as AWS Lambda Function

This project uses **ASP.NET Core Web API** project template to run .NET Core Web API througha Lambda Function.

## Convert an ASP.NET Core Web API to Lambda Function
1. Open **Visual Studio**, select **File > New > Project**
2. Select **ASP.NET Core Web API** project template
3. Add the [Amazon.Lambda.AspNetCoreServer.Hosting](https://www.nuget.org/packages/Amazon.Lambda.AspNetCoreServer.Hosting/) NuGet package to your project.
4. Add a call to `AddAWSLambdaHosting` in your application when the services are being defined for the application.
    ```
    // Add AWS Lambda support.
    builder.Services.AddAWSLambdaHosting(LambdaEventSource.RestApi);
    ```
5. Add `app.UsePathBase("/prod");` in your `Program.cs` file. This is because, API Gateway appends stage name in the default FQDN.
6. Finally, use executing assembly name as Function Handler. In this project, use `dotnet-core-web-api` as Function Handler.

## References
- [Introducing the .NET 6 runtime for AWS Lambda](https://aws.amazon.com/blogs/compute/introducing-the-net-6-runtime-for-aws-lambda/)