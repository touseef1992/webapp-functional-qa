# run_tests.ps1
param([switch]$UsePYTHONPATH)

# Activate venv
. .\.venv\Scripts\Activate.ps1

if ($UsePYTHONPATH) {
    $env:PYTHONPATH = (Resolve-Path .).Path
    Write-Host "PYTHONPATH set to $env:PYTHONPATH"
}

pytest -q --maxfail=1 --html=reports/pytest-report.html --self-contained-html
