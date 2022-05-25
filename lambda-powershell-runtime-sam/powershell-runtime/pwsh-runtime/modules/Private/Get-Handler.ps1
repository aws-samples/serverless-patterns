# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
function private:Get-Handler
{
    <#
        .SYNOPSIS
            Parse _HANDLER environment variable

        .DESCRIPTION
            Parse _HANDLER environment variable
    
        .Notes
            Valid "_HANDLER" options:
            - "<script.ps1>" 
            - "<script.ps1>::<function_name>"
            - "Module::<module_name>::<function_name>"
    #>
    [CmdletBinding()]
    param
    (
        [String]
        $handler = $env:_HANDLER
    )
    If ($env:POWERSHELL_RUNTIME_VERBOSE -eq 'TRUE') {$VerbosePreference = "continue"}
    Write-Verbose "[RUNTIME-Get-Handler]Start: Get-Handler"

    enum HandlerType {
        Script
        Function
        Module
    }

    Write-Verbose "[RUNTIME-Get-Handler]Split _HANDLER environment variable"
    $private:handlerArray = $handler.Split('::')

    if ($private:handlerArray[0] -like '*.ps1' -and $private:handlerArray.Count -eq 1) {
        # Handler contains only a script file
        Write-Verbose "[RUNTIME-Get-Handler]Handler contains only a script file"

        $private:handlerObject = @{
            handlerType = [HandlerType]::Script
            scriptFileName = $private:handlerArray[0]
            scriptFilePath = [System.IO.Path]::Combine($env:LAMBDA_TASK_ROOT, $private:handlerArray[0])
        }
        Write-Verbose "[RUNTIME-Get-Handler]Handler type set to: $($private:handlerObject.handlerType)"
        Write-Verbose "[RUNTIME-Get-Handler]Handler set to PowerShell script name: $($private:handlerObject.scriptFileName)"
    }

    elseif ($private:handlerArray[0] -like '*.ps1' -and $private:handlerArray.Count -eq 2) {
        # Handler contains a script file and handler function name
        Write-Verbose "[RUNTIME-Get-Handler]Handler contains a script file and handler function name"

        $private:handlerObject = @{
            handlerType = [HandlerType]::Function
            scriptFileName = $private:handlerArray[0]
            scriptFilePath = [System.IO.Path]::Combine($env:LAMBDA_TASK_ROOT, $private:handlerArray[0])
            functionName = $private:handlerArray[1]
        }

        Write-Verbose "[RUNTIME-Get-Handler]Handler type set to: $($private:handlerObject.handlerType)"
        Write-Verbose "[RUNTIME-Get-Handler]Script file set to PowerShell script name: $($private:handlerObject.scriptFileName)"
        Write-Verbose "[RUNTIME-Get-Handler]Handler set to PowerShell function: $($private:handlerObject.functionName)"

    }
    elseif ($private:handlerArray[0] -eq 'Module' -and $private:handlerArray.Count -eq 3) {
        # Handler contains a module name and handler function name
        Write-Verbose "[RUNTIME-Get-Handler]Handler contains a module name and handler function name"

        $private:handlerObject = @{
            handlerType = [HandlerType]::Module
            moduleName = $private:handlerArray[1]
            functionName = $private:handlerArray[2]
        }
        Write-Verbose "[RUNTIME-Get-Handler]Handler type set to: $($private:handlerObject.handlerType)"
        Write-Verbose "[RUNTIME-Get-Handler]Module name set to PowerShell module: $($private:handlerObject.moduleName)"
        Write-Verbose "[RUNTIME-Get-Handler]Handler set to PowerShell function: $($private:handlerObject.functionName)"

    }
    # Unable to parse Handler object
    else { 
        Write-Verbose "[RUNTIME-Get-Handler]Unable to parse Handler object"
        throw ('Invalid Lambda Handler: {0}' -f $handler)
    }
 
    Write-Verbose "[RUNTIME-Get-Handler]Return handlerObject"
    return [pscustomobject]$private:handlerObject
}