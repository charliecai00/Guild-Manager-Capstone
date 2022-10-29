from flask import Flask, request
from flask_restx import Resource, Api, fields
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
        return {COMMANDS: [
            "Get_Heros",
            "Hire_Hero",
            "List_Guild_Members",
            "Add_Party",
            "Get_Quest",
            "Do_Quest"
        ]}

expected_input = api.model('expected_input', {
    "Type": fields.String(default="Add_To_Party", required=True),
    "Data": fields.String(default="specific data goes here", required=True)
})

@api.route((INPUT))
class input(Resource):
    # Input takes any kind of JSON for whatever command
    @api.expect(expected_input)
    def post(self):
        print(f'{request.json=}')
        type = request.json["Type"]
        if (type == "Add_To_Party"):
            return {MESSAGE: "This is add to party"}
        elif (type == "Do_Quest"):
            pass
        elif (type == "Get_Heroes"):
            pass
        elif (type == "Hire_Heroes"):
            pass
