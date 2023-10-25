@echo off
REM ====================================================
REM ====================================================
set PYTHON= 
set COMMANDLINE_ARGS= 
REM ====================================================
REM ====================================================
if not defined PYTHON (set PYTHON=python)
%PYTHON% run.py %COMMANDLINE_ARGS%
