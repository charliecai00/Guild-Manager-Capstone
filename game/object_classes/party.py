
from random import randint


class Party:
    def __init__(self, new_hero_list=[], name="Dudes") -> None:
        self.hero_list = new_hero_list
        self.name = name

    def __str__(self) -> str:
        hero_names = [h.name for h in self.hero_list]
        return "Party: {}, Heros: {}".format(self.name, hero_names)

    def __repr__(self) -> str:
        return str(self)

    def Add_Nero(self, new_hero):
        self.hero_list.append(new_hero)

    def Take_Challenge(self, challenge) -> bool:
        curr_hero = self.Get_Random_Hero()
        return curr_hero.Test_Skill(challenge.Get_Skill())

    def Get_Random_Hero(self):
        return self.hero_list[randint(0, len(self.hero_list)-1)]
