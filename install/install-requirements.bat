@echo off
REM ====================================================
REM ====================================================
set PYTHON= "E:\EasyAI\.venv\Scripts\python.exe"
REM ====================================================
REM ====================================================
if not defined PYTHON (set PYTHON=python)
%PYTHON% -m pip install -r requirements.txt
