@echo off
REM start.bat — one click starter for demo_webapp
SETLOCAL

REM change directory to project (note the quotes because of spaces and `!`)
cd /d "D:\Kar Har Maidan Fateh!\project_option_b\demo_webapp"

REM Try to activate venv (venv or .venv)
if exist "venv\Scripts\activate.bat" (
  echo Activating venv...
  call "venv\Scripts\activate.bat"
) else if exist ".venv\Scripts\activate.bat" (
  echo Activating .venv...
  call ".venv\Scripts\activate.bat"
) else (
  echo No virtualenv found (venv or .venv). Using system python.
  echo To create a venv run: python -m venv venv
)

REM Optional: tweak these if you want
set FLASK_DEBUG=1
set FLASK_RUN_HOST=127.0.0.1
set FLASK_RUN_PORT=5000

echo Starting Flask app...
python run.py

echo.
echo Flask process exited.
pause
ENDLOCAL
