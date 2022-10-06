
from game.object_classes.character import Character

class Adventurer(Character):
    def __init__(self) -> None:
        super().__init__()
        self.items = []
    