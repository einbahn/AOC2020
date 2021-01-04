import re
from aocd.models import Puzzle
from collections import defaultdict


def solve(data):
    invalid = []
    rules = defaultdict(list)
    rules, _, nearby = data.split('\n\n')
    nearby = nearby[16:].split('\n')
    pat = re.compile(r'([\w]+):\s(\d+)-(\d+) or (\d+)-(\d+)')
    for n in nearby:
        for value in n.split(','):
            v = int(value)
            for r in rules.split('\n'):
                p = [int(m) for m in pat.findall(r)[0][1:]]
                if p[0] <= v <= p[1] or p[2] <= v <= p[3]:
                    break
            else:
                invalid.append(v)
    return sum(invalid)


puzzle = Puzzle(year=2020, day=16)
ans_part_one = solve(puzzle.input_data)
print(solve(puzzle.input_data))
