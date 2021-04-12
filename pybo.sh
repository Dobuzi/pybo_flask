#!/bin/bash
export FLASK_APP=pybo
export FLASK_ENV=development
export APP_CONFIG_FILE=/Users/dobuzi/Workspace/webApp/flask/pybo/config/development.py
source venv/bin/activate
pip install -r requirements.txt
flask run
