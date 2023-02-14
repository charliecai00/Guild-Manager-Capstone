# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from flask import Flask, request
from flask.helpers import send_from_directory
from flask_restx import Resource, Api, fields
from flask_cors import CORS, cross_origin
# import werkzeug.exceptions as wz

from game.game_object import Game

app = Flask(__name__, static_folder='front-end/build', static_url_path='')
CORS(app)
api = Api(app)

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()