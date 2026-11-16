# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
function private:Send-FunctionHandlerResponse
{
    <#
        .SYNOPSIS
            POST function response back to Runtime API

        .DESCRIPTION
            POST function response back to Runtime API

        .Notes
            
    #>
    [CmdletBinding()]
    param
    (
        $private:InvocationResponse
    )
    If ($env:POWERSHELL_RUNTIME_VERBOSE -eq 'TRUE') {$VerbosePreference = "continue"}
    Write-Verbose "[RUNTIME-Send-FunctionHandlerResponse]Start: Send-FunctionHandlerResponse"

    Write-Verbose "[RUNTIME-Send-FunctionHandlerResponse]Create POST request to Runtime API"
    $private:responseUri = "http://$env:AWS_LAMBDA_RUNTIME_API/2018-06-01/runtime/invocation/$env:AWS_LAMBDA_RUNTIME_AWS_REQUEST_ID/response"
    $private:responseRequest = [System.Net.WebRequest]::Create($private:responseUri)
    $private:responseRequest.Headers.Add("User-Agent", "aws-lambda-powershell/" + $env:POWERSHELL_VERSION)
    $private:responseRequest.Method = 'POST'

    if (-not([String]::IsNullOrWhiteSpace($private:InvocationResponse))) {
        Write-Verbose "[RUNTIME-Send-FunctionHandlerResponse]Sending POST request to Runtime API"
        $private:responseByteArray = [System.Text.Encoding]::UTF8.GetBytes($private:InvocationResponse)
        $private:responseStream = $private:responseRequest.GetRequestStream()
        $private:responseStream.Write($private:responseByteArray, 0, $private:responseByteArray.Length)
    }

    $null = $private:responseRequest.GetResponse()
    if ($private:responseStream) {$private:responseStream.Dispose() }
}