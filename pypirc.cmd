REM "Write secure password to pypirc"
echo [distutils] # this tells distutils what package indexes you can push to > %USERPROFILE%\.pypirc
echo index-servers = >> %USERPROFILE%\.pypirc
echo     pypi >> %USERPROFILE%\.pypirc
echo     pypitest >> %USERPROFILE%\.pypirc
echo     legacy >> %USERPROFILE%\.pypirc
echo. >> %USERPROFILE%\.pypirc
echo [pypi] >> %USERPROFILE%\.pypirc
echo username: %PYPI_USERNAME% >> %USERPROFILE%\.pypirc
echo password: %PYPI_PASSWORD% >> %USERPROFILE%\.pypirc
echo. >> %USERPROFILE%\.pypirc
echo [pypitest] >> %USERPROFILE%\.pypirc
echo repository: https://testpypi.python.org/pypi >> %USERPROFILE%\.pypirc
echo username: %PYPI_USERNAME% >> %USERPROFILE%\.pypirc
echo password: %PYPI_PASSWORD% >> %USERPROFILE%\.pypirc
echo. >> %USERPROFILE%\.pypirc
echo [legacy] >> %USERPROFILE%\.pypirc
echo repository: https://upload.pypi.org/legacy/ >> %USERPROFILE%\.pypirc
echo username: %PYPI_USERNAME% >> %USERPROFILE%\.pypirc
echo password: %PYPI_PASSWORD% >> %USERPROFILE%\.pypirc
echo. >> %USERPROFILE%\.pypirc
echo [server-login] >> %USERPROFILE%\.pypirc
echo username: %PYPI_USERNAME% >> %USERPROFILE%\.pypirc
echo password: %PYPI_PASSWORD% >> %USERPROFILE%\.pypirc
dir %USERPROFILE%
