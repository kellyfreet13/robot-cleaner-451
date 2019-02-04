import random
import numpy as np

from Point import Point


class Map:
    def __init__(self, width, height):
        self.dirty = [[random.randint(0, 1) for i in range(height)] for j in range(width)]

    def show(self):
        print(np.matrix(self.dirty))

    # returns whether an (row, col) coordinate is dirty
    def is_dirty(self, point: Point):
        return self.dirty[point.row][point.col]

    def clean(self, to_clean: Point):
        self.dirty[to_clean.row][to_clean.col] = 0

    def set_map(self, arr):
        self.dirty = arr

    # assumes a square map
    def get_map_size(self):
        return len(self.dirty) * len(self.dirty[0])

    def get_row_boundaries(self):
        return 0, len(self.dirty)-1


if __name__ == '__main__':
    test = Map(19, 19)
    test.show()
    print(test.is_dirty(0, 0))
    print(test.is_dirty(1, 1))

