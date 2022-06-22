# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
function private:Invoke-FunctionHandler
{
    <#
        .SYNOPSIS
            Invoke Lambda handler function.

        .DESCRIPTION
            Invoke Lambda handler function.
    
        .Notes
            Runs entire script if handler isthe script, or function from script/module
    #>
    [CmdletBinding()]
    param
    (
        [Parameter(Mandatory)] $private:runtimeNextInvocationResponse,
        [Parameter(Mandatory)] $private:HandlerArray,
        [Parameter(Mandatory)] $private:LambdaContext
    )
    If ($env:POWERSHELL_RUNTIME_VERBOSE -eq 'TRUE') {$VerbosePreference = "continue"}
    Write-Verbose "[RUNTIME-Invoke-FunctionHandler]Start: Invoke-FunctionHandler"

    $private:LambdaInput = ConvertFrom-Json -InputObject $private:runtimeNextInvocationResponse.incomingEvent
    switch ($private:HandlerArray.handlerType) {
        "Module" {
            $private:functionInvocationResponse = & $private:handlerArray.functionName $private:LambdaInput $private:LambdaContext
        }
        "Function" {
            $private:functionInvocationResponse = & $private:handlerArray.functionName $private:LambdaInput $private:LambdaContext
        }
        "Script" {
            $private:functionInvocationResponse = & $private:handlerArray.scriptFilePath $private:LambdaInput $private:LambdaContext
        }
    }

    # Convert function response to a string if needed
    if ($private:functionInvocationResponse -and ($private:functionInvocationResponse.GetType().Name -ne 'String')) {
        $private:responseString = ConvertTo-Json -InputObject $private:functionInvocationResponse -Compress
    }
    else {
        $private:responseString = $private:functionInvocationResponse

    }
   
    return $private:responseString
}