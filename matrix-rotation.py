"""Matrix rotation
:ref: https://www.hackerrank.com/contests/teko-test001/challenges/matrix-rotation-4
"""

__author__ = "dungdm93"
__version__ = "1.0"
__date__ = "2018-07-29"


def read_in():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = [int(i) for i in input().split()]
        matrix.append(row)
    return n, matrix


def write_out(n, matrix):
    for j in range(0, n, +1):
        for i in range(n - 1, -1, -1):
            print(matrix[i][j], end=' ')
        print()


if __name__ == '__main__':
    n, matrix = read_in()
    write_out(n, matrix)
