Write-Verbose "Run module init tasks before handler"
function examplehandler
{
    [cmdletbinding()]
    param(
        [parameter()]
        $InputObject,

        [parameter()]
        $Context
    )
    Write-Verbose "Function Remaining Time: $($LambdaContext.GetRemainingTimeInMillis())"
    Write-Verbose "Run handler function from module"
    Write-Output "Hello from PowerShell version $env:POWERSHELL_VERSION on Lambda."
}