#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-31 22:44:52
LastEditTime: 2021-12-31 22:59:40
Description: JABUKE
FilePath: P7934.py
'''


from typing import Counter


def calcArea(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2


def func():
    triangle = []
    for _ in range(3):
        triangle.append(list(map(int, input().strip().split())))
    areas = calcArea(triangle[0][0], triangle[0][1], triangle[1]
                     [0], triangle[1][1], triangle[2][0], triangle[2][1])
    print("%.1f" % areas)

    n = int(input())
    count = 0
    for _ in range(n):
        point = list(map(int, input().strip().split()))
        area = calcArea(triangle[0][0], triangle[0][1], triangle[1]
                        [0], triangle[1][1], point[0], point[1])
        area += calcArea(triangle[0][0], triangle[0][1], triangle[2]
                         [0], triangle[2][1], point[0], point[1])
        area += calcArea(triangle[2][0], triangle[2][1], triangle[1]
                         [0], triangle[1][1], point[0], point[1])
        if area <= areas:
            count += 1
    print(count)


if __name__ == '__main__':
    func()
