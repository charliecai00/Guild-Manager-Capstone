# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from flask import Flask, request
from flask_restx import Resource, Api, fields, Namespace
from flask_cors import CORS

import game.guild_script as guild_script
import game.hero_script as hero_script
import game.party_script as party_script
import game.quest_script as quest_script
import db.db_connect as dbc
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
DEVELOPER_NS = 'Developer'
# Create namespaces
guild_ns = Namespace(GUILD_NS, 'Guild APIs')
quest_ns = Namespace(QUEST_NS, 'Quest APIs')
hero_ns = Namespace(HERO_NS, 'Hero APIs')
party_ns = Namespace(PARTY_NS, 'Party APIs')
developer_ns = Namespace(DEVELOPER_NS, 'Developer API')
api.add_namespace(guild_ns)
api.add_namespace(quest_ns)
api.add_namespace(hero_ns)
api.add_namespace(party_ns)
api.add_namespace(developer_ns)
# Define API routes
# Create guild routes
CREATE = 'Create'
RELOAD = 'Reload'
GUILD_DETAIL = 'Guild_Detail'
CREATE_PATH = f'{GUILD_NS}/{CREATE}'
RELOAD_PATH = f'{GUILD_NS}/{RELOAD}'
GUILD_DETAIL_PATH = f'{GUILD_NS}/{GUILD_DETAIL}'
# Create quest routes
UNSOLD_QUEST = 'Unsold_Quest'
BUY = 'Buy'
SELL = 'Sell'
START = 'Start'
QUEST_DETAIL = 'Quest_Detail'
UNSOLD_QUEST_PATH = f'{QUEST_NS}/{UNSOLD_QUEST}'
BUY_PATH = f'{QUEST_NS}/{BUY}'
SELL_PATH = f'{QUEST_NS}/{SELL}'
START_PATH = f'{QUEST_NS}/{START}'
QUEST_DETAIL_PATH = f'{QUEST_NS}/{QUEST_DETAIL}'
# Create hero routes
HIRE = 'Hire'
FIRE = 'Fire'
UNEMPLOYED = 'Unemployed'
HEAL = 'Heal'
HERO_DETAIL = 'Hero_Detail'
HERO_NOT_IN_PARTY = 'Hero_Not_In_Party'
HERO_OPTIONS = 'Hero_Options'
HIRE_PATH = f'{HERO_NS}/{HIRE}'
FIRE_PATH = f'{HERO_NS}/{FIRE}'
UNEMPLOYED_PATH = f'{HERO_NS}/{UNEMPLOYED}'
HEAL_PATH = f'{HERO_NS}/{HEAL}'
HERO_DETAIL_PATH = f'{HERO_NS}/{HERO_DETAIL}'
HERO_NOT_IN_PARTY_PATH = f'{HERO_NS}/{HERO_NOT_IN_PARTY}'
HERO_OPTIONS_PATH = f'{HERO_NS}/{HERO_OPTIONS}'
# Create party routes
ADD_HERO = 'Add_Hero'
REMOVE_HERO = 'Remove_Hero'
ADD_PARTY = 'Add_Party'
DISBAND_PARTY = 'Disband_Party'
PARTY_DETAIL = 'Party_Detail'
ADD_HERO_PATH = f'{PARTY_NS}/{ADD_HERO}'
REMOVE_HERO_PATH = f'{PARTY_NS}/{REMOVE_HERO}'
ADD_PARTY_PATH = f'{PARTY_NS}/{ADD_PARTY}'
DISBAND_PARTY_PATH = f'{PARTY_NS}/{DISBAND_PARTY}'
PARTY_DETAIL_PATH = f'{PARTY_NS}/{PARTY_DETAIL}'
# Create developer endpoint
RESET_DB = 'Reset_DB'
RESET_DB_PATH = f'{DEVELOPER_NS}/{RESET_DB}'

# Define Marco
RES = 'Response'

# API models
model_id = api.model('Input: id', {'id': fields.Integer})
model_id_guildid = api.model('Input: id & guildid',
                             {'id': fields.Integer,
                              'guild_id': fields.Integer})
model_id_partyid = api.model('Input: id & partyid',
                             {'id': fields.Integer,
                              'party_id': fields.Integer})


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
    @api.expect(model_id)
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
    @api.expect(model_id_guildid)
    def post(self):
        flag, msg = quest_script.buy_quest(request.json['id'],
                                           request.json['guild_id'])
        if flag:
            return {RES: "Success"}
        return {RES: msg}


@quest_ns.route(f'/{SELL}')
class Sell(Resource):
    @api.expect(model_id_guildid)
    def post(self):
        flag, msg = quest_script.sell_quest(request.json['id'],
                                            request.json['guild_id'])
        if flag:
            return {RES: "Success"}
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
    @api.expect(model_id)
    def post(self):
        return {RES: db_quest.get_quest_details(request.json['id'])}


@hero_ns.route(f'/{HIRE}')
class Hire(Resource):
    @api.expect(model_id_guildid)
    def post(self):
        flag, msg = guild_script.hire_guild_hero(request.json['guild_id'],
                                                 request.json['id'])
        if flag:
            return {RES: "Success"}
        return {RES: msg}


@hero_ns.route(f'/{FIRE}')
class Fire(Resource):
    @api.expect(model_id_guildid)
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
    @api.expect(model_id_guildid)
    def post(self):
        flag, msg = hero_script.heal_hero(request.json['id'],
                                          request.json['guild_id'])
        if flag:
            return {RES: 'Success'}
        return {RES: msg}


@hero_ns.route(f'/{HERO_DETAIL}')
class HeroDetail(Resource):
    @api.expect(model_id)
    def post(self):
        return {RES: db_hero.get_hero_details(request.json['id'])}


@hero_ns.route(f'/{HERO_NOT_IN_PARTY}')
class HeroNotInParty(Resource):
    @api.expect(model_id)
    def post(self):
        guild_detail = db_guild.get_guild_details(request.json['id'])

        res = []
        for i in guild_detail['HeroIDs']:
            hero_detail = db_hero.get_hero_details(i)
            if not hero_detail["InParty?"]:
                res.append(hero_detail)

        return {RES: res}


@hero_ns.route(f'/{HERO_OPTIONS}')
class HeroOptions(Resource):
    def get(self):
        res = {"Fire": FIRE_PATH,
               "Heal": HEAL_PATH}
        return {RES: res}


@party_ns.route(f'/{ADD_PARTY}')
class AddParty(Resource):
    add_party_input = api.model('AddParty',
                                {'Name': fields.String,
                                 'guild_id': fields.Integer})

    @api.expect(add_party_input)
    def post(self):
        party_script.generate_party(request.json['Name'])
        flag, msg = guild_script.add_guild_party(request.json['guild_id'],
                                                 db_party.fetch_curr_id())
        if flag:
            return {RES: "Success"}
        return {RES: msg}


@party_ns.route(f'/{DISBAND_PARTY}')
class DisbandParty(Resource):
    @api.expect(model_id_partyid)
    def post(self):
        flag, msg = guild_script.remove_guild_party(request.json['id'],
                                                    request.json['party_id'])
        if flag:
            return {RES: "Success"}
        return {RES: msg}


@party_ns.route(f'/{ADD_HERO}')
class AddHero(Resource):
    @api.expect(model_id_partyid)
    def post(self):
        flag, msg = party_script.add_party_hero(request.json['party_id'],
                                                request.json['id'])
        if flag:
            return {RES: "Success"}
        return {RES: msg}


@party_ns.route(f'/{REMOVE_HERO}')
class RemoveHero(Resource):
    @api.expect(model_id_partyid)
    def post(self):
        flag, msg = party_script.remove_party_hero(request.json['party_id'],
                                                   request.json['id'])
        if flag:
            return {RES: "Success"}
        return {RES: msg}


@party_ns.route(f'/{PARTY_DETAIL}')
class PartyDetail(Resource):
    @api.expect(model_id)
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


@developer_ns.route(f'/{RESET_DB}')
class ResetDB(Resource):
    def get(self):
        """
        Delete all DB items & Populate 200 heros and quests
        """
        dbc.del_many(db_guild.GUILD_COLLECT, {})
        dbc.del_many(db_hero.HERO_COLLECT, {})
        dbc.del_many(db_party.PARTY_COLLECT, {})
        dbc.del_many(db_quest.QUEST_COLLECT, {})

        for i in range(200):
            hero_script.generate_hero()
            quest_script.generate_quest()


if __name__ == '__main__':
    app.run()
