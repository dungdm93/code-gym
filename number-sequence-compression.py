"""Number Sequence Compression
:ref: https://www.hackerrank.com/contests/tin-hoc-tre-toan-quoc-2018-bang-b-thcs/challenges/number-sequence-compression
"""
__author__ = "dungdm93"
__version__ = "1.0"
__date__ = "2018-08-16"


def pascal(n):
    curr = 1
    for k in range(n):
        yield curr
        curr = curr * (n - k) // (k + 1)
    yield curr


if __name__ == '__main__':
    n = int(input())

    mod = pow(10, 9)
    result = 0
    for i, p in enumerate(pascal(n - 1), start=1):
        result = (result + i * p) % mod
    print(result)
