Write-Host "Activating virtual environment..."

# Activate venv
.\venv\Scripts\Activate

Write-Host "Running tests..."

pytest

if ($LASTEXITCODE -eq 0) {
    Write-Host "All tests passed ✅"
    exit 0
} else {
    Write-Host "Tests failed ❌"
    exit 1
}