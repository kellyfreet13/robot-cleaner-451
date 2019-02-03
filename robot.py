from map import Map
from Point import Point

class Robot:
    def __init__(self):
        # start at location (x=0, y=0)
        self.start = Point(0, 0)
        self.track = [self.start]

        print(self.start)

        # last path will be straight up/down column 18
        self.middle_track = [1, 4, 7, 10, 13, 16]

        # the map of dirty locations
        self.map = None

    def clean(self, task: Map):
        # set the map as a class variable
        self.map = task

        # implementation to follow, just boilerplate at the moment

    def show(self):
        print('Number of steps: ', len(self.track) - 1)


if __name__ == '__main__':
    home = Map(19, 19)
    home.show()
    agent = Robot()
    agent.clean(home)
    agent.show()
    home.show()
