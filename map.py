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
        self.dirty[to_clean.row][to_clean.col]


if __name__ == '__main__':
    test = Map(19, 19)
    test.show()
    print(test.is_dirty(0, 0))
    print(test.is_dirty(1, 1))

