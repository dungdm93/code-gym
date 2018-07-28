"""Sum of Multiples
:ref: https://www.hackerrank.com/contests/teko-test001/challenges/sum-of-multiples
"""

__author__ = "dungdm93"
__version__ = "1.0"
__date__ = "2018-07-28"


def sum_multiple_of_numbers_lest_than(n, max):
    number = max // n
    if max % n == 0:
        number = number - 1
    greatest = number * n
    return (n + greatest) * number // 2


def do_logic(max):
    return sum_multiple_of_numbers_lest_than(3, max) \
           + sum_multiple_of_numbers_lest_than(5, max) \
           - sum_multiple_of_numbers_lest_than(15, max)


if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        n = int(input())
        print(do_logic(n))
