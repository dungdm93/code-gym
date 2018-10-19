"""Chef and Periodic Sequence
:ref: https://www.codechef.com/SNCK1A19/problems/PERIODIC
"""
from math import gcd

__author__ = "dungdm93"
__version__ = "1.0"
__date__ = "2018-10-19"


def readin():
    n = int(input())
    arr = [int(i) for i in input().split()]
    return n, arr


def do_logic(n, arr):
    res = None
    prev = None
    max_val = max(arr)
    for i in range(n):
        if arr[i] == -1:
            continue
        if prev is None:
            prev = i
            continue
        if arr[i] - arr[prev] == i - prev:
            prev = i
            continue
        if arr[i] - arr[prev] > i - prev:
            return "impossible"
        # arr[i] - arr[prev] < i - prev:
        curr_period = arr[prev] + (i - prev - arr[i])
        if curr_period < arr[prev]:
            return "impossible"
        res = curr_period if res is None else gcd(res, curr_period)
        if res < max_val:
            return "impossible"
    return "inf" if res is None else res


def main():
    t = int(input())
    for i in range(t):
        n, arr = readin()
        res = do_logic(n, arr)
        print(res)


if __name__ == '__main__':
    main()
