from Point import Point

if __name__ == '__main__':

    # let's move like so

    # x - -         - - -
    # - - -   =>    - x -
    # - - -         - - -
    a = Point(0, 0)
    a = a.vert_right()
    assert a == Point(1, 1)

    # x - -         - x -
    # - - -   =>    - - -
    # - - -         - - -
    b = Point(0, 0)
    b = b.mid_right()
    assert b == Point(0, 1)

    # x - -         - - -
    # - - -   =>    x - -
    # - - -         - - -
    c = Point(0, 0)
    c = c.vert_center()
    assert c == Point(1, 0)

    # - - -         - - -
    # - - -   =>    - x -
    # - x -         - - -
    d = Point(2, 1)
    d.change_vert_direction()
    d = d.vert_center()
    assert d == Point(1, 1)

    # - - -         - - -
    # - - -   =>    - - x
    # - x -         - - -
    e = Point(2, 1)
    e.change_vert_direction()
    e = e.vert_right()
    assert e == Point(1, 2)

    # - - -         - - -
    # - - -   =>    x - -
    # - x -         - - -
    f = Point(2, 1)
    f.change_vert_direction()
    f = f.vert_left()
    assert f == Point(1, 0)

    # x - -         - - -          - - x
    # - - -   =>    - x -    =>    - - -
    # - - -         - - -          - - -
    g = Point(0, 0)
    g = g.vert_right()
    assert g == Point(1, 1)
    g.change_vert_direction()
    g = g.vert_right()
    assert g == Point(0, 2)
