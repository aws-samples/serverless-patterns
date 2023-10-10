# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

Set-PSDebug -Strict

# Instantiated to be available within the scope of the files dot-sourced below.
$Script:ModuleRoot = $PSScriptRoot

$privateFunctionsPath = Join-Path -Path "$PSScriptRoot" -ChildPath 'Private'
$publicFunctionsPath = Join-Path -Path "$PSScriptRoot" -ChildPath 'Public'

# Dot-source each private and public function during import of module.
Get-ChildItem -Path $privateFunctionsPath, $publicFunctionsPath -Filter *.ps1 -Recurse | ForEach-Object {. $_.FullName}