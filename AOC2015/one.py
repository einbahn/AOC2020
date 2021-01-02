from aocd.models import Puzzle

p = Puzzle(year=2015, day=1)
c = 0
for i in p.input_data:
    if i == '(':
        c += 1
    else:
        c -= 1

print("part 1 {}".format(c))

c = 0
ans = 0
for i, j in enumerate(p.input_data, 1):
    if j == '(':
        c += 1
    else:
        c -= 1
    if c == -1:
       ans = i
       break

print("part 2 {}".format(ans))