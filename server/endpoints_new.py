# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from flask import Flask, request
from flask_restx import Resource, Api, fields, Namespace
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)

#Define namespaces
GUILD_NS = 'Guild'
QUEST_NS = 'Quest'
HERO_NS = 'Hero'
PARTY_NS = 'Party'
#Create namespaces
guild_ns = Namespace(GUILD_NS, 'Guild APIs')
quest_ns = Namespace(QUEST_NS, 'Quest API')
hero_ns = Namespace(HERO_NS, 'Hero API')
party_ns = Namespace(PARTY_NS, 'Party API')
api.add_namespace(guild_ns)
api.add_namespace(quest_ns)
api.add_namespace(hero_ns)
api.add_namespace(party_ns)
#Define API routes
CREATE = 'Create'
RELOAD = 'Reload'
UNSOLD_QUEST = 'Unsold Quest'
BUY = 'Buy'
SELL = 'Sell'
START = 'Start'
SELECT_PARTY = 'Select Party'
HIRE = 'Hire'
FIRE = 'Fire'
UNEMPLOYED = 'Unemployed'
HEAL = 'Heal'
ADD_HERO = 'Add Hero'
REMOVE_HERO = 'Remove Hero'
ADD_PARTY = 'Add Party'
DELETE_PARTY = 'Delete Party'
#Create guild routes
CREATE_PATH = f'{GUILD_NS}/{CREATE}'
RELOAD_PATH = f'{GUILD_NS}/{RELOAD}'
#Create quest routes
UNSOLD_QUEST_PATH = f'{QUEST_NS}/{UNSOLD_QUEST}'
BUY_PATH = f'{QUEST_NS}/{BUY}'
SELL_PATH = f'{QUEST_NS}/{SELL}'
START_PATH = f'{QUEST_NS}/{START}'
SELECT_PARTY_PATH = f'{QUEST_NS}/{SELECT_PARTY}'
#Create hero routes
HIRE_PATH = f'{HERO_NS}/{HIRE}'
FIRE_PATH = f'{HERO_NS}/{FIRE}'
UNEMPLOYED_PATH = f'{HERO_NS}/{UNEMPLOYED}'
HEAL_PATH = f'{HERO_NS}/{HEAL}'
#Create party routes
ADD_HERO_PATH = f'{PARTY_NS}/{ADD_HERO}'
REMOVE_HERO_PATH = f'{PARTY_NS}/{REMOVE_HERO}'
ADD_PARTY_PATH = f'{PARTY_NS}/{ADD_PARTY}'
DELETE_PARTY_PATH = f'{PARTY_NS}/{DELETE_PARTY}'
#Create main menu route
MAIN_MENU = '/main_menu'

@api.route(MAIN_MENU)
class MainMenu(Resource):
    """
    This will deliver our main menu.
    """
    def get(self):
        """
        Gets the main game menu.
        """
        return {'Title': 'Main Menu',
                'Default': 0,
                'Choices': {
                    '1': {'text': 'ADD_PARTY_WITH_HEROS',
                          'url': '/add_party_with_heros',
                          'method': 'post'}
                }}

guild_ns.route(CREATE_PATH)
class Create(Resource):
    