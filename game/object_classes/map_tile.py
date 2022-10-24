import game.object_classes.static_consts as sc

class MapTile:
    def __init__(self) -> None:
        self.terrain = 'Fields'
        self.paths = []
        self.name = str(sc.LOCALE_ID)
        sc.LOCALE_ID += 1

    def __str__(self) -> str:
        s = "Location: {}, Terrain: {}\n".format(
            self.name,
            self.terrain
        )
        return s
    
    def __repr__(self) -> str:
        return str(self)
