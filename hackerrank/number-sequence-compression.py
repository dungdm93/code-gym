"""Number Sequence Compression
:ref: https://www.hackerrank.com/contests/tin-hoc-tre-toan-quoc-2018-bang-b-thcs/challenges/number-sequence-compression
"""
__author__ = "dungdm93"
__version__ = "2.0"
__date__ = "2018-08-18"

mod = pow(10, 9)

def power(n, m):
  if m <= 0:
    return pow(n, m)
  half = power(n, m // 2)
  result = (half * half) % mod
  if m % 2 != 0:
    result = (n * result) % mod
  return result

if __name__ == '__main__':
    """
    res = 1*C(0, n-1) + 2*C(1, n-1) + ... + n*C(n-1, n-1)
        = C(0, n-1) +   C(1, n-1) + ... +       C(n-1, n-1)
                    + 1*C(1, n-1) + ... + (n-1)*C(n-1, n-1)
        = (k=0,n-1)S[C(k,n-1)] + (k=0,n-1)S[k*C(k,n-1)]
        = 2^(n-1) + (n-1)*2^(n-2)
        = 2^(n-2)*(n+1)
    """
    n = int(input())

    result = power(2, n - 2) * (n + 1) % mod
    print(int(result))