#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-21 23:47:45
LastEditTime: 2021-12-22 00:05:16
Description: 弹珠游戏
FilePath: P2356.py
'''


def func():
    n = int(input())
    matrix, points = [], []
    for _ in range(n):
        matrix.append(tuple(map(int, input().strip().split())))
    matrix2 = list(zip(*matrix))

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                points.append(sum(matrix[i]) + sum(matrix2[j]))

    print(max(points) if len(points) != 0 else "Bad Game!")


if __name__ == '__main__':
    func()
