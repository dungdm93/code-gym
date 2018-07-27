"""LineUp
:ref: https://www.hackerrank.com/contests/teko-test001/challenges/line-up-1
"""

__author__ = "dungdm93"
__version__ = "1.0"
__date__ = "2018-07-27"


def read_in():
    n = int(input())
    heights = [int(i) for i in input().split()]
    return n, heights


def write_out(heights):
    print(*heights)


def calculate(heights):
    man = []
    tree = []
    for i, h in enumerate(heights):
        if h > 0:
            man.append(h)
        else:
            tree.append(i)
    man.sort()
    output = man.copy()
    for i in tree:
        output.insert(i, -1)
    return output


if __name__ == '__main__':
    n, heights = read_in()
    output = calculate(heights)
    write_out(output)
