#!/bin/bash
export FLASK_APP=pybo
export FLASK_ENV=development
export APP_CONFIG_FILE=/Users/dobuzi/Workspace/webApp/flask/config/development.py
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run