"""Reverse string fragment
:ref: https://www.hackerrank.com/contests/teko-test001/challenges/reverse-string-fragment
"""

__author__ = "dungdm93"
__version__ = "1.0"
__date__ = "2018-07-28"


def read_in():
    string = input()
    return string


def write_out(output, dir=1):
    if dir == -1:
        output.reverse()
    for e in output:
        if isinstance(e, list):
            write_out(e, -dir)
        else:
            print(e, end='')


def build_structure(string, i=0):
    output = []
    while i < len(string):
        if string[i] == '(':
            ele, end = build_structure(string, i + 1)
            i = end + 1
            output.append(ele)
        elif string[i] == ')':
            return output, i
        else:
            output.append(string[i])
            i = i + 1
    return output, i


if __name__ == '__main__':
    string = read_in()
    output, _ = build_structure(string)
    write_out(output)
