#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-17 23:30:11
LastEditTime: 2021-12-17 23:44:28
Description: cover
FilePath: P3717.py
'''


def func():
    n, m, r = map(int, input().strip().split())
    matrix = [[0] * n for _ in range(n)]
    point = []
    for _ in range(m):
        x, y = map(lambda el: int(el) - 1, input().strip().split())
        matrix[x][y] = 1
        point.append([x, y])

    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(len(point)):
                if matrix[i][j] == 0 and (i - point[k][0]) ** 2 + (j - point[k][1]) ** 2 <= r ** 2:
                    matrix[i][j] = 1
        count += sum(matrix[i])
    print(count)


if __name__ == '__main__':
    func()
