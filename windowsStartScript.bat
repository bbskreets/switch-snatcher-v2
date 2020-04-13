@echo off

WHERE python
IF %ERRORLEVEL% NEQ 0 ECHO Python is not in your path or is not installed. If you installed, follow this: https://geek-university.com/python/add-python-to-the-windows-path/ 
pause 

goto :DOES_PYTHON_EXIST

:DOES_PYTHON_EXIST
python -V | find /v "Python" >NUL 2>NUL && (goto :PYTHON_DOES_NOT_EXIST)
python -V | find "Python 3"    >NUL 2>NUL && (goto :PYTHON_DOES_EXIST)
goto :EOF

:PYTHON_DOES_NOT_EXIST
echo Python 3 is not installed on your system.
echo Now opening the download URL.
start "" "https://www.python.org/downloads/windows/"
goto :EOF

:PYTHON_DOES_EXIST
:: This will retrieve Python 3.8.0 for example.
python -m pip install --user -r requirements.txt
cd %~dp0
start powershell -noexit -Command "& {python run.py}"
goto :EOF
