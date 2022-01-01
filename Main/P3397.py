#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-12 17:18:38
LastEditTime: 2021-12-12 17:28:10
Description: 地毯
FilePath: P3397.py
'''


def func():
    n, m = map(int, input().strip().split())
    matrix = [[0] * n for _ in range(n)]
    for _ in range(m):
        x1, y1, x2, y2 = map(lambda el: int(el) - 1, input().strip().split())
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                matrix[x][y] += 1
    for row in range(n):
        print(" ".join(map(str, matrix[row])))


if __name__ == '__main__':
    func()
