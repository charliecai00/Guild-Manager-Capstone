
from random import randint


class Party:
    def __init__(self, new_hero_list = []) -> None:
        self.hero_list = new_hero_list
        self.name = "The Fellowship of Heros"
    
    def __str__(self) -> str:
        return "Party: {}, Heros: {}".format(self.name, self.hero_list)

    def Add_Nero(self, new_hero):
        self.hero_list.append(new_hero)

    def Take_Challenge(self, challenge):
        curr_hero = self.Get_Random_Hero()
        return curr_hero.Test_Skill(challenge.Get_Skill())

    def Get_Random_Hero(self):
        return self.hero_list[randint(0,len(self.hero_list)-1)]