"""Chefland and Average Distance
:ref: https://www.codechef.com/SNCK1A19/problems/AVGMAT
"""

__author__ = "dungdm93"
__version__ = "1.0"
__date__ = "2018-10-19"


def readin():
    n, m = input().split()
    n = int(n)
    m = int(m)
    houses = []
    for i in range(n):
        row = input()
        for j in range(m):
            if row[j] != "0":
                houses.append((i, j))
    return n, m, houses


def do_logic(n, m, houses):
    no_of_house = len(houses)
    dist = [0] * (n + m)
    for i in range(no_of_house):
        h1 = houses[i]
        for j in range(i + 1, no_of_house):
            h2 = houses[j]
            d = abs(h1[0] - h2[0]) + abs(h1[1] - h2[1])
            dist[d] = dist[d] + 1
    return dist


def main():
    t = int(input())
    for i in range(t):
        n, m, houses = readin()
        res = do_logic(n, m, houses)
        for j in range(1, n + m - 1):
            print(res[j], end=' ')


if __name__ == '__main__':
    main()
