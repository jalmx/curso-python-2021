#!/bin/bash

python3 -m venv .
source ./bin/activate
pip install notebook
pip install autopep8
pip install BeautifulSoup4 requests bs4
jupyter notebook ./Documentacion
