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

MAIN_MENU = '/main_menu'
ADD_PARTY_WITH_HEROS = '/add_party_with_heros'
DISBAND_PARTY = '/disband_party'
DO_QUEST = '/do_quest'
ADD_HEROES = '/add_heroes'
GET_QUEST = '/get_quest'
HIRE_HEROS = '/hire_heros'
FIRE_HERO = '/fire_hero'
LIST = '/list'

ERROR = 'Error'
RESULT = 'Result'
DATA = 'Data'
TYPE = 'Type'
TITLE = 'Title'

game = Game()


@api.route(MAIN_MENU)
@cross_origin()
class MainMenu(Resource):
    # Returns a list of commands
    def get(self):
        return {'Title': 'Main Menu',
                'Default': 0,
                'Choices': {
                    '1': {'text': 'ADD_PARTY_WITH_HEROS',
                          'url': '/add_party_with_heros',
                          'method': 'post'},
                    '2': {'text': 'Do_Quest',
                          'url': '/do_quest',
                          'method': 'post'},
                    '3': {'text': 'Add_Heroes',
                          'url': '/add_heroes',
                          'method': 'post'},
                    '4': {'text': 'Get_Quests',
                          'url': '/get_quest',
                          'method': 'get'},
                    '5': {'text': 'Hire_Heros',
                          'url': '/hire_heros',
                          'method': 'post'},
                    '6': {'text': 'List_Guild_Members',
                          'url': '/list',
                          'method': 'get'},
                    '7': {'text': 'Disband_Party',
                          'url': '/disband_party',
                          'method': 'post'},
                    '8': {'text': 'Fire_Hero',
                          'url': '/fire_hero',
                          'method': 'post'},
                    'X': {'text': 'Exit'},
                }
                }


add_heroes_input = api.model('add_heroes', {
    "Count": fields.Integer(default="10", required=False),
    "Type": fields.String(default="Mage", required=False)
})


@api.route(ADD_HEROES)
@cross_origin()
class AddHeroes(Resource):
    """
    The endpoint adds hero to DB.
    It takes 2 arguments:
        Count - how many heros to add?
        Type - what is the type of hero?
    """
    @api.expect(add_heroes_input)
    def post(self):
        print(f'{request.json=}')

        count = request.json["Count"]
        hero_class = request.json["Type"]

        # Todo: function to call
        res = str(game.Add_Heros(count, hero_class))
        return {DATA: {"Heros": {"": res}},
                TYPE: hero_class,
                TITLE: 'Add Heroes'}


hire_heros_input = api.model('hire_heros', {
    "Hiree": fields.Integer(default=0, required=True)
})


@api.route(HIRE_HEROS)
@cross_origin()
class HireHeros(Resource):
    """
    The endpoint hire heros as requested by the user.
    It takes 1 argument:
        Hero ID - what is the hero ID?
    """
    @api.expect(hire_heros_input)
    def post(self):
        print(f'{request.json=}')

        hero_id = request.json["Hiree"]

        result = game.Hire_Hero(hero_id)
        if result:
            return {RESULT: "Hero hired."}
        else:
            return {RESULT: "Could not hire hero, out of money."}


fire_hero_input = api.model('fire_hero', {
    "Firee": fields.Integer(default=0, required=True),
})


@api.route(FIRE_HERO)
@cross_origin()
class FireHero(Resource):
    """
    The endpoint fire hero as requested by the user.
    It takes 1 argument:
        Hero ID - what is the hero ID to fire?
    """
    @api.expect(fire_hero_input)
    def post(self):
        print(f'{request.json=}')
        hero_id = request.json["Firee"]
        print("hero id in fire hero ", hero_id)
        result = game.Fire_Hero(hero_id)
        if result:
            return {RESULT: "Hero Fired."}
        else:
            return {RESULT: "Request failed. Check input."}


add_party_with_heros_input = api.model('add_party_with_heros', {
    "HeroIDs": fields.String(default="0,1,2", required=True),
    "PartyName": fields.String(default="testPartyName")
})


@api.route(ADD_PARTY_WITH_HEROS)
@cross_origin()
class AddPartyWithHeros(Resource):
    """
    The endpoint adds hero to a party
    It takes 2 arguments:
        Hero ID - what is the hero ID that you're hiring?
        Party ID - what is the party ID that you're adding the hero to?
    """
    @api.expect(add_party_with_heros_input)
    def post(self):
        print(f'{request.json=}')
        HeroIDs = request.json["HeroIDs"]
        PartyName = request.json["PartyName"]
        parse_hero_ID = HeroIDs.split(",")

        # for i in range(len(parse_hero_ID)):
        #     parse_hero_ID[i] = int(parse_hero_ID[i])
        # print("endpoint ", type(parse_hero_ID[0]))
        result = game.Add_Party_With_Heros(parse_hero_ID, PartyName)
        if result:
            return {RESULT:
                    "Heros added to a new party."}
        else:
            return {RESULT:
                    "Some heros were not hired in the guild."}


disband_party_input = api.model('disband_party', {
    "PartyID": fields.Integer(default=0, required=True)
})


@api.route(DISBAND_PARTY)
@cross_origin()
class DisbandParty(Resource):
    """
    The endpoint removes a party from the Guild.
    It takes 1 argument:
        Party ID - what is the party ID?
    """
    @api.expect(disband_party_input)
    def post(self):
        print(f'{request.json=}')

        party_ID = request.json["PartyID"]
        print("check party in the test: ", game.guild.party_dic)

        result = game.Disband_Party(int(party_ID))
        if result:
            return {RESULT: "{} disbanded.".format(party_ID)}
        else:
            return {RESULT: "Request failed. Check input."}


do_quest_input = api.model('do_quest', {
    "PartyID": fields.Integer(default="0", required=True),
    "QuestID": fields.Integer(default="0", required=True)
})


@api.route(DO_QUEST)
@cross_origin()
class DoQuest(Resource):
    """
    User can start on a quest.
    The endpoint takes 2 arguments:
        Party ID - what is the party doing the quest?
        Quest ID - what is the quest that you want to do?
    """
    @api.expect(do_quest_input)
    def post(self):
        print(f'{request.json=}')

        party_ID = request.json["PartyID"]
        quest_ID = request.json["QuestID"]

        result = game.Do_Quest(quest_ID, party_ID)
        if result:
            return {RESULT: "{} completed the quest!".format(party_ID)}
        else:
            return {RESULT: "Request failed. Check input."}


@api.route(GET_QUEST)
@cross_origin()
class GetQuest(Resource):
    """
    Get details on a quest.
    """
    def get(self):
        res = game.Get_Quest().get_info()
        return {DATA: {"Name": {"": res[0]}, "Skill": {"": res[1:]}},
                TYPE: 'Data',
                TITLE: 'Get Quest'}


@api.route(LIST)
@cross_origin()
class List(Resource):
    """
    Get all informations on the Guild including:
        Funds
        Heros
        Parties
        Quests
    """
    def get(self):
        res = str(game.Guild_Status()).split(" ")
        funds = res[1]
        heros = res[3]
        parties = res[5]
        quests = res[7]
        return {DATA: {"Funds": {"": funds},
                       "Heros": {"": heros},
                       "Parties": {"": parties},
                       "Quests": {"": quests}},
                TYPE: 'Data',
                TITLE: 'List Guild Members'}

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()