# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
function private:Send-FunctionHandlerError
{
    <#
        .SYNOPSIS
            POST function invocation error back to Runtime API

        .DESCRIPTION
            POST function invocation error back to Runtime API

        .Notes
            
    #>
    [CmdletBinding()]
    param
    (
        [Parameter(Mandatory)] $private:InvocationError
    )
    If ($env:POWERSHELL_RUNTIME_VERBOSE -eq 'TRUE') {$VerbosePreference = "continue"}
    Write-Verbose "[RUNTIME-Send-FunctionHandlerError]Start: Send-FunctionHandlerError"

    Write-Verbose "[RUNTIME-Send-FunctionHandlerError]Create POST request to Runtime Error API"
    $private:responseUri = "http://$env:AWS_LAMBDA_RUNTIME_API/2018-06-01/runtime/invocation/$env:AWS_LAMBDA_RUNTIME_AWS_REQUEST_ID/error"
    $private:responseRequest = [System.Net.WebRequest]::Create($private:responseUri)
    $private:responseRequest.Headers.Add("User-Agent", "aws-lambda-powershell/" + $env:POWERSHELL_VERSION)
    $private:responseRequest.Method = 'POST'

    Write-Host $private:InvocationError

    Write-Verbose "[RUNTIME-Send-FunctionHandlerError]Create response error object"
    $private:responseErrorBody = ConvertTo-Json -Compress -InputObject @{
        errorMessage = $private:InvocationError.Exception.Message
        errorType    = $private:InvocationError.CategoryInfo.Reason
    }

    Write-Verbose "[RUNTIME-Send-FunctionHandlerError]Send response error object"
    $private:responseStream = $private:responseRequest.GetRequestStream()
    $private:responseByteArray = [System.Text.Encoding]::UTF8.GetBytes($private:responseErrorBody)
    $private:responseStream.Write($private:responseByteArray, 0, $private:responseByteArray.Length)

    $null = $private:responseRequest.GetResponse()
    if ($private:responseStream) { $private:responseStream.Dispose() }
}