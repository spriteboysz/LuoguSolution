#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-19 16:29:14
LastEditTime: 2021-12-19 21:48:18
Description: 圆
FilePath: P1652.py
'''


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def func():
    n = int(input())
    x = list(map(int, input().strip().split()))
    y = list(map(int, input().strip().split()))
    r = list(map(int, input().strip().split()))
    x1, y1, x2, y2 = map(int, input().strip().split())
    count = 0
    for i in range(n):
        if (distance(x[i], y[i], x1, y1) < r[i]) ^ (distance(x[i], y[i], x2, y2) < r[i]):
            count += 1
    print(count)


if __name__ == '__main__':
    func()
