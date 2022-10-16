
from game.object_classes.map_tile import MapTile


class Map:
    def __init__(self, size_x=100, size_y=100) -> None:
        self.map = [[] * size_x] * size_y
        for y in range(size_y):
            for x in range(size_x):
                self.map[y][x] = self.Pop_Coord()

    def Pop_Coord(self):
        return MapTile()
