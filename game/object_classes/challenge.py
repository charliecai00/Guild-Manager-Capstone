
import game.object_classes.static_consts as sc


class Challenge:
    def __init__(self, skill=None) -> None:
        self.test_skill = skill
        self.name = str(sc.QUEST_ID)
        sc.QUEST_ID += 1

    def Get_Skill(self):
        return self.test_skill

    def Set_Skill(self, new_skill):
        self.test_skill = new_skill

    def __repr__(self) -> str:
        return "Name: {}, Skill: {}".format(self.name, self.test_skill)
