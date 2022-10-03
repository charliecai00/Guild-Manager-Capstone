from game.object_classes.character import Character

class Enemy(Character):
    def __init__(self) -> None:
        Character.__init__(self)
        self.type = []
    