# PowerShell helper that simply invokes the Python launcher.
# Works on Windows or any platform where PowerShell is available.

Write-Host "Starting Indoor Navigation (using Python launcher)"
python "$(Join-Path $PSScriptRoot 'manage.py')" start
