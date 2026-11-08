#Requires -Version 5.1
<#
.SYNOPSIS
    Import the risk-analysis tool and agent into the active watsonx Orchestrate environment.

.DESCRIPTION
    Dependency order: tool first, then agent.
    Run from the repository root:

        Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
        .\scripts\import-all.ps1

    Prerequisites:
        - venv\Scripts\Activate.ps1 must be present (run: python -m venv venv && pip install ibm-watsonx-orchestrate)
        - An active WXO environment: orchestrate env list
        - Sync tests must pass: python -m pytest tests\test_sync.py tests\test_wxo_tool.py -v
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot

Write-Host "Activating venv..."
& "$repoRoot\venv\Scripts\Activate.ps1"

# Ensure the package-root copies are in sync before uploading.
# Uses binary copy to preserve exact line endings.
Write-Host ""
Write-Host "-> Syncing pipeline copy..."
[System.IO.File]::WriteAllBytes(
    "$repoRoot\tools\risk_tool_pkg\pipeline.py",
    [System.IO.File]::ReadAllBytes("$repoRoot\src\source-code\src\pipeline.py")
)

Write-Host "-> Syncing dataset copy..."
[System.IO.File]::WriteAllBytes(
    "$repoRoot\tools\risk_tool_pkg\data\public-service-risk-v1.json",
    [System.IO.File]::ReadAllBytes("$repoRoot\data\samples\public-service-risk-v1.json")
)

Write-Host ""
Write-Host "-> Importing Python tool (package root: tools\risk_tool_pkg)..."
orchestrate tools import `
    -k python `
    -f tools/risk_tool_pkg/analyze_risk_cases.py `
    --package-root tools/risk_tool_pkg

Write-Host ""
Write-Host "-> Importing agent..."
orchestrate agents import -f agents/risk_analysis_agent.yaml

Write-Host ""
Write-Host "Import complete."
Write-Host "Verify with: orchestrate tools list"
Write-Host "            orchestrate agents list"
