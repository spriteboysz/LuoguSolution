#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-26 23:37:55
LastEditTime: 2021-10-26 23:51:19
Description: 攀爬者
FilePath: P5143.py
'''


def distance(lst1, lst2):
    total = 0
    for a, b in zip(lst1, lst2):
        total += (a - b) ** 2
    return total ** 0.5


def func():
    n = int(input())
    coordinates = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        coordinates.append(row)

    coordinates = sorted(coordinates, key=lambda element: element[2])
    dis = 0
    for i in range(0, n - 1):
        dis += distance(coordinates[i + 1], coordinates[i])
    print("%.3f" % dis)


if __name__ == '__main__':
    func()
