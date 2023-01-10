# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

class Challenge:
    def __init__(self, skill=None, new_type='Random') -> None:
        self.test_skill = skill
        self.name = 0   # change this later
        self.type = new_type
        self.success_message = ""
        self.fail_message = ""

    def Get_Skill(self) -> str:
        return self.test_skill

    def Set_Skill(self, new_skill):
        self.test_skill = new_skill

    def __repr__(self):
        return "Name: {} Skill: {}".format(self.name, self.test_skill)
