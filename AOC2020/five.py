from math import ceil
from aocd.models import Puzzle


def bin_search(pass_str, max):
    low = 0
    high = max - 1
    for i in pass_str:
        mid = ceil((low + high) / 2)
        if i == 'F' or i == 'L':
            if high - low == 1:
                return low
            else:
                high = mid - 1
        elif i == 'B' or i == 'R':
            if high - low == 1:
                return high
            else:
                low = mid


def decode_boarding_pass(boarding_pass, max_row=128, max_col=8):
    """
    F -> lower half
    B -> upper half
    R -> upper half
    L -> lower half

    return -> row, column, Seat ID (row * 8 + col)

    FBFBBFFRLR
    :param boarding_pass:
    :return tuple:
    """
    row = bin_search(boarding_pass[:7], max_row)
    col = bin_search(boarding_pass[7:], max_col)
    return row, col, row * 8 + col


if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=5)
    highest = 0
    # Part A
    for i in puzzle.input_data.split('\n'):
        _, _, seat_id = decode_boarding_pass(i)
        if seat_id > highest:
            highest = seat_id
    print("The highest seat ID is {}".format(highest))

    # Part B
    seats = []
    for i in puzzle.input_data.split('\n'):
        seats.append(decode_boarding_pass(i))
    sorted_seats = sorted(seats, key=lambda x: x[2])
    for i, s in enumerate(sorted_seats):
        if s[2]+1 != sorted_seats[i+1][2]:
            print("Your Seat ID is {}".format(s[2]+1))
            break

