from aocd.models import Puzzle


def two_sum(data, target=2020):
    data = sorted(data)
    left = 0
    right = len(data) - 1
    while left < right:
        if data[left] + data[right] == target:
            return data[left] * data[right]
        elif data[left] + data[right] < target:
            left += 1
        else:
            right -= 1
    raise ValueError


def three_sum(data, target=2020):
    data = sorted(data)
    for i, j in enumerate(data):
        left = i + 1
        right = len(data) - 1
        while left < right:
            if data[i] + data[left] + data[right] == target:
                return data[i] * data[left] * data[right]
            elif data[i] + data[left] + data[right] < target:
                left += 1
            else:
                right -= 1
    raise ValueError


if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=1)
    ip = [int(i) for i in puzzle.input_data.split('\n')]
    ans_a = two_sum(ip)
    ans_b = three_sum(ip)
