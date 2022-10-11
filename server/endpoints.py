# from http import HTTPStatus

from flask import Flask  # , request
from flask_restx import Resource, Api  # , fields
# import werkzeug.exceptions as wz

app = Flask(__name__)
api = Api(app)

INPUT = '/input'
COMMAND_LIST = '/command_list'
MESSAGE = 'message'
COMMANDS = 'commands'


@api.route(COMMAND_LIST)
class command_list(Resource):
    # Returns a list of commands
    def get(self):
        return {COMMANDS: ["Get_Heros", "Find_Hero", "Hire_Hero", "Guild_Status", "Add_Party", "Get_Quest", "Find_Quest", "Do_Quest"]}


@api.route((INPUT))
class input(Resource):
    # Input takes any kind of JSON for whatever command
    def get(self):
        return {MESSAGE: "test"}
