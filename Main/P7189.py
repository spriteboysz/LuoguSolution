#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-20 22:57:37
LastEditTime: 2021-12-20 23:32:33
Description: PARKING
FilePath: P7189.py
'''


def func():
    a, b, c = map(int, input().strip().split())
    time = [0] * 1000
    for _ in range(3):
        start, end = map(int, input().strip().split())
        for i in range(start, end):
            time[i] += 1
    cost = 0
    for item in time:
        if item == 1:
            cost += a
        if item == 2:
            cost += 2 * b
        if item == 3:
            cost += 3 * c

    print(cost)


if __name__ == '__main__':
    func()
