from flask import Flask
from flask_restx import Resource, Api
# import db.db as db

app = Flask(__name__)
api = Api(app)


@api.route('/dummy_api')
class dummy_api(Resource):
    def get(self):
        return {"message": "Welcome to Guild Manager!"}


@api.route('/command_list')
class command_list(Resource):
    # Returns a list of commands
    def get(self):
        return {"commands": ["c1", "c2", "c3", "c4"]}


@api.route('/input')
class input(Resource):
    # Input takes any kind of JSON for whatever command
    def get(self):
        return {"test": "test"}
