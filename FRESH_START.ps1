# Complete Fresh Start - Clear All Caches and Restart
Write-Host "========================================" -ForegroundColor Green
Write-Host "  FRESH START - CLEARING ALL CACHES" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# Set location
Set-Location d:\AutomationEdge\InterviewAgent
Write-Host "[1/5] Setting location to interview agent directory..." -ForegroundColor Cyan

# Kill all Python processes
Write-Host "[2/5] Killing all Python processes..." -ForegroundColor Cyan
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2
Write-Host "      ✓ All Python processes stopped" -ForegroundColor Green

# Delete Python cache files
Write-Host "[3/5] Clearing Python cache files..." -ForegroundColor Cyan
Get-ChildItem -Path . -Filter "*.pyc" -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Force -ErrorAction SilentlyContinue
Get-ChildItem -Path . -Filter "__pycache__" -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Write-Host "      ✓ Cache files cleared" -ForegroundColor Green

# Verify files exist
Write-Host "[4/5] Verifying required files..." -ForegroundColor Cyan
$requiredFiles = @(
    "web_app.py",
    "question_bank_expanded.py",
    "interview_session.py",
    "scoring_evaluator.py",
    "report_generator.py"
)

foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Host "      ✓ $file exists" -ForegroundColor Green
    } else {
        Write-Host "      ✗ $file MISSING!" -ForegroundColor Red
    }
}

# Start fresh web app
Write-Host "[5/5] Starting web app with fresh question bank..." -ForegroundColor Cyan
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  STARTING AI INTERVIEW PANELIST" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Open your browser: http://localhost:5000" -ForegroundColor Yellow
Write-Host "Each interview will have DIFFERENT questions!" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# Start the web app
python web_app.py
