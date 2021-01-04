from collections import deque

def initialize(xs): 
    map = {}
    for i,j in enumerate(xs,1):
        map[j] = deque(maxlen=2)
        map[j].append(i)
        map[j].append(i)
    return map, xs[-1], len(xs)+1
    
def consider(map, n, t, target=2000):
    while t != target:
        a, b = map[n]
        n = b - a 
        if n in map:
            map[n].append(t) 
        else:
            map[n] = deque(maxlen=2)
            map[n].append(t)
            map[n].append(t)
        t += 1
    a, b = map[n]
    return b - a