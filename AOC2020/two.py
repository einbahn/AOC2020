from aocd.models import Puzzle

puzzle = Puzzle(2020, 2)
data = [i for i in puzzle.input_data.split('\n')]

def check_passwd(password):
    """
    >>> check_passwd('1-3 a: abcde')
    True
    >>> check_passwd('1-3 b: cdefg')
    False
    >>> check_passwd('2-9 c: ccccccccc')
    True
    """
    pfields = password.split()
    pmin, pmax = [int(i) for i in pfields[0].split('-')]
    l = pfields[1][0]
    ps = pfields[2]
    pslen = len([i for i in ps if i == l])
    return pmax >= pslen >= pmin

def check_passwd2(password):
    """
    >>> check_passwd2('1-3 a: abcde')
    True
    >>> check_passwd2('1-3 b: cdefg')
    False
    >>> check_passwd2('2-9 c: ccccccccc')
    False
    """
    pfields = password.split(' ')
    idx1, idx2 = [int(i)-1 for i in pfields[0].split('-')]
    ltr = pfields[1][0]
    ps = pfields[2]
    return (ps[idx1] == ltr) != (ps[idx2] == ltr)


ans1 = len([check_passwd(i) for i in data if check_passwd(i)])
ans2 = len([check_passwd2(i) for i in data if check_passwd2(i)])
