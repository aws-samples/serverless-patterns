# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
function private:Get-LambdaNextInvocation
{
    <#
        .SYNOPSIS
            Get /NEXT invocation from AWS Lambda Runtime API.

        .DESCRIPTION
            Get /NEXT invocation from AWS Lambda Runtime API.
    
        .Notes
            If there is an error calling the Runtime API endpoint, this is ignored and retried as part of the event loop.
    #>
    If ($env:POWERSHELL_RUNTIME_VERBOSE -eq 'TRUE') {$VerbosePreference = "continue"}
    Write-Verbose "[RUNTIME-Get-LambdaNextInvocation]Start: Get-LambdaNextInvocation"

    Write-Verbose "[RUNTIME-Get-LambdaNextInvocation]Create GET request to Runtime API"
    $private:incomingWebRequest = [System.Net.WebRequest]::Create("http://$env:AWS_LAMBDA_RUNTIME_API/2018-06-01/runtime/invocation/next")
    $private:incomingWebRequest.Headers.Add("User-Agent", "aws-lambda-powershell/" + $env:POWERSHELL_VERSION)
    try {
        # Get the next invocation
        Write-Verbose "[RUNTIME-Get-LambdaNextInvocation]Get the next invocation"
        $private:incomingWebResponse = $private:incomingWebRequest.GetResponse()
    }
    catch {
        # If there is an error calling the Runtime API endpoint, ignore which tries again
        continue
    }

    Write-Verbose "[RUNTIME-Get-LambdaNextInvocation]Read response stream"
    $private:incomingStreamReader = [System.IO.StreamReader]::new($private:incomingWebResponse.GetResponseStream())
    $private:incomingEvent = $private:incomingStreamReader.ReadToEnd()
    $private:incomingStreamReader.Dispose()

    # If there is no response from the Runtime API endpoint, ignore which tries again.
    if ([String]::IsNullOrWhiteSpace($private:incomingEvent)) { continue }
    else {
        $private:responseStream = $null
    }

    Write-Verbose "[RUNTIME-Get-LambdaNextInvocation]Create response object"
    $private:NextInvocationResponseObject = [pscustomobject]@{
        headers = $private:incomingWebResponse.Headers
        incomingEvent = $private:incomingEvent
    }
    if ($private:responseStream) { $private:responseStream.Dispose() }
    Write-Verbose "[RUNTIME-Get-LambdaNextInvocation]return response object"
    return [pscustomobject]$private:NextInvocationResponseObject        
}