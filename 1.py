from aocd.models import Puzzle
from aocd import submit

puzzle = Puzzle(year=2020, day=1)
data = sorted([int(i) for i in puzzle.input_data.split('\n')])

def two_sum(data, target=2020):
    left = 0
    right = len(data) - 1
    while left < right:
        if data[left] + data[right] == target:
            return (left, right)
        elif data[left] + data[right] < target:
            left += 1
        else:
            right -= 1
    return ()


def three_sum(data, target=2020):
    for i, j in enumerate(data):
        left = i + 1
        right = len(data) - 1
        while left < right:
            if data[i] + data[left] + data[right] == target:
                return [i, left, right]
            elif data[i] + data[left] + data[right] < target:
                left += 1
            else:
                right -= 1
    return []

pair = two_sum(data)
assert data[pair[0]] + data[pair[1]]== 2020
result = data[pair[0]] * data[pair[1]]


triple = three_sum(data)
assert data[triple[0]] + data[triple[1]] + data[triple[2]] == 2020

result3 = data[triple[0]] * data[triple[1]] * data[triple[2]]

#submit(result3)