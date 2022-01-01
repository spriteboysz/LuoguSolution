#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-18 23:59:06
Description: 矩阵转置
FilePath: B2106.py
'''


def func():
    n, m = map(int, input().strip().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().strip().split())))

    for j in range(m):
        row = []
        for i in range(n):
            row.append(str(matrix[i][j]))
        print(" ".join(row))


if __name__ == '__main__':
    func()
