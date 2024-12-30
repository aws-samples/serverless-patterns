using System.Runtime.InteropServices;
using Amazon.CDK;
using Amazon.CDK.AWS.Lambda;

namespace AlbEcsBedrockAgentsCdkDotnet.Common;

internal static class LambdaFunctionsCdkUtils
{
    /// <summary>
    /// Gets the bundling options for Lambda functions
    /// </summary>
    /// <returns><see cref="BundlingOptions"/></returns>
    internal static BundlingOptions GetBuildingOptions()
    {
        // Build options for Lambda functions
        return new BundlingOptions()
        {
            Image = Runtime.DOTNET_8.BundlingImage,
            User = "root",
            OutputType = BundlingOutput.ARCHIVED,
            Command = [
                "/bin/sh",
                "-c",
                "dotnet tool install -g Amazon.Lambda.Tools && " +
                "dotnet build && " +
                "dotnet lambda package " +
                "--function-architecture " + (RuntimeInformation.ProcessArchitecture == System.Runtime.InteropServices.Architecture.X64 ? "x86_64" : "arm64") + " " +
                "--output-package /asset-output/function.zip"
            ],
        };
    }
}