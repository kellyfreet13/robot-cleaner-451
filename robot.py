from map import Map
from Point import Point
from Constants import MIDDLE_TRACK


class Robot:
    def __init__(self):
        # start at location (row=0, col=0)
        self.start = Point(0, 0)
        self.track = [self.start]

        self.loc = self.start   # current location
        self.vert_dir = 1       # signifies going 'down'
        self.pos = 'left'       # on edge of 3-lane 'track'
        self.map = None         # the map of dirty locations

    # changes robots vertical direction from up to down or vice-versa
    def change_vert_direction(self):
        # python ternary operator
        self.vert_dir = 1 if self.vert_dir == -1 else -1

    # if the robot is in a center track (track of width 3)
    def is_centered(self):
        return self.loc.col in MIDDLE_TRACK

    # if the robot is on the top or bottom 'row' of the grid
    def is_on_vert_boundary(self):
        v_bounds = self.map.get_row_boundaries()
        return self.loc.row == v_bounds[0] or self.loc.row == v_bounds[1]

    # iterates over the map and cleans dirty locations
    def clean(self, task: Map):
        # set the map as a class variable
        self.map = task

        # just for testing, it will just move back and forth at the end
        i = 0
        while i < 10:
            print('\n\n--------------Map-------------')
            self.map.show()
            print('---------Robot Status---------')
            print('\tMoves: %d' % (len(self.track)-1))
            print('\tLocation: ', self.loc)
            print('\tOn vertical boundary?: ', self.is_on_vert_boundary(), '\n')

            if self.map.is_dirty(self.loc):
                self.map.clean(self.loc)

            if not self.is_centered():
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
