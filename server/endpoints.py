from flask import Flask, request
from flask_restx import Resource, Api, fields
# import werkzeug.exceptions as wz

from game.game_object import Game

app = Flask(__name__)
api = Api(app)

MAIN_MENU = '/main_menu'
ADD_TO_PARTY = '/add_to_party'
DO_QUEST = '/do_quest'
GET_HEROES = '/get_heroes'
GET_QUEST = '/get_quest'
HIRE_HEROES = '/hire_heroes'
LIST = '/list'
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


add_to_party_input = api.model('example', {
    "HeroIDs": fields.String(default="data... ", required=True),
    "PartyID": fields.Integer(default="data... ", required=True)
})


@api.route(ADD_TO_PARTY)
class AddToParty(Resource):
    @api.expect(add_to_party_input)
    def post(self):
        print(f'{request.json=}')

        HeroIDs = request.json["HeroIDs"]
        PartyID = request.json["PartyID"]

        parse_hero_ID = HeroIDs.split(",")
        game.Add_Party(PartyID, parse_hero_ID)


do_quest_input = api.model('example', {
    "PartyID": fields.Integer(default="data... ", required=True),
    "QuestID": fields.Integer(default="data... ", required=True)
})


@api.route(DO_QUEST)
class DoQuest(Resource):
    @api.expect(do_quest_input)
    def post(self):
        print(f'{request.json=}')

        party_ID = request.json["PartyID"]
        quest_ID = request.json["QuestID"]

        result = game.Do_Quest(quest_ID, party_ID)
        if result:
            return {RESULT: "{} completed the quest!".format(party_ID)}
        else:
            return {RESULT: "{} failed".format(party_ID)}


get_heroes_input = api.model('example', {
    "Count": fields.Integer(default="data... ", required=True),
    "Type": fields.String(default="data... ", required=True)
})


@api.route(GET_HEROES)
class GetHeroes(Resource):
    @api.expect(get_heroes_input)
    def post(self):
        print(f'{request.json=}')

        count = request.json["Count"]
        hero_class = request.json["Type"]

        # Todo: function to call
        res = game.Get_Heros()
        return {RESULT: res}


@api.route(GET_QUEST)
class GetQuest(Resource):
    def get(self):
        res = game.Get_Quest()
        return {RESULT: res}


hire_heroes_input = api.model('example', {
    "HireList": fields.Integer(default="data... ", required=True),
})


@api.route(HIRE_HEROES)
class HireHeroes(Resource):
    @api.expect(hire_heroes_input)
    def post(self):
        print(f'{request.json=}')

        hero_list = request.json["HireList"]

        hero_list = hero_list.split(",")
        for i in hero_list:
            if not game.Hire_Hero(i):
                return {ERROR: "Could not hire hero, out of money"}


@api.route(LIST)
class List(Resource):
    def get(self):
        res = game.Guild_Status()
        return {RESULT: res}
