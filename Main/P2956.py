#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-21 22:47:00
LastEditTime: 2021-12-21 22:57:45
Description: The Robot Plow G
FilePath: P2956.py
'''


def func():
    x, y, t = map(int, input().strip().split())
    matrix = [["."] * x for _ in range(y)]
    for _ in range(t):
        x1, y1, x2, y2 = map(lambda el: int(el) - 1, input().strip().split())
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                matrix[y][x] = "#"

    count = 0
    for row in matrix:
        count += row.count("#")
    print(count)


if __name__ == '__main__':
    func()
