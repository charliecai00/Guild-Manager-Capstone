#!/bin/bash

# run our server locally:
PYTHONPATH=$(pwd):$PYTHONPATH
FLASK_APP=endpoints python3 -m flask run --host=127.0.0.1 --port=8000
