from aocd.models import Puzzle
from collections import deque, defaultdict
from math import prod

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
    sdata = sorted([int(i) for i in data.split('\n')])
    sdata.append(max(sdata) + 3)
    sdata.insert(0, 0)
    sublists = []
    def powerset(iterable):
        from itertools import chain, combinations
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
    i = 0
    while i < len(sdata):
        j = i
        k = i + 1
        sl = []
        sl.append(sdata[i])
        try:
            while sdata[k] - sdata[j] < 3:
                sl.append(sdata[k])
                k += 1
                j += 1
        except IndexError:
            pass
        i = k
        sublists.append(sl)
    count = []
    for ls in sublists:
        if ls[-1] - ls[0] > 3:
            count.append(len(list(powerset(ls[1:-1]))) - 1)
        else:
            count.append(len(list(powerset(ls[1:-1]))))
    return prod(count)

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=10)
    print(sum_jolt_diff(puzzle.input_data))
    print(part_two(puzzle.input_data))

    """
    [[0, 1, 2, 3, 4], [7, 8, 9, 10, 11], [14], [17, 18, 19, 20], [23, 24, 25], [28], [31, 32, 33, 34, 35], [38, 39],  [42], [45, 46, 47, 48, 49], [52]]
    
    
        (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22) - full
    (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)     - skip 11
    (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)    - skip 6
    (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)        - skip 6, and 11
    (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)    - skip 5 
    (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)        - skip 5, 11
    (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)       - skip 5, 6
    (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)           - skip 5, 6, 11
    
    
    
    deque([0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22])
    [0, 1], [4, 5, 6, 7], [10, 11, 12], [15, 16], [19,22])
    
    4, 5, 6, 7
    4, 5, 7
    4, 6, 7
    4, 7
    
    
    from 1: 1 1,4
    from 4: 3 1,4,5  1,4,6  1,4,7
    from 5: 2 1,4,5,6 1,4,5,7
    from 6: 1 1,4,5,6,7
    from 7: 1 1,4,5,6,7,10
    from 10: 2 1,4,5,6,7,10,11  1,4,5,6,7,10,12
    from 11: 1 
    from 12: 1
    from 15: 1
    from 16: 1 
    from 19: 1
    from 22: 1
    
    deque([1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22])
    1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22

    1, 4, 6, 7, 10, 11, 12, 15, 16, 19, 22
    
    1, 4, 7, 10, 11, 12...22
    
    1, 4, 5, 7, 10, 11, ...22

    1, 4, 5, 6, 7, 10, 12
    
    1, 4, 5, 6, 7, 10, 12, 15, 16, 19, 22
    

        
        5,
        6,
        11,
        5, 6
        5, 11
        6, 11
        5, 6, 11
        
        
        1
        2
        3
        1, 2
        1, 3
        2, 3
        1, 2, 3
        [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 52]
        [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 52]
        [[0, 1, 2, 3, 4], [7, 8, 9, 10, 11], [14], [17, 18, 19, 20], [23, 24, 25], [28], [31, 32, 33, 34, 35], [38, 39],  [42], [45, 46, 47, 48, 49], [52]]
                [7,                  7,        1,           4,            2,          1,         7,                1,       1,           5, 1]  
         
        0, 1, 2, 3, 4
        0, 1, 2, 4
        0, 1, 4
        0, 1, 3, 4
        0, 2, 3, 4
        0, 2, 4
        0, 3, 4
        
        7, 8, 9, 10, 11
        7, 8, 9, 11
        7, 8, 11
        7, 8, 10, 11
        7, 9, 10, 11
        7, 9, 11
        7, 10, 11
        
        17, 18, 19, 20
        17, 18, 20
        17, 19, 20
        17, 20
        
        23, 24, 25
        23, 25
        
        31, 32, 33, 34, 35
        31, 32, 33, 35
        31, 32, 34, 35
        31, 32, 35
        31, 33, 34, 35
        31, 33, 35
        31, 34, 35
        
        45, 46, 47, 48, 49
        45, 46, 48, 49
        45, 47, 48, 49
        45, 46, 47, 49
        45, 47, 49 
        45, 48, 49
        45, 46, 49
        
        
        
        
        
        
        
        
    """


