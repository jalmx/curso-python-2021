#! /bin/bash

#prepara el entorno virtual
python3 -m venv .

#arranco el entorno
source ./bin/activate

# prepara el bot
pip install python-telegram-bot --upgrade

#crear el archivo que contendra el token de telegram
touch TOKEN.py
echo "TOKEN='YOUR KEY'" >> TOKEN.py

mv TOKEN.py ./src/

# instalacion de lib para scrap

pip install requests beautifulsoup4