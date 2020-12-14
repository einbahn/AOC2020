def manhattan(pos1, pos2):
    x1, y1 = pos1.x, pos1.y
    x2, y2 = pos2.x, pos2.y
    return abs(x1 - x2) + abs(y1 - y2)


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ship(object):

    class Waypoint(object):
        def __init__(self):
            self.position = Position(10, 1)

        def rotate(self, direction, degree):
            if degree == 180:
                self.position.x = -self.position.x
                self.position.y = -self.position.y
            elif direction == 'L' and degree == 90 or direction == 'R' and degree == 270:
                # x, y => -y, x
                self.position.x, self.position.y = -self.position.y, self.position.x
            elif direction == 'R' and degree == 90 or direction == 'L' and degree == 270:
                # x, y = y, -x
                self.position.x, self.position.y = self.position.y, -self.position.x

        def move(self, direction, steps):
            if direction == 'N':
                self.position.y += steps
            elif direction == 'E':
                self.position.x += steps
            elif direction == 'S':
                self.position.y -= steps
            elif direction == 'W':
                self.position.x -= steps
            else:
                self.rotate(direction, steps)

    def __init__(self):
        self.position = Position(0, 0)
        self.direction = 'E'
        self.waypoint = self.Waypoint()

    def move(self, steps):
        for _ in range(steps):
            self.position.x += self.waypoint.position.x
            self.position.y += self.waypoint.position.y

    def distance_from_start(self):
        return manhattan(self.position, Position(0, 0))


if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(year=2020, day=12)
    ship = Ship()
    for i in puzzle.input_data.split('\n'):
        d = i[0]
        s = int(i[1:])
        if d == 'F':
            ship.move(s)
        else:
            ship.waypoint.move(d, s)
    print(ship.distance_from_start())
