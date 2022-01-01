#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-23 23:25:01
LastEditTime: 2021-12-23 23:42:50
Description: 防护伞
FilePath: P1927.py
'''


def dis2(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def func():
    pi = 3.1415926535
    n = int(input())
    point = []
    for _ in range(n):
        point.append(list(map(int, input().strip().split())))

    radius2 = []
    for i in range(n):
        distance = []
        for j in range(n):
            if i != j:
                distance.append(
                    dis2(point[i][0], point[i][1], point[j][0], point[j][1]))
        radius2.append(max(distance))
    print("%.4f" % (pi * min(radius2)))


if __name__ == '__main__':
    func()
