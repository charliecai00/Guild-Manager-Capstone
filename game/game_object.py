# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from game.game_math.random import RandomRange
# from game.object_classes.challenge import Challenge
from game.object_classes.quest import Quest
from game.object_classes.guild import Guild
from game.object_classes.hero import Hero
from game.object_classes.map_tile import MapTile
from game.object_classes.map import Map


class Game:
    def __init__(self):
        # setting up ID numbers
        self.GUILD_ID = 0
        self.HERO_ID = 0
        self.QUEST_ID = 0
        self.LOCALE_ID = 0
        self.guild = self.Create_Guild()  # will be modified to multiple guilds in the future
        self.map = self.Create_Map()
        self.full_hero_dic = {}
        self.full_quest_list = []

    def Create_Guild(self) -> Guild:
        ret_guild = Guild(self.GUILD_ID)
        self.GUILD_ID += 1
        return ret_guild

    def Add_Heros(self, count=10, type=None) -> int:
        for i in range(count):
            self.full_hero_dic[self.HERO_ID] = Hero(self.HERO_ID, type)
            self.HERO_ID += 1
        return self.HERO_ID

    def Find_Heros(self, hero_id) -> int:
        if hero_id not in self.full_hero_dic.keys():
            return None
        else:
            return self.full_hero_dic[hero_id]

    def Hire_Hero(self, id) -> bool:
        guild = self.guild  # will select from the function argument
        if id not in self.full_hero_dic.keys():
            print("Hero with id {} hasn't been added to the game".format(id))
            return False
        if id in guild.hired_heros_dic.keys():
            print("Hero with id {} has already been hired".format(id))
            return False
        hero = self.full_hero_dic[id]
        if isinstance(hero, Hero):
            is_hired = guild.Hire_Hero(hero)
            if is_hired:
                self.full_hero_dic[id] = "hiredByGuild"
            return is_hired
        return False

    def Fire_Hero(self, id) -> bool:
        guild = self.guild  # will select from a list of guild in the future
        if not isinstance(id, int):
            return False
        fired_hero = guild.Fire_Hero(id)
        if fired_hero:
            self.full_hero_dic[id] = fired_hero
            return True
        else:
            return False

    def Guild_Status(self) -> str:
        return str(self.guild)

    def Add_Party_With_Heros(self, hero_id_lst, party_name=None) -> bool:
        print("add party with heros function called in game")
        parsed_hero_id_lst = list(map(int, hero_id_lst))
        # for i in range(len(hero_id_lst)):
        #     parsed_hero_id_lst[i] = int(hero_id_lst[i])
        print("check hero id lst in add party with heros in Game:", hero_id_lst)
        print("game_obj ", type(parsed_hero_id_lst[0]))

        guild = self.guild  # will select from a list of guild in the future
        if party_name:
            return guild.Add_Party_With_Heros(parsed_hero_id_lst, party_name)
        else:
            return guild.Add_Party_With_Heros(parsed_hero_id_lst)
    
    def Assign_Heros_To_Party(self, hero_lst, party_id):
        guild = self.guild  # will select from a list of guild in the future
        guild.Assign_Heros_To_Party(hero_lst, party_id)
        return True

    def Disband_Party(self, party_id) -> bool:
        guild = self.guild  # will be selected from the funtion argument
        return guild.Disband_Party(party_id) is not None

    def Get_Quest(self) -> Quest:
        new_quest = Quest()
        self.full_quest_list.append(new_quest)
        return new_quest

    def Find_Quest(self, name) -> Quest:
        for quest in self.full_quest_list:
            if quest.name == name:
                return quest
        return None

    def Do_Quest(self, quest_name, party_name) -> bool:
        if self.Find_Quest(quest_name) is None:
            return False
        return self.guild.Send_Quest(party_name, self.Find_Quest(quest_name))
    
    def Create_Map(self) -> Map:
        locales = Map()
        coordinates = []
        while len(coordinates) < 5:
            coords = (RandomRange(0, 10), RandomRange(0, 10))
            if coords in coordinates:
                continue
            coordinates.append(coords)
            locales.locations[coords] = MapTile(self.LOCALE_ID)
            self.LOCALE_ID += 1
        return locales
    
    # def Get_Location(self, name) -> MapTile:
    #     for locale in self.map:
    #         if locale[1].name == name:
    #             return locale
    #     return None
