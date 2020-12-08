from aocd.models import Puzzle
import re
from collections import namedtuple, deque


def make_graph(data):
    graph = {}
    Record = namedtuple('Record', ['number', 'color'])
    for rule in data.split('\n'):
        bag = re.findall(r'(^[\w]+\s[\w]+)\sbags', rule)
        assert len(bag) == 1
        bag = bag[0]
        contents = re.findall(r'(\d)\s([\w\s]+)\sbag[s]?', rule)
        if not contents:
            contents = ''
        if bag not in graph:
            graph[bag] = []
        for n, c in contents:
            graph[bag].append(Record(int(n), c))
    return graph


def part_a(graph, target='shiny gold'):
    found = []
    for k in graph.keys():
        if k in found or k == target:
            continue
        bag_queue = deque()
        for r in graph[k]:
            bag_queue.append(r.color)
        while bag_queue:
            if target in bag_queue:
                found.append(k)
                break
            curr_bag = bag_queue.popleft()
            for j in graph[curr_bag]:
                bag_queue.append(j.color)
    return len(found)


def part_b(graph, target='shiny gold'):
    queue = deque()
    total = 0
    for i in graph[target]:
        queue.append(i)
    while queue:
        current = queue.popleft()
        total += current.number
        for j in graph[current.color]:
            for k in range(current.number):
                queue.append(j)
    return total

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=7)
    graph = make_graph(puzzle.input_data)
    print("{} outer bags can carry a {} bag.".format(part_a(graph), 'shiny gold'))
    print("A {} bag contains {} other bags.".format('shiny gold', part_b(graph)))