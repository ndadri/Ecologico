@echo off
IF "%1"=="run" (
    venv\Scripts\python.exe app.py
) ELSE IF "%1"=="install" (
    venv\Scripts\pip.exe install -r requirements.txt
) ELSE IF "%1"=="freeze" (
    venv\Scripts\pip.exe freeze > requirements.txt
)