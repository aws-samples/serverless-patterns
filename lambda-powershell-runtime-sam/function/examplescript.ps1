Write-Verbose "Run script"
Write-Verbose $LambdaInput
Write-Verbose "Function Remaining Time: $($LambdaContext.GetRemainingTimeInMillis())"
Write-Output "Hello from PowerShell version $env:POWERSHELL_VERSION on Lambda."