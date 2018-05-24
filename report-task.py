import functools


def read_in():
    n = int(input())
    points = list()
    for _ in range(0, n):
        task = input().split()
        points.append((int(task[0]), "START"))
        points.append((int(task[1]), "END"))
    return points


def point_comparator(x, y):
    if x[0] != y[0]:
        ret = -1 if x[0] < y[0] else 1
    elif x[1] != y[1]:
        ret = -1 if x[1] == "END" else 1
    else:
        ret = 0
    return ret


def calc_max_parallel(points):
    curr_parallel = 0
    max_parallel = 0
    for point in points:
        curr_parallel += 1 if point[1] == "START" else -1
        if curr_parallel > max_parallel:
            max_parallel = curr_parallel
    return max_parallel


def main():
    points = read_in()
    points.sort(key=functools.cmp_to_key(point_comparator))
    max_parallel = calc_max_parallel(points)
    print(max_parallel)


if __name__ == '__main__':
    main()
