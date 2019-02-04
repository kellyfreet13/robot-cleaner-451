from map import Map
from Point import Point


class Robot:
    def __init__(self):
        # start at location (row=0, col=0)
        self.start = Point(0, 0)
        self.track = [self.start]

        self.loc = self.start   # current location
        self.vert_dir = 1       # signifies going 'down'
        self.pos = 'left'       # on edge of 3-lane 'track'
        self.map = None         # the map of dirty locations

    def change_vert_direction(self):
        # python ternary operator
        self.vert_dir = 1 if self.vert_dir == -1 else -1

    def clean(self, task: Map):
        # set the map as a class variable
        self.map = task

        # just for testing, it will just move back and forth at the end
        i = 0
        while i < 10:
            self.map.show()
            print('Robot at: ', self.loc, '\n')
            if self.map.is_dirty(self.loc):
                self.map.clean(self.loc)

            if not self.loc.is_centered():
                if self.pos == 'left':
                    self.loc = self.loc.mid_right()
                    self.track.append(self.loc)
                    continue
                elif self.pos == 'right':
                    self.loc = self.loc.mid_left()
                    self.track.append(self.loc)
                    continue

            # check if a side is dirty
            if self.map.is_dirty(self.loc.mid_left()):
                self.loc = self.loc.mid_left()   # move left
                self.map.clean(self.loc)         # and clean
                self.track.append(self.loc)      # update track
                self.pos = 'left'
            elif self.map.is_dirty(self.loc.mid_right()):
                self.loc = self.loc.mid_right()  # move right
                self.map.clean(self.loc)         # and clean
                self.track.append(self.loc)      # update track
                self.pos = 'right'

            # left diagonal is dirty
            elif self.map.is_dirty(self.loc.vert_left(self.vert_dir)):
                self.loc = self.loc.vert_left(self.vert_dir)
                self.track.append(self.loc)
                self.map.clean(self.loc)

                self.loc = self.loc.mid_right()  # return to center
                self.track.append(self.loc)

            # right diagonal is dirty
            elif self.map.is_dirty(self.loc.vert_right(self.vert_dir)):
                self.loc = self.loc.vert_right(self.vert_dir)
                self.track.append(self.loc)
                self.map.clean(self.loc)

                self.loc = self.loc.mid_left()  # return to center
                self.track.append(self.loc)

            # center is dirty, and diagonals aren't
            elif self.map.is_dirty(self.loc.vert_center(self.vert_dir)):
                self.loc = self.loc.vert_center(self.vert_dir)
                self.map.clean(self.loc)
                self.track.append(self.loc)

            i += 1
            print('Robot has made %d moves' % len(self.track))

    def show(self):
        print('Number of steps: ', len(self.track) - 1)

        # requirement of the assignment
        assert len(self.track) < self.map.get_map_size()


if __name__ == '__main__':
    home = Map(19, 19)

    test_map = [
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0]
    ]
    home.set_map(test_map)
    #home.show()
    agent = Robot()
    agent.clean(home)
    agent.show()
    home.show()
