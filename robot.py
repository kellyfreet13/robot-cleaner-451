from map import Map


class Robot:
    def __init__(self):
        self.start = (0, 0)
        self.track = [self.start]

    # def clean(self, task: Map):

    def show(self):
        print('Number of steps: ', len(self.track) - 1)


if __name__ == '__main__':
    home = Map(19, 19)
    home.show()
    agent = Robot()
    # agent.clean(home)
    agent.show()
    home.show()
