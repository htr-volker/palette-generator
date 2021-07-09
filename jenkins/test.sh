#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip3 install -r test-requirements.txt

pytest --cov=frontend/application --cov-report xml --cov-report term-missing --junitxml junit.xml