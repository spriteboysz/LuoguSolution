#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-27 23:10:54
LastEditTime: 2021-11-27 23:28:38
Description: Power Consumption Calculation
FilePath: CF10A.py
'''


def func():
    n, p1, p2, p3, t1, t2 = map(int, input().strip().split())
    left, right = [0] * n, [0] * n
    power = 0
    for i in range(n):
        left[i], right[i] = map(int, input().strip().split())
        power += (right[i] - left[i]) * p1

    for i in range(n - 1):
        interval = left[i + 1] - right[i]
        if interval <= t1:
            power += p1 * interval
        elif t1 < interval <= t1 + t2:
            power += p1 * t1 + p2 * (interval - t1)
        else:
            power += p1 * t1 + p2 * t2 + p3 * (interval - t1 - t2)
    print(power)


if __name__ == '__main__':
    func()
