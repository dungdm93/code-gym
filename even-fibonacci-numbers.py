"""Sum of even Fibonacci numbers
:ref: https://www.hackerrank.com/contests/teko-test001/challenges/even-fibonacci-numbers-1
"""

__author__ = "dungdm93"
__version__ = "1.0"
__date__ = "2018-07-27"


fib = [1, 1]
sum = [0, 0]


# from bisect import bisect_left
def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def find_index_lt(a, x):
    """Find rightmost value less than x"""
    i = bisect_left(a, x)
    if i:
        return i - 1
    raise ValueError


def calc_fib(i):
    if i >= len(fib):
        next_fib = calc_fib(i - 2) + calc_fib(i - 1)
        fib.append(next_fib)
    return fib[i]


def calc_sum(i):
    if i >= len(sum):
        prev_sum = calc_sum(i - 1)
        next_fib = calc_fib(i)
        if next_fib % 2 == 0:
            sum.append(prev_sum + next_fib)
        else:
            sum.append(prev_sum)
    return sum[i]


def do_logic(max):
    if fib[-1] > max:
        i = find_index_lt(fib, max)
        return sum[i]

    n = len(fib) - 1
    while calc_fib(n + 1) < max:
        calc_sum(n + 1)
        n = n + 1
    return calc_sum(n)


if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        max = int(input())
        print(do_logic(max))
