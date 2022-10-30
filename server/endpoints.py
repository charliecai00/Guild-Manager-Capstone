from flask import Flask, request
from flask_restx import Resource, Api, fields
# import werkzeug.exceptions as wz

from game.game_object import Game

app = Flask(__name__)
api = Api(app)

INPUT = '/input'
COMMAND_LIST = '/command_list'
COMMANDS = 'Commands'
RESULT = 'Results'
ERROR = 'Error'

game = Game()


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
    "Data1": fields.String(default="specific data goes here", required=True),
    "Data2": fields.String(default="specific data goes here", required=True)
})


@api.route((INPUT))
class input(Resource):
    # Input takes any kind of JSON for whatever command
    @api.expect(expected_input)
    def post(self):
        print(f'{request.json=}')
        _type = request.json["Type"]
        if (_type == "Add_To_Party"):
            hero_ID = request.json["Data1"]
            party_ID = request.json["Data2"]

            parse_hero_ID = hero_ID.split(",")
            game.Add_Party(party_ID, parse_hero_ID)
        elif (_type == "Do_Quest"):
            party_ID = request.json["Data1"]
            quest_ID = request.json["Data2"]

            result = game.Do_Quest(quest_ID, party_ID)
            if result:
                print("{} completed the quest!".format(party_ID))
            else:
                print("{} failed".format(party_ID))
        elif (_type == "Get_Heroes"):
            count = request.json["Data1"]
            hero_class = request.json["Data2"]

            #Todo: function to call
            res = game.Get_Heros()
            return {RESULT: res}
        elif (_type == "Get_Quests"):
            res = game.Get_Quest()
            return {RESULT: res}
        elif (_type == "Hire_Heroes"):
            hero_list = request.json["Data1"]

            hero_list = hero_list.split(",")
            for i in hero_list:
                if not game.Hire_Hero(i):
                    return {ERROR: "Could not hire hero, out of money"}
        elif (_type == "Get_Quests"):
            res = game.Guild_Status()
            return {RESULT: res}
            