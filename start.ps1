<#
.SYNOPSIS
    Launcher for Scary Drama / Film Terminal Prop
#>
param(
    [string]$Mode = "words",
    [double]$Delay = 0.03,
    [string]$Color = "bold_red"
)

$host.UI.RawUI.WindowTitle = "SCARY DRAMA PROP - TERMINAL LOOP"
Clear-Host
Write-Host "========================================================" -ForegroundColor Red
Write-Host "  SCARY DRAMA PROP - TERMINAL LOOP" -ForegroundColor Red
Write-Host "  Mode: $Mode | Delay: $Delay s | Color: $Color" -ForegroundColor DarkGray
Write-Host "  Press Ctrl+C at any time to exit" -ForegroundColor DarkGray
Write-Host "========================================================`n" -ForegroundColor Red

$scriptPath = Join-Path $PSScriptRoot "loop.py"
python $scriptPath --mode $Mode --delay $Delay --color $Color
