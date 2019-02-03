from map import Map
from Point import Point


class Robot:
    def __init__(self):
        # start at location (x=0, y=0)
        self.start = Point(0, 0)
        self.track = [self.start]

        # current location
        self.loc = self.start

        print(self.start)

        # last path will be straight up/down column 18
        self.middle_track = [1, 4, 7, 10, 13, 16]

        # the map of dirty locations
        self.map = None

    def is_centered(self):
        return self.loc.col in self.middle_track

    def clean(self, task: Map):
        # set the map as a class variable
        self.map = task

        # check if a side is dirty
        if self.map.is_dirty(self.loc.mid_left()):
            self.loc = self.loc.mid_left()   # move left
            self.map.clean(self.loc)         # and clean
        elif self.map.is_dirty(self.loc.mid_right()):
            self.loc = self.loc.mid_right()  # move right
            self.map.clean(self.loc)         # and clean

        # special case
        #   this way we won't have to do unnecessary backtracking in the future
        # - 0 -
        # 1 0 1
        if (
            self.is_centered() and
            self.map.is_dirty(self.loc.vert_left()) and
            self.map.is_dirty(self.loc.vert_right())
        ):
            # move lower left and clean
            self.loc = self.loc.vert_left()
            self.map.clean(self.loc)

            # move two right (old lower right perspective)
            self.loc = self.loc.mid_right()
            self.loc = self.loc.mid_right()
            self.map.clean(self.loc)  # now clean it






    def show(self):
        print('Number of steps: ', len(self.track) - 1)


if __name__ == '__main__':
    home = Map(19, 19)
    home.show()
    agent = Robot()
    agent.clean(home)
    agent.show()
    home.show()
