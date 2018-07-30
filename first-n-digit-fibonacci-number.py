"""First N-digit Fibonacci number
:ref: https://www.hackerrank.com/contests/teko-test001/challenges/first-n-digit-fibonacci-number
"""

__author__ = "dungdm93"
__version__ = "1.0"
__date__ = "2018-07-30"

fib = [1, 1]


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


def find_index_ge(a, x):
    """Find leftmost item greater than or equal to x"""
    i = bisect_left(a, x)
    if i != len(a):
        return i
    raise ValueError


def calc_fib(i):
    if i >= len(fib):
        next_fib = calc_fib(i - 2) + calc_fib(i - 1)
        fib.append(next_fib)
    return fib[i]


def do_logic(n):
    x = 0 if n == 1 else pow(10, n - 1)
    if fib[-1] > x:
        i = find_index_ge(fib, x)
        return i

    n = len(fib) - 1
    while calc_fib(n) < x:
        n = n + 1
    return n


if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        n = int(input())
        if n == 0:
            print(0)
            continue
        x = do_logic(n)
        print(x + 1)
