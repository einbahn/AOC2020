def manhattan(pos1, pos2):
    x1, y1 = pos1.x, pos1.y
    x2, y2 = pos2.x, pos2.y
    return abs(x1 - x2) + abs(y1 - y2)


class Ship(object):
    class Position(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

    direction_degree = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
    degree_direction = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}

    def __init__(self):
        self.position = self.Position(0, 0)
        self.direction = 'E'

    def move(self, direction, steps):
        if direction == 'N':
            self.position.y += steps
        elif direction == 'E':
            self.position.x += steps
        elif direction == 'S':
            self.position.y -= steps
        elif direction == 'W':
            self.position.x -= steps
        elif direction == 'L':
            curr_dgr = self.direction_degree[self.direction]
            new_dgr = (curr_dgr - steps) % 360
            self.direction = self.degree_direction[new_dgr]
        elif direction == 'R':
            curr_dgr = self.direction_degree[self.direction]
            new_dgr = (curr_dgr + steps) % 360
            self.direction = self.degree_direction[new_dgr]
        elif direction == 'F':
            self.move(self.direction, steps)

    def distance_from_start(self):
        return manhattan(self.position, self.Position(0, 0))


if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(year=2020, day=12)
    ship = Ship()
    for i in puzzle.input_data.split('\n'):
        d = i[0]
        s = int(i[1:])
        ship.move(d, s)
    print(ship.distance_from_start())
