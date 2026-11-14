# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
function Private:Set-LambdaContext
{
    <#
    .SYNOPSIS
    Captures the content of the provided Lambda Context variable.

    .DESCRIPTION
    Captures the content of the provided Lambda Context variable.
    #>
    If ($env:POWERSHELL_RUNTIME_VERBOSE -eq 'TRUE') {$VerbosePreference = "continue"}
    Write-Verbose "[RUNTIME-Set-LambdaContext]Start: Set-LambdaContext"

    # Importing .NET class from .cs file to support the script property "RemainingTime" and method "getRemainingTimeInMillis".
    # This is taken from the Lambda .Net runtime LambdaContext code: https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.Core/ILambdaContext.cs
    Write-Verbose "[RUNTIME-Set-LambdaContext]Importing .NET class from .cs file to support script properties and method"
    Add-Type -TypeDefinition ([System.IO.File]::ReadAllText('/opt/PowerShellLambdaContext.cs'))

    Write-Verbose "[RUNTIME-Set-LambdaContext]Creating LambdaContext"
    $private:LambdaContext = [Amazon.Lambda.PowerShell.Internal.LambdaContext]::new(
        $env:AWS_LAMBDA_FUNCTION_NAME,
        $env:AWS_LAMBDA_FUNCTION_VERSION,
        $env:AWS_LAMBDA_RUNTIME_INVOKE_FUNCTION_ARN,
        [int]$env:AWS_LAMBDA_FUNCTION_MEMORY_SIZE,
        $env:AWS_LAMBDA_RUNTIME_AWS_REQUEST_ID,
        $env:AWS_LAMBDA_LOG_GROUP_NAME,
        $env:AWS_LAMBDA_LOG_STREAM_NAME,
        $env:AWS_LAMBDA_RUNTIME_COGNITO_IDENTITY,
        $env:AWS_LAMBDA_RUNTIME_CLIENT_CONTEXT,
        [double]$env:AWS_LAMBDA_RUNTIME_DEADLINE_MS
    )
    Write-Verbose "[RUNTIME-Set-LambdaContext]return LambdaContext: $($private:LambdaContext)"
    return $private:LambdaContext
}