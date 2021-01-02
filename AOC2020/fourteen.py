from aocd.models import Puzzle
import re
from itertools import product as product


def solve_a(data):
    memory = {}
    for d in data:
        mask = d[0][7::]
        instructions = d[1::]
        for i in instructions:
            matches = re.findall(r'mem\[(\d+)\]\s=\s(\d+)', i)[0]
            address, value = matches[0], int(matches[1])
            memory[address] = 0
            value_in_bin = format(value, '036b')
            assert len(mask) == len(value_in_bin)
            bl = []
            for k, j in zip(mask, value_in_bin):
                if k == 'X':
                    bl.append(j)
                elif k == '1':
                    bl.append(str(int(j) | 1))
                elif k == '0':
                    bl.append(str(int(j) & 0))
            memory[address] = int("".join(bl), 2)
    return sum([v for k, v in memory.items()])


def solve_b(data):
    memory = {}
    for d in data:
        mask = d[0][7::]
        instructions = d[1::]
        for i in instructions:
            matches = re.findall(r'mem\[(\d+)\]\s=\s(\d+)', i)[0]
            address, value = int(matches[0]), int(matches[1])
            address_in_bin = format(address, '036b')
            bl = []
            num_floating = 0
            for k, j in zip(mask, address_in_bin):
                if k == 'X':
                    bl.append('{}')
                    num_floating += 1
                elif k == '1':
                    bl.append('1')
                elif k == '0':
                    bl.append(str(int(j)))
            string_spec = "".join(bl)
            for p in product(range(2), repeat=num_floating):
                memory[string_spec.format(*p)] = value
    return sum([v for k, v in memory.items()])


def split_input(input_string):
    res = []
    for i in re.split(r'(?=mask)', input_string)[1::]:
        res.append(i.strip().split('\n'))
    return res


if __name__ == '__main__':
    ip = Puzzle(year=2020, day=14).input_data
    res_a = solve_a(split_input(ip))
    res_b = solve_b(split_input(ip))
    print("the result of part a is {}".format(res_a))
    print("the result of part b is {}".format(res_b))