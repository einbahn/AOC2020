def two_sum(data, target):
    data = sorted(data)
    left = 0
    right = len(data) - 1
    while left < right:
        if data[left] + data[right] == target:
            return
        elif data[left] + data[right] < target:
            left += 1
        else:
            right -= 1
    raise ValueError


def part_one(data, preamble_length=25):
    n = [int(i) for i in data.split('\n')]
    i = 0
    j = 0 + preamble_length
    k = j
    while True:
        s = n[i:j]
        target = n[k]
        try:
            two_sum(s, target)
        except ValueError:
            return target
            break
        i = i+1
        j = j+1
        k = k+1


def part_two(data, target=41682220):
    n = [int(i) for i in data.split('\n')]
    i = 0
    k = i + 1
    s = [n[i], n[k]]
    while sum(s) != target and k < len(n):
        if sum(s) > target:
            i += 1
            k = i + 1
            s = [n[i], n[k]]
        else:
            k += 1
            s.append(n[k])
    if sum(s) == target:
        return min(s) + max(s)
    else:
        return None
