"""First non-unique
:ref: https://www.hackerrank.com/contests/teko-test001/challenges/first-non-unique
"""

__author__ = "dungdm93"
__version__ = "1.0"
__date__ = "2018-07-28"


def read_in():
    n = int(input())
    numbers = [int(i) for i in input().split()]
    return n, numbers


def write_out(output):
    print(output)


def do_logic(n, numbers):
    slot = 0
    for i in numbers:
        if slot & (2 << i):
            return i
        else:
            slot = slot | (2 << i)
    return -1


if __name__ == '__main__':
    n, numbers = read_in()
    output = do_logic(n, numbers)
    write_out(output)
