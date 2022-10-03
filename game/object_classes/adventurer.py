
from game.object_classes.character import Character

class Adventurer(Character):
    def __init__(self) -> None:
        Character.__init__(self)
        self.items = []
    