
from object_classes.guild import Guild

class Game:
    def __init__(self):
        self.guild = Guild()

    def Get_Heros(self):
        return self.guild.Find_Heros()

    