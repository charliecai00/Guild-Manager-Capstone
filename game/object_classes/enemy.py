from game.object_classes.character import Character

class Enemy(Character):
    def __init__(self) -> None:
        super().__init__()
        self.type = []
    