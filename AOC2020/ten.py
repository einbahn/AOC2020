from aocd.models import Puzzle
from collections import deque, defaultdict
from math import prod


def powerset(iterable):
    from itertools import chain, combinations
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def sum_jolt_diff(data):
    p = 0
    diff = defaultdict(list)
    adapters = deque()
    for j in sorted([int(i) for i in data.split('\n')]):
        adapters.append(j)
    adapters.append(max(adapters) + 3)
    while adapters:
        c = adapters.popleft()
        if c - p > 3:
            break
        d = c - p
        diff[d].append(c)
        p = c
    return prod([len(diff[k]) for k in diff.keys()])


def part_two(data):
    sorted_data = sorted([int(i) for i in data.split('\n')])
    sorted_data.append(max(sorted_data) + 3)
    sorted_data.insert(0, 0)
    sublist = []
    i = 0
    while i < len(sorted_data):
        j = i
        k = i + 1
        sl = [sorted_data[i]]
        while k < len(sorted_data) and sorted_data[k] - sorted_data[j] < 3:
            sl.append(sorted_data[k])
            k += 1
            j += 1
        i = k
        sublist.append(sl)
    count = []
    for sl in sublist:
        if sl[-1] - sl[0] > 3:
            count.append(len(list(powerset(sl[1:-1]))) - 1)
        else:
            count.append(len(list(powerset(sl[1:-1]))))
    return prod(count)


if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=10)
    print(sum_jolt_diff(puzzle.input_data))
    print(part_two(puzzle.input_data))
