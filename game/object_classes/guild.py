# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from game.object_classes.hero import Hero
from game.object_classes.party import Party
from game.object_classes.quest import Quest


class Guild:
    def __init__(self, new_id) -> None:
        self.id = new_id
        self.PARTY_ID = 0
        self.hired_heros_list = []
        self.groups_list = []
        self.quest_list = []
        self.quest_history = []
        self.party_list = []
        self.funds = 100

    def __str__(self) -> str:
        return "Funds: {} Heros: {} Parties: {} Quests: {}".format(
            self.funds,
            self.hired_heros_list,
            self.party_list,
            self.quest_list
        )

    def __repr__(self):
        return str(self)

    def Hire_Hero(self, new_hero: Hero) -> bool:
        if (self.funds - new_hero.cost < 0):
            return False
        else:
            self.hired_heros_list.append(new_hero)
            self.funds -= new_hero.cost
            return True

    def Fire_Hero(self, del_hero: Hero) -> bool:
        try:
            self.hired_heros_list.remove(del_hero)
        except ValueError:
            return False
        return True

    def Form_Party(self, hero_list, name=None) -> None:
        if name is not None:
            self.party_list.append(Party(self.PARTY_ID, hero_list, name))
        else:
            self.party_list.append(Party(self.PARTY_ID, hero_list))
        self.PARTY_ID += 1

    def Disband_Party(self, name) -> bool:
        remove_ind = None
        for i in range(len(self.party_list)):
            if self.party_list[i].name == name:
                remove_ind = i
        if remove_ind != None:
            self.party_list.pop(remove_ind)
            # call disband function
            return True
        else:
            return False

    def Get_Party(self, name) -> Party:
        for party in self.party_list:
            if party.name == name:
                return party

    def Send_Quest(self, party_name, quest: Quest) -> bool:
        party = self.Get_Party(party_name)
        report, status = party.Complete_Quest(quest)
        return status
