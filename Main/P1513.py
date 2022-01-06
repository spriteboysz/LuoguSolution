#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-06 22:47:19
LastEditTime: 2022-01-06 23:04:39
Description: 绕钉子的长绳子
FilePath: P1513.py
'''


def calcLength(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def func():
    n, r = map(float, input().strip().split())
    point = []
    for _ in range(int(n)):
        point.append(list(map(float, input().strip().split())))
    point.append(point[0])

    length = 0
    for i in range(1, int(n) + 1):
        length += calcLength(point[i - 1][0], point[i - 1]
                             [1], point[i][0], point[i][1])
    length += 2 * r * 3.14159265
    print("%.2f" % length)


if __name__ == '__main__':
    func()
