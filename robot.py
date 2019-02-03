from map import Map
from Point import Point


class Robot:
    def __init__(self):
        # start at location (x=0, y=0)
        self.start = Point(0, 0)
        self.track = [self.start]

        # current location
        self.loc = self.start

        self.pos = 'left'

        # the map of dirty locations
        self.map = None

    def clean(self, task: Map):
        # set the map as a class variable
        self.map = task

        # just for testing, you'll get an out of bounds exception
        # if you're not stepping through the debugger
        i = 0
        while i < 10:
            print('Robot at: ', self.loc)
            if self.map.is_dirty(self.loc):
                self.map.clean(self.loc)

            if not self.loc.is_centered():
                if self.pos == 'left':
                    self.loc = self.loc.mid_right()
                    continue
                elif self.pos == 'right':
                    self.loc = self.loc.mid_left()
                    continue

            # check if a side is dirty
            if self.map.is_dirty(self.loc.mid_left()):
                self.loc = self.loc.mid_left()   # move left
                self.map.clean(self.loc)         # and clean
                self.pos = 'left'
            elif self.map.is_dirty(self.loc.mid_right()):
                self.loc = self.loc.mid_right()  # move right
                self.map.clean(self.loc)         # and clean
                self.pos = 'right'

            # left diagonal is dirty
            elif self.map.is_dirty(self.loc.vert_left()):
                self.loc = self.loc.vert_left()
                self.map.clean(self.loc)

                self.loc = self.loc.mid_right()  # return to center

            # right diagonal is dirty
            elif self.map.is_dirty(self.loc.vert_right()):
                self.loc = self.loc.vert_right()
                self.map.clean(self.loc)

                self.loc = self.loc.mid_left()  # return to center

            # center is dirty, and diagonals aren't
            elif self.map.is_dirty(self.loc.vert_center()):
                self.loc = self.loc.vert_center()
                self.map.clean(self.loc)

            self.map.show()
            i += 1

    def show(self):
        print('Number of steps: ', len(self.track) - 1)


if __name__ == '__main__':
    home = Map(19, 19)

    test_map = [
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0]
    ]
    home.set_map(test_map)

    home.show()
    agent = Robot()
    agent.clean(home)
    agent.show()
    home.show()
