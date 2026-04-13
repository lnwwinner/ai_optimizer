@echo off

echo ==============================
echo Starting AI Malware System
echo ==============================

REM Activate virtual environment
if exist venv (
    call venv\Scripts\activate
) else (
    echo [ERROR] venv not found. Please run install first.
    pause
    exit /b
)

echo.
echo [1] Starting API Server...
start cmd /k python api\server.py

echo.
echo [2] Starting Dashboard...
start cmd /k python web\dashboard.py

echo.
echo ==============================
echo System is running

echo API: http://localhost:5000

echo Dashboard: http://localhost:7000

echo ==============================

pause
