#!/bin/bash

# run our server locally:
export PYTHONPATH=$(pwd):$PYTHONPATH
export FLASK_DEBUG=1
FLASK_APP=server.endpoints python3 -m flask run --host=127.0.0.1 --port=8000
