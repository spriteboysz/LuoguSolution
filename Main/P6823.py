#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-26 16:46:10
LastEditTime: 2021-12-26 22:29:59
Description: zrmpaul Loves Array
FilePath: P6823.py
'''


def func():
    n, m = map(int, input().strip().split())
    lst = [i + 1 for i in range(n)]
    operator = []
    for i in range(m):
        current = list(map(int, input().strip().split()))
        operator.append(current)
        if current[0] == 1 or current[0] == 2:
            start = i

    for i in range(start, m):
        if operator[i][0] == 1:
            lst = list(sorted(lst))
        if operator[i][0] == 2:
            lst = list(sorted(lst, reverse=True))
        if operator[i][0] == 3:
            x, y = int(operator[i][1]) - 1, int(operator[i][2]) - 1
            lst[x], lst[y] = lst[y], lst[x]
        if operator[i][0] == 4:
            lst = list(reversed(lst))
        print(" ".join(map(str, lst)))


if __name__ == '__main__':
    func()
