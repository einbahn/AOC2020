# def make_window(x, y, length, width):
#     pos0 = x - 1, y - 1
#     pos1 = x - 1, y
#     pos2 = x - 1, y + 1
#     pos3 = x, y - 1
#     pos4 = x, y + 1
#     pos5 = x + 1, y - 1
#     pos6 = x + 1, y
#     pos7 = x + 1, y + 1
#
#     # top left
#     if x == 0 and y == 0:
#         return pos4, pos6, pos7
#
#     # top right
#     elif x == 0 and y == width - 1:
#         return pos3, pos5, pos6
#
#     # bottom left
#     elif x == length - 1 and y == 0:
#         return pos1, pos2, pos4
#
#     # bottom right
#     elif x == length - 1 and y == width - 1:
#         return pos0, pos1, pos3
#
#     # top
#     elif x == 0 and y != 0:
#         return pos3, pos4, pos5, pos6, pos7
#
#     # left
#     elif x != 0 and y == 0:
#         return pos1, pos2, pos4, pos6, pos7
#
#     # right
#     elif x != 0 and y == width - 1:
#         return pos0, pos1, pos3, pos5, pos6
#
#     # bottom
#     elif x == length - 1 and y != 0:
#         return pos0, pos1, pos2, pos3, pos4
#
#     # mid:
#     else:
#         return pos0, pos1, pos2, pos3, pos4, pos5, pos6, pos7

def make_window(x, y, length, width, map):
    pos0 = lambda x, y: (x - 1, y - 1)
    pos1 = lambda x, y: (x - 1, y)
    pos2 = lambda x, y: (x - 1, y + 1)
    pos3 = lambda x, y: (x, y - 1)
    pos4 = lambda x, y: (x, y + 1)
    pos5 = lambda x, y: (x + 1, y - 1)
    pos6 = lambda x, y: (x + 1, y)
    pos7 = lambda x, y: (x + 1, y + 1)

    def within_bounds(*coords):
        x, y = coords
        return 0 <= x <= length - 1 and 0 <= y <= width - 1

    def increment(*positions):
        occupied = 0
        for pos in positions:
            nx, ny = pos(x, y)
            while within_bounds(pos(nx, ny)[0], pos(nx, ny)[1]) and map[nx][ny] == '.':
                nx, ny = pos(nx, ny)
            if map[nx][ny] == '#':
                occupied += 1
        return occupied

    # top left
    if x == 0 and y == 0:
        return increment(pos4, pos6, pos7)

    # top right
    elif x == 0 and y == width - 1:
        return increment(pos3, pos5, pos6)

    # bottom left
    elif x == length - 1 and y == 0:
        return increment(pos1, pos2, pos4)

    # bottom right
    elif x == length - 1 and y == width - 1:
        return increment(pos0, pos1, pos3)

    # top
    elif x == 0 and y != 0:
        return increment(pos3, pos4, pos5, pos6, pos7)

    # left
    elif x != 0 and y == 0:
        return increment(pos1, pos2, pos4, pos6, pos7)

    # right
    elif x != 0 and y == width - 1:
        return increment(pos0, pos1, pos3, pos5, pos6)

    # bottom
    elif x == length - 1 and y != 0:
        return increment(pos0, pos1, pos2, pos3, pos4)

    # mid:
    else:
        return increment(pos0, pos1, pos2, pos3, pos4, pos5, pos6, pos7)


def part_one(data):
    from copy import deepcopy
    seat_map = [[j for j in i] for i in data.split('\n')]
    length = len(seat_map)
    wid = len(seat_map[0])
    sm_read = deepcopy(seat_map)
    sm_write = deepcopy(seat_map)
    it = 0
    while True:
        it += 1
        changes = 0
        for i, d in enumerate(sm_read):
            for j, s in enumerate(d):
                if s == '.':
                    continue
                occupied = make_window(i, j, length, wid, sm_read)
                if sm_read[i][j] == 'L' and not occupied:
                    sm_write[i][j] = '#'
                    changes += 1
                elif sm_read[i][j] == '#' and occupied >= 5:
                    sm_write[i][j] = 'L'
                    changes += 1
        if not changes:
            break
        sm_read = deepcopy(sm_write)
        sm_write = deepcopy(sm_write)
    return sum(x.count('#') for x in sm_write)


if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(year=2020, day=11)
    print(part_one(puzzle.input_data))
