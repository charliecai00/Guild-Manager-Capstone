# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

# import game.object_classes.static_consts as sc


class MapTile:
    def __init__(self, id) -> None:
        self.terrain = 'Fields'
        self.paths = []
        self.name = str(id)

    def __str__(self) -> str:
        s = "Location: {}, Terrain: {}\n".format(
            self.name,
            self.terrain
        )
        return s

    def __repr__(self) -> str:
        return str(self)
