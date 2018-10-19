"""Farthest leaves
:ref: https://www.hackerrank.com/contests/teko-test001/challenges/farthest-leaves
"""

__author__ = "dungdm93"
__version__ = "1.0"
__date__ = "2018-07-30"


def read_in():
    string = input()
    return string


def write_out(output):
    print(*output)


def do_logic(string, i=0):
    string = string.replace('(', ' ( ') \
        .replace(')', ' ) ')
    elements = string.split()
    depths = [0] * len(elements)
    d = 0
    for i, e in enumerate(elements):
        if e == '(':
            d = d + 1
        elif e == ')':
            d = d - 1
        else:
            depths[i] = d
    max_d = max(depths)
    return [e for i, e in enumerate(elements) if depths[i] == max_d]


if __name__ == '__main__':
    string = read_in()
    output = do_logic(string)
    write_out(output)
