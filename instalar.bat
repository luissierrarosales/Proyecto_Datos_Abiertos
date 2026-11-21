@echo off
title Instalacion del proyecto

py -m venv venv
call venv\Scripts\activate

py -m pip install --upgrade pip
py -m pip install -r requirements.txt

if not exist .env copy .env.example .env

echo.
echo Instalacion terminada. Revisa el archivo .env antes de iniciar.
pause