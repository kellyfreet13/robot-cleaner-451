from Constants import MIDDLE_TRACK


class Point:
    def __init__(self, row_init, col_init):
        self.row = row_init
        self.col = col_init
        self.vert_dir = 1  # this represent going 'down' initially
        # (0, 0) (0, 1)
        # (1, 0) (1, 1)
        # (2, 0) (2, 1)

    def is_centered(self):
        return self.col in MIDDLE_TRACK

    def change_vert_direction(self):
        # python ternary operator
        self.vert_dir = 1 if self.vert_dir == -1 else -1

    def mid_left(self):
        return Point(self.row, self.col-1)

    def mid_right(self):
        return Point(self.row, self.col+1)

    def vert_left(self):
        return Point(self.row+self.vert_dir, self.col-1)

    def vert_center(self):
        return Point(self.row+self.vert_dir, self.col)

    def vert_right(self):
        return Point(self.row+self.vert_dir, self.col+1)

    def __repr__(self):
        return ''.join(["[", str(self.row), ",", str(self.col), "]"])

    # equality checker
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
