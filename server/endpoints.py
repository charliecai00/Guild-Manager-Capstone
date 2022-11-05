from flask import Flask, request
from flask_restx import Resource, Api, fields
# import werkzeug.exceptions as wz

from game.game_object import Game

app = Flask(__name__)
api = Api(app)

INPUT = '/input'
MAIN_MENU = '/main_menu'
RESULT = 'Results'
ERROR = 'Error'

game = Game()


@api.route(MAIN_MENU)
class MainMenu(Resource):
    # Returns a list of commands
    def get(self):
        return {'Title': 'Main Menu',
                'Options': {
                    '1': {'text': 'Add_To_Party'},
                    '2': {'text': 'Do_Quest'},
                    '3': {'text': 'Get_Heroes'},
                    '4': {'text': 'Get_Quests'},
                    '5': {'text': 'Hire_Heroes'},
                    '6': {'text': 'List_Guild_Members'},
                    'X': {'text': 'Exit'},
                }
        }


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
        elif (_type == "List_Guild_Members"):
            res = game.Guild_Status()
            return {RESULT: res}
            