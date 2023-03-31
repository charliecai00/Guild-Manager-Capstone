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
GUILD_DETAIL = 'Guild_Detail'
UNSOLD_QUEST = 'Unsold_Quest'
BUY = 'Buy'
SELL = 'Sell'
START = 'Start'
QUEST_DETAIL = 'Quest_Detail'
HIRE = 'Hire'
FIRE = 'Fire'
UNEMPLOYED = 'Unemployed'
HEAL = 'Heal'
HERO_DETAIL = 'Hero_Detail'
DB_ADD_HERO = 'DB_Add_Heroes'
ADD_HERO = 'Add_Hero'
REMOVE_HERO = 'Remove_Hero'
ADD_PARTY = 'Add_Party'
DISBAND_PARTY = 'Disband_Party'
GET_PARTY = 'Get_Party'
PARTY_DETAIL = 'Party_Detail'
# Create guild routes
CREATE_PATH = f'{GUILD_NS}/{CREATE}'
RELOAD_PATH = f'{GUILD_NS}/{RELOAD}'
GUILD_DETAIL_PATH = f'{GUILD_NS}/{GUILD_DETAIL}'
# Create quest routes
UNSOLD_QUEST_PATH = f'{QUEST_NS}/{UNSOLD_QUEST}'
BUY_PATH = f'{QUEST_NS}/{BUY}'
SELL_PATH = f'{QUEST_NS}/{SELL}'
START_PATH = f'{QUEST_NS}/{START}'
QUEST_DETAIL_PATH = f'{QUEST_NS}/{QUEST_DETAIL}'
# Create hero routes
HIRE_PATH = f'{HERO_NS}/{HIRE}'
FIRE_PATH = f'{HERO_NS}/{FIRE}'
UNEMPLOYED_PATH = f'{HERO_NS}/{UNEMPLOYED}'
HEAL_PATH = f'{HERO_NS}/{HEAL}'
HERO_DETAIL_PATH = f'{HERO_NS}/{HERO_DETAIL}'
DB_ADD_HERO_PATH = f'{HERO_NS}/{DB_ADD_HERO}'
# Create party routes
ADD_HERO_PATH = f'{PARTY_NS}/{ADD_HERO}'
REMOVE_HERO_PATH = f'{PARTY_NS}/{REMOVE_HERO}'
ADD_PARTY_PATH = f'{PARTY_NS}/{ADD_PARTY}'
DISBAND_PARTY_PATH = f'{PARTY_NS}/{DISBAND_PARTY}'
GET_PARTY_PATH = f'{PARTY_NS}/{GET_PARTY}'
PARTY_DETAIL_PATH = f'{PARTY_NS}/{PARTY_DETAIL}'
# Create main menu route
# MAIN_MENU = '/main_menu'

# Define Marco
RES = 'Response'
detail_input = api.model('Return Detail w/ ID', {'id': fields.Integer})


@guild_ns.route(f'/{CREATE}')
class Create(Resource):
    create_input = api.model('Create', {'Name': fields.String})

    @api.expect(create_input)
    def post(self):
        guild_script.generate_guild(request.json["Name"])
        return {RES: 'Success'}


@guild_ns.route(f'/{RELOAD}')
class Reload(Resource):
    """
    Return example: [{id:name}] -> [{1:'guild1'}, {2:'guild2}]
    """
    def get(self):
        guilds = db_guild.get_guilds()
        guild_ids_names = []
        for i in guilds:
            guild_ids_names.append({"id": i['ID'], "name": i['Name']})
        return {RES: guild_ids_names}


@guild_ns.route(f'/{GUILD_DETAIL}')
class GuildDetail(Resource):
    @api.expect(detail_input)
    def post(self):
        res = db_guild.get_guild_details(request.json['id'])
        # Number summary
        res["Amt. of Hero"] = len(res["HeroIDs"])
        res["Amt. of Party"] = len(res["PartyIDs"])
        res["Amt. of Quest"] = len(res["QuestIDs"])

        # Look up hero
        heroes = []
        for i in res["HeroIDs"]:
            hero_detail = db_hero.get_hero_details(i)
            heroes.append({'id': i, "name": hero_detail["Name"]})
        res["Hero"] = heroes
        del res['HeroIDs']

        # Look up party
        party = []
        for i in res["PartyIDs"]:
            party_detail = db_party.get_party_details(i)
            party.append({'id': i, "name": party_detail["Name"]})
        res["Party"] = party
        del res['PartyIDs']

        # Look up quest
        quest = []
        for i in res["QuestIDs"]:
            quest_detail = db_quest.get_quest_details(i)
            quest.append({'id': i, "name": quest_detail["Name"]})
        res["Quest"] = quest
        del res['QuestIDs']

        return {RES: res}


@quest_ns.route(f'/{UNSOLD_QUEST}')
class Unsold(Resource):
    def get(self):
        return {RES: db_quest.get_unpurchase_quest()}


@quest_ns.route(f'/{BUY}')
class Buy(Resource):
    buy_input = api.model('Buy', {'id': fields.Integer,
                                  'guild_id': fields.Integer})

    @api.expect(buy_input)
    def post(self):
        flag, msg = quest_script.buy_quest(request.json['id'],
                                           request.json['guild_id'])
        if flag:
            return {RES: msg}
        return {RES: msg}


@quest_ns.route(f'/{SELL}')
class Sell(Resource):
    sell_input = api.model('Sell', {'id': fields.Integer,
                                    'guild_id': fields.Integer})

    @api.expect(sell_input)
    def post(self):
        flag, msg = quest_script.sell_quest(request.json['id'],
                                            request.json['guild_id'])
        if flag:
            return {RES: msg}
        return {RES: msg}


@quest_ns.route(f'/{START}')
class StartQuest(Resource):
    start_input = api.model('StartQuest', {'id': fields.Integer,
                                           'party_id': fields.Integer})

    @api.expect(start_input)
    def post(self):
        report = quest_script.start_quest(request.json['id'],
                                          request.json['party_id'])
        return {RES: report}


@quest_ns.route(f'/{QUEST_DETAIL}')
class QuestDetail(Resource):
    @api.expect(detail_input)
    def post(self):
        return {RES: db_quest.get_quest_details(request.json['id'])}


@hero_ns.route(f'/{HIRE}')
class Hire(Resource):
    hire_input = api.model('Hire', {'id': fields.Integer,
                                    'guild_id': fields.Integer})

    @api.expect(hire_input)
    def post(self):
        flag, msg = guild_script.hire_guild_hero(request.json['guild_id'],
                                                 request.json['id'])
        if flag:
            return {RES: "Success"}
        return {RES: msg}


@hero_ns.route(f'/{FIRE}')
class Fire(Resource):
    fire_input = api.model('Fire', {'id': fields.Integer,
                                    'guild_id': fields.Integer})

    @api.expect(fire_input)
    def post(self):
        flag, msg = guild_script.fire_guild_hero(request.json['guild_id'],
                                                 request.json['id'])
        if flag:
            return {RES: "Success"}
        return {RES: msg}


@hero_ns.route(f'/{UNEMPLOYED}')
class Unemployed(Resource):
    def get(self):
        return {RES: db_hero.get_unemploy_hero()}


@hero_ns.route(f'/{HEAL}')
class Heal(Resource):
    heal_input = api.model('Heal', {'id': fields.Integer,
                                    'guild_id': fields.Integer})

    @api.expect(heal_input)
    def post(self):
        flag, msg = hero_script.heal_hero(request.json['id'],
                                          request.json['guild_id'])
        if flag:
            return {RES: msg}
        return {RES: msg}


@hero_ns.route(f'/{HERO_DETAIL}')
class HeroDetail(Resource):
    @api.expect(detail_input)
    def post(self):
        return {RES: db_hero.get_hero_details(request.json['id'])}


@hero_ns.route(f'/{DB_ADD_HERO}')
class DBAddHero(Resource):
    add_input = api.model("DBAddHero", {'id': fields.Integer})

    @api.expect(add_input)
    def post(self):
        hero_script.generate_hero(request.json['id'])
        return {RES: "Success"}


@party_ns.route(f'/{ADD_PARTY}')
class AddParty(Resource):
    add_party_input = api.model('AddParty', {'Name': fields.String})

    @api.expect(add_party_input)
    def post(self):
        party_script.generate_party(request.json['Name'])
        return {RES: 'Success'}


@party_ns.route(f'/{DISBAND_PARTY}')
class DisbandParty(Resource):
    disband_party_input = api.model('DisbandParty', {'id': fields.Integer})

    @api.expect(disband_party_input)
    def post(self):
        flag, msg = party_script.disband_party(request.json['id'])
        if flag:
            return {RES: "Success"}
        return {RES: "Failure"}


@party_ns.route(f'/{ADD_HERO}')
class AddHero(Resource):
    add_hero_input = api.model('AddHero', {'id': fields.Integer,
                                           'party_id': fields.Integer})

    @api.expect(add_hero_input)
    def post(self):
        flag, msg = party_script.add_party_hero(request.json['party_id'],
                                                request.json['id'])
        if flag:
            return {RES: "Success"}
        return {RES: msg}


@party_ns.route(f'/{REMOVE_HERO}')
class RemoveHero(Resource):
    remove_hero_input = api.model('RemoveHero', {'id': fields.Integer,
                                                 'party_id': fields.Integer})

    @api.expect(remove_hero_input)
    def post(self):
        flag, msg = party_script.remove_party_hero(request.json['party_id'],
                                                   request.json['id'])
        if flag:
            return {RES: "Success"}
        return {RES: msg}


@party_ns.route(f'/{GET_PARTY}')
class GetParty(Resource):
    def get(self):
        return {RES: db_party.get_party()}


@party_ns.route(f'/{PARTY_DETAIL}')
class PartyDetail(Resource):
    @api.expect(detail_input)
    def post(self):
        res = db_party.get_party_details(request.json['id'])

        # Look up hero
        heroes = []
        for i in res["HeroIDs"]:
            hero_detail = db_hero.get_hero_details(i)
            heroes.append({'id': i, "name": hero_detail["Name"]})
        res["Hero"] = heroes
        del res['HeroIDs']

        return {RES: res}


if __name__ == '__main__':
    app.run()
