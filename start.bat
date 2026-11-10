@echo off
title SCARY DRAMA PROP - TERMINAL LOOP
color 0C
cls
echo ========================================================
echo   SCARY DRAMA PROP - TERMINAL LOOP
echo   Press Ctrl+C at any time to stop
echo ========================================================
echo.
python "%~dp0loop.py" %*
pause
