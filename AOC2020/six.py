from aocd.models import Puzzle

def solve_a(data):
    count = 0
    for i in data.split('\n\n'):
        count += len(set([j for j in "".join(i.split('\n'))]))
    return count

puzzle = Puzzle(year=2020, day=6)
ans_a = solve_a(puzzle.input_data)

def solve_b(data):
    count = 0
    groups = data.split('\n\n')
    for group in groups:
        answer_sets = []
        for person in group.split('\n'):
            answer_sets.append(set([ans for ans in person]))
        u = set.intersection(*answer_sets)
        count += len(u)
    return count

ans_b = solve_b(puzzle.input_data)