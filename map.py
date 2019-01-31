import random
import numpy as np


class Map:
    def __init__(self, width, height):
        self.dirty = [[random.randint(0, 1) for i in range(height)] for j in range(width)]

    def show(self):
        print(np.matrix(self.dirty))

    # returns whether an (x, y) coordinate is dirty
    def is_dirty(self, x, y):
        return self.dirty[x][y]


if __name__ == '__main__':
    test = Map(19, 19)
    test.show()
    print(test.is_dirty(0, 0))
    print(test.is_dirty(1, 1))

