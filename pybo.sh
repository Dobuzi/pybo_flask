#!/bin/bash
export FLASK_APP=pybo
export FLASK_ENV=development
source venv/bin/activate
pip install -r requirements.txt
flask run
