from aocd.models import Puzzle
import re
from collections import namedtuple, deque

puzzle = Puzzle(year=2020, day=7)


def process_luggage(data, target='shiny gold'):
    bag_graph = {}
    Record = namedtuple('Record', ['number', 'color'])
    for rule in data.split('\n'):
        bag = re.findall(r'(^[\w]+\s[\w]+)\sbags', rule)
        assert len(bag) == 1
        bag = bag[0]
        contents = re.findall(r'(\d)\s([\w\s]+)\sbag[s]?', rule)
        if not contents:
            contents = ''
        if bag not in bag_graph:
            bag_graph[bag] = []
        for n, c in contents:
            bag_graph[bag].append(Record(n, c))
    found = []
    for k in bag_graph.keys():
        if k in found:
            continue
        bag_queue = deque()
        for r in bag_graph[k]:
            bag_queue.append(r)
        while bag_queue:
            if [d for d in bag_queue if d.color == target]:
                found.add(k)
            curr_bag = bag_queue.popleft()
            for j in bag_graph[curr_bag.color]:
                bag_queue.append(j)
    return len(found)



