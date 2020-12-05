from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=3)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def part_a(data, down=1, right=3):
    tree_map = [i for i in data.split('\n')]
    map_width = len(tree_map[0])
    row = col = count = 0
    for i in range(1, len(tree_map)):
        row = row + down
        col = col + right
        if col >= map_width:
            col -= map_width
        if tree_map[row][col] == '#':
            count += 1
    return count


def part_b(data, slopes):
    from math import prod
    tree_map = [i for i in data.split('\n')]
    map_width = len(tree_map[0])
    res = []
    for s in slopes:
        row = col = count = 0
        right, down = s
        for i in range(1, len(tree_map), down):
            row += down
            col += right
            if col >= map_width:
                col -= map_width
            if tree_map[row][col] == '#':
                count += 1
        res.append(count)
    return prod(res)

