import re
from aocd.models import Puzzle
from collections import defaultdict
import numpy as np
from math import prod 

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


def solve_two(data):
    rules, mine, nearby = data.split('\n\n')
    mine = [int(m) for m in mine[13:].split(',')]
    nearby = nearby[16:].split('\n')
    valid = []

    def process_rules():
        rule_set = defaultdict(list)
        pat = re.compile(r'^([\w\s]+):\s(\d+)-(\d+) or (\d+)-(\d+)')
        for r in rules.split('\n'):
            p = pat.findall(r)[0]
            lims = [int(l) for l in p[1:]]
            rule_set[p[0]] = lims
        return rule_set
    rule_set = process_rules()

    def test_lims(n, limits):
        return limits[0] <= n <= limits[1] or limits[2] <= n <= limits[3]
    
    def find_field(col, field_names): 
        for n in col:
            for field_name, lims in rule_set.items():
                if not test_lims(n, lims):
                    field_names.remove(field_name)
        return field_names

    def process_position(pos):
        processed = set()
        result = []
        items = sorted(pos.items(), key=lambda x: len(x[1]))
        for i in items:
            res = list(i[1].difference(processed)).pop()
            result.append((i[0], res))
            processed = processed.union(i[1])
        return result
             
    for n in nearby:
        ns = [int(i) for i in n.split(',')]
        invalid = False
        for v in ns:
            for lims in rule_set.values():
                if test_lims(v, lims):
                    break
            else:
                invalid = True
                break
        if not invalid:
            valid.append(ns)
    valid.append(mine)
    arr = np.array(valid)
    field_names = [f for f in rule_set.keys()]
    positions = {}
    for i in range(0, len(arr[0])):
        field = find_field(arr[:,i], field_names[:])
        positions[i] = set(field)
    result = process_position(positions)
    departure = [i[0] for i in result if i[1].startswith('departure')]
    return prod([mine[i] for i in departure])

puzzle = Puzzle(year=2020, day=16)
data = 'class: 1-3 or 5-7\nrow: 6-11 or 33-44\nseat: 13-40 or 45-50\n\nyour ticket:\n7,1,14\n\nnearby tickets:\n7,3,47\n40,4,50\n55,2,20\n38,6,12'
data2 = 'class: 0-1 or 4-19\nrow: 0-5 or 8-19\nseat: 0-13 or 16-19\n\nyour ticket:\n11,12,13\n\nnearby tickets:\n3,9,18\n15,1,5\n5,14,9'
print(solve_two(puzzle.input_data))