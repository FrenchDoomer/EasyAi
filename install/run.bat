@echo off
REM ====================================================
REM ====================================================
set PYTHON= "E:\EasyAI\.venv\Scripts\python.exe"
set COMMANDLINE_ARGS= -s -d
REM ====================================================
REM ====================================================
if not defined PYTHON (set PYTHON=python)
%PYTHON% run.py %COMMANDLINE_ARGS%
