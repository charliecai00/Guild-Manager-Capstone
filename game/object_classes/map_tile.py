import game.object_classes.static_consts as sc

class MapTile:
    def __init__(self) -> None:
        self.terrain = 'Fields'
        self.paths = []
        self.name = str(sc.LOCALE_ID)
        sc.LOCALE_ID += 1

