# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from game.object_classes.character import Character


class Enemy(Character):
    def __init__(self) -> None:
        super().__init__()
        self.type = []
