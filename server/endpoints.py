# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from flask import Flask, request
from flask_restx import Resource, Api, fields, Namespace
from flask_cors import CORS

import game.guild_script as guild_script
import game.hero_script as hero_script
import game.party_script as party_script
import game.quest_script as quest_script
import db.guild as db_guild
import db.hero as db_hero
import db.party as db_party
import db.quest as db_quest

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

# Define namespaces
GUILD_NS = 'Guild'
QUEST_NS = 'Quest'
HERO_NS = 'Hero'
PARTY_NS = 'Party'
# Create namespaces
guild_ns = Namespace(GUILD_NS, 'Guild APIs')
quest_ns = Namespace(QUEST_NS, 'Quest API')
hero_ns = Namespace(HERO_NS, 'Hero API')
party_ns = Namespace(PARTY_NS, 'Party API')
api.add_namespace(guild_ns)
api.add_namespace(quest_ns)
api.add_namespace(hero_ns)
api.add_namespace(party_ns)
# Define API routes
CREATE = 'Create'
RELOAD = 'Reload'
UNSOLD_QUEST = 'Unsold_Quest'
BUY = 'Buy'
SELL = 'Sell'
START = 'Start'
HIRE = 'Hire'
FIRE = 'Fire'
UNEMPLOYED = 'Unemployed'
HEAL = 'Heal'
ADD_HERO = 'Add_Hero'
REMOVE_HERO = 'Remove_Hero'
ADD_PARTY = 'Add_Party'
DISBAND_PARTY = 'Disband_Party'
GET_PARTY = 'Get_Party'
GET_PARTY_DETAIL = 'Get_Party_Detail'
# Create guild routes
CREATE_PATH = f'{GUILD_NS}/{CREATE}'
RELOAD_PATH = f'{GUILD_NS}/{RELOAD}'
# Create quest routes
UNSOLD_QUEST_PATH = f'{QUEST_NS}/{UNSOLD_QUEST}'
BUY_PATH = f'{QUEST_NS}/{BUY}'
SELL_PATH = f'{QUEST_NS}/{SELL}'
START_PATH = f'{QUEST_NS}/{START}'
# Create hero routes
HIRE_PATH = f'{HERO_NS}/{HIRE}'
FIRE_PATH = f'{HERO_NS}/{FIRE}'
UNEMPLOYED_PATH = f'{HERO_NS}/{UNEMPLOYED}'
HEAL_PATH = f'{HERO_NS}/{HEAL}'
# Create party routes
ADD_HERO_PATH = f'{PARTY_NS}/{ADD_HERO}'
REMOVE_HERO_PATH = f'{PARTY_NS}/{REMOVE_HERO}'
ADD_PARTY_PATH = f'{PARTY_NS}/{ADD_PARTY}'
DISBAND_PARTY_PATH = f'{PARTY_NS}/{DISBAND_PARTY}'
GET_PARTY_PATH = f'{PARTY_NS}/{GET_PARTY}'
GET_PARTY_DETAIL_PATH = f'{PARTY_NS}/{GET_PARTY_DETAIL}'
# Create main menu route
# MAIN_MENU = '/main_menu'

# Define Marco
RES = 'Response'


@guild_ns.route(f'/{CREATE}')
class Create(Resource):
    create_input = api.model('Provide new guild name', {'Name': fields.String})

    @api.expect(create_input)
    def post(self):
        guild_script.generate_guild(request.json["Name"])
        return {RES: 'Success'}


@guild_ns.route(f'/{RELOAD}')
class Reload(Resource):
    def get(self):
        guilds = db_guild.get_guilds()
        guild_names = []
        for i in guilds:
            guild_names.append(i["Name"])
        return {RES: guild_names}


@quest_ns.route(f'/{UNSOLD_QUEST}')
class Unsold(Resource):
    def get(self):
        return {RES: db_quest.get_unpurchase_quest()}


@quest_ns.route(f'/{BUY}')
class Buy(Resource):
    buy_input = api.model('Buy quest by id', {'id': fields.Integer})

    @api.expect(buy_input)
    def post(self):
        return {RES: 'Success'}
    # Todo: call buy_quest()


@quest_ns.route(f'/{SELL}')
class Sell(Resource):
    sell_input = api.model('Sell quest by id', {'id': fields.Integer})

    @api.expect(sell_input)
    def post(self):
        return {RES: 'Success'}
    # Todo: call sell_quest()


@quest_ns.route(f'/{START}')
class StartQuest(Resource):
    start_input = api.model('Start quest and party by id playing the quest',
                            {'id': fields.Integer, 'party_id': fields.Integer})

    @api.expect(start_input)
    def post(self):
        quest_script.start_quest(request.json['id'], request.json['party_id'])
        return {RES: 'Success'}


@hero_ns.route(f'/{HIRE}')
class Hire(Resource):
    hire_input = api.model('Hire hero by id and provide guild id',
                           {'id': fields.Integer, 'guild_id': fields.Integer})

    @api.expect(hire_input)
    def post(self):
        if (hero_script.hire_hero(request.json['id'],
                                  request.json['guild_id'])):
            return {RES: "Success"}
        return {RES: "Could not hire hero, out of money."}


@hero_ns.route(f'/{FIRE}')
class Fire(Resource):
    fire_input = api.model('Fire hero by id', {'id': fields.Integer})

    @api.expect(fire_input)
    def post(self):
        hero_script.fire_hero(request.json['id'])
        return {RES: 'Success'}


@hero_ns.route(f'/{UNEMPLOYED}')
class Unemployed(Resource):
    def get(self):
        return {RES: db_hero.get_unemploy_hero()}


@hero_ns.route(f'/{HEAL}')
class Heal(Resource):
    heal_input = api.model('Heal hero by id', {'id': fields.Integer})

    @api.expect(heal_input)
    def post(self):
        hero_script.heal_hero(request.json['id'])
        return {RES: 'Success'}


@party_ns.route(f'/{ADD_PARTY}')
class AddParty(Resource):
    add_party_input = api.model('Give the new party a name',
                                {'Name': fields.String})

    @api.expect(add_party_input)
    def post(self):
        party_script.generate_party(request.json['Name'])
        return {RES: 'Success'}


@party_ns.route(f'/{DISBAND_PARTY}')
class DisbandParty(Resource):
    disband_party_input = api.model('Delete a party by id',
                                    {'id': fields.Integer})

    @api.expect(disband_party_input)
    def post(self):
        party_script.disband_party(request.json['id'])
        return {RES: 'Success'}


@party_ns.route(f'/{ADD_HERO}')
class AddHero(Resource):
    add_hero_input = api.model('Add hero to party by IDs',
                               {'id': fields.Integer,
                                'party_id': fields.Integer})

    @api.expect(add_hero_input)
    def post(self):
        party_script.add_party_hero(request.json['party_id'],
                                    request.json['id'])
        return {RES: 'Success'}


@party_ns.route(f'/{REMOVE_HERO}')
class RemoveHero(Resource):
    remove_hero_input = api.model('Remove hero to party by IDs',
                                  {'id': fields.Integer,
                                   'party_id': fields.Integer})

    @api.expect(remove_hero_input)
    def post(self):
        party_script.remove_party_hero(request.json['party_id'],
                                       request.json['id'])
        return {RES: 'Success'}


@party_ns.route(f'/{GET_PARTY}')
class GetParty(Resource):
    def get(self):
        return {RES: db_party.get_party()}


@party_ns.route(f'/{GET_PARTY_DETAIL}')
class GetPartyDetail(Resource):
    def get(self):
        return {RES: db_party.get_party_details()}


if __name__ == '__main__':
    app.run()
