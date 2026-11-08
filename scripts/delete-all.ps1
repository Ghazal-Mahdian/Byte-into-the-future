#Requires -Version 5.1
<#
.SYNOPSIS
    Remove the risk-analysis agent and tool from the active watsonx Orchestrate environment.

.DESCRIPTION
    Removal order: agent first, then tool (reverse of import).
    Run from the repository root:

        Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
        .\scripts\delete-all.ps1
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Continue'   # allow individual steps to fail without stopping

$repoRoot = Split-Path -Parent $PSScriptRoot

Write-Host "Activating venv..."
& "$repoRoot\venv\Scripts\Activate.ps1"

Write-Host ""
Write-Host "-> Removing agent risk_analysis_agent..."
orchestrate agents remove -n risk_analysis_agent --kind native

Write-Host ""
Write-Host "-> Removing tool analyze_risk_cases..."
orchestrate tools remove -n analyze_risk_cases

Write-Host ""
Write-Host "Cleanup complete."
