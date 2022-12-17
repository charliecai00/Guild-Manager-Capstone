# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF
import copy
from game.object_classes.hero import Hero
from game.object_classes.party import Party
from game.object_classes.quest import Quest


class Guild:
    def __init__(self, new_id) -> None:
        self.id = new_id
        self.PARTY_ID = 0
        self.party_dic = {}
        self.hired_heros_dic = {}
        self.groups_list = []
        self.quest_list = []
        self.quest_history = []
        self.funds = 100

    def __str__(self) -> str:
        return "Funds: {} Heros: {} Parties: {} Quests: {}".format(
            self.funds,
            self.hired_heros_dic,
            self.party_dic,
            self.quest_list
        )

    def __repr__(self):
        return str(self)

    def Hire_Hero(self, new_hero: Hero) -> bool:
        if (self.funds - new_hero.cost < 0):
            print("Insufficient funds")
            return False
        elif new_hero.id in self.hired_heros_dic.keys():
            try:
                raise ValueError('The hero has already been hired in the guild')
            except ValueError as error:
                print('Caught this error: ' + repr(error))
                return False
        else:
            self.hired_heros_dic[new_hero.id] = new_hero
            self.funds -= new_hero.cost
            return True
    
    def Hire_Heros(self, new_heros) -> bool:
        for id in new_heros:
            if not self.Hire_Hero(id):
                print("hire unsuccessful")
                return False
        print("hire successful")
        return True
    
    def Fire_Hero(self, id: int) -> Hero:
        if id in self.hired_heros_dic.keys():
            hero = self.hired_heros_dic[id]
            print("before fire the hero: ", hero)
            print("party ", self.party_dic)
            self.party_dic[hero.party_id].Remove_Hero(id)
            hero.party_id = None
            print("going to fire")
            del self.hired_heros_dic[id]
            return hero
        else:
            return None

    def Add_Party(self, party_name=None) -> bool:
        """
        Add a new party to the guild without any heros
        """
        if party_name in self.party_dic.keys():
            print("Party name already exists!")
            return False
        if party_name is not None:
            self.party_dic[self.PARTY_ID] = Party(self.PARTY_ID, [], party_name)
        else:
            self.party_dic[self.PARTY_ID] = Party(self.PARTY_ID)
        self.PARTY_ID += 1
        return True

    def Assign_Hero_To_Party(self, hero_id, dest_party_id) -> bool:
        """
        Move one hero to the destination party.
        If the hero was in another party, remove the hero from previous party.
        Toggle the party_id attribute in the hero to the destination party id.
        """
        if hero_id not in self.hired_heros_dic.keys():
            print("Hero with id {} not hired by the guild".format(hero_id))
            return False
        if dest_party_id not in self.party_dic.keys():
            print("Party with id {} not in the guild. +\
                  Change the party id or add the party first".format(dest_party_id))
            return False
        hero = self.hired_heros_dic[hero_id]
        prev_party_id = hero.party_id
        if prev_party_id is None:
            hero_added = self.party_dic[dest_party_id].Add_Hero(hero)
            if hero_added:
                hero.party_id = dest_party_id
            return hero_added
        else:
            if self.party_dic[prev_party_id].Remove_Hero(hero_id):
                if self.party_dic[dest_party_id].Add_Hero(hero):
                    hero.party_id = dest_party_id
                    return True
            return False

    def check_heros(self, hero_id_lst) -> bool:
        for id in hero_id_lst:
            if id not in self.hired_heros_dic.keys():
                print('keys: ', self.hired_heros_dic.keys())
                print('the id ', type(id))
                print("Hero with id {} is not hired by the guild".format(id))
                return False
        return True

    def Assign_Heros_To_Party(self, hero_id_lst, dest_party_id) -> bool:
        print("check hero list in assign heros to party in Guild: ", hero_id_lst)
        if not self.check_heros(hero_id_lst):
            return False
        for i in range(len(hero_id_lst)):
            if not self.Assign_Hero_To_Party(hero_id_lst[i], dest_party_id):
                print("Error adding the hero with id {} to the party".format(hero_id_lst[i]))
                return False
            else:
                print("hero with id {} added to party with id {} successful".format(hero_id_lst[i], dest_party_id))
        return True

    def Add_Party_With_Heros(self, hero_lst, party_name=None) -> bool:
        """
        "Add the heros to a new party in the guild"
        1. Add a new party with the latest PARTY_ID to the guild;
        2. Update the PARTY_ID
        3. Assign the heros to this new party
        """
        print("guild ", type(hero_lst[0]))
        print("check hero id list in add_party_with_heros in Guild", hero_lst)
        print('before new party is added to the guild, the self.party_id is ', self.PARTY_ID)

        if not self.check_heros(hero_lst):
            return False
        if party_name:
            party_added = self.Add_Party(party_name)
        else:
            party_added = self.Add_Party()
        if party_added:
            print('after new party is added to the guild, the self.party_id is ', self.PARTY_ID)
            if self.Assign_Heros_To_Party(hero_lst, self.PARTY_ID - 1):
                print("after hero assigned to the party:", self.party_dic[self.PARTY_ID - 1])
                return True
            else:
                return False
        else:
            print("Adding Party Unsuccessful")
            return False

    def Disband_Party(self, partyId) -> list:
        print("check party in disband party in guild: ", self.party_dic)
        if partyId not in self.party_dic.keys():
            print("Invalid partyId")
            return None
        hero_list = self.party_dic[partyId].hero_list
        hero_list_copy = copy.deepcopy(hero_list)
        for i in range(len(hero_list)):
            hero_list[i].party_id = None
        self.party_dic[partyId] = "Disbanded"
        print("in guild, after the party {} has been disbanded: ".format(partyId), self.party_dic[partyId])
        # return the relic of this party in case the disbanded party will be used in the future
        return hero_list_copy 

    def Get_Party(self, party_id) -> Party:
        if party_id in self.party_dic.keys():
            return self.party_dic[party_id]
        else:
            return None

    def Send_Quest(self, party_name, quest: Quest) -> bool:
        party = self.Get_Party(party_name)
        report, status = party.Complete_Quest(quest)
        return status
