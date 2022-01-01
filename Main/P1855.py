#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-17 22:31:45
LastEditTime: 2021-12-17 22:46:45
Description: 榨取kkksc03
FilePath: P1855.py
'''


def func():
    n, m, t = map(int, input().strip().split())
    cost = []
    for _ in range(n):
        cost.append(list(map(int, input().strip().split())))
    cost = sorted(cost, key=lambda el: (el[0], el[1]))
    count1, money1, time1 = 0, 0, 0
    for el in cost:
        if money1 + el[0] <= m and time1 + el[1] <= t:
            money1 += el[0]
            time1 += el[1]
            count1 += 1
        else:
            break
    print(cost)
    print(count1)

    cost = sorted(cost, key=lambda el: (el[1], el[0]))
    count2, money2, time2 = 0, 0, 0
    for el in cost:
        if money2 + el[0] <= m and time2 + el[1] <= t:
            money2 += el[0]
            time2 += el[1]
            count2 += 1
        else:
            break
    print(cost)
    print(count2)
    print(max(count1, count2))


if __name__ == '__main__':
    func()
