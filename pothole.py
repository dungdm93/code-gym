"""Pothole
:ref: https://www.hackerrank.com/contests/teko-test001/challenges/pothole-1
"""

__author__ = "dungdm93"
__version__ = "1.0"
__date__ = "2018-07-29"


def read_in():
    n = int(input())
    heights = [int(i) for i in input().split()]
    return heights


def write_out(max_depth):
    print(max_depth)


def do_logic(heights):
    diff = []
    for i in range(1, len(heights)):
        diff.append(heights[i] - heights[i - 1])
    up = down = max_depth = 0
    for i, d in enumerate(diff):
        if d == 0:
            up = down = 0
        elif d < 0:
            up = 0
            if i > 0 and diff[i - 1] >= 0:
                down = 0
            down = down + d
        elif d > 0:
            up = up + d
            curr_dep = min(abs(up), abs(down))
            max_depth = max(max_depth, curr_dep)
    return max_depth


if __name__ == '__main__':
    heights = read_in()
    max_depth = do_logic(heights)
    write_out(max_depth)
