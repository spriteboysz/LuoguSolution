#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-19 23:16:46
LastEditTime: 2021-10-19 23:23:16
Description: 图像旋转
FilePath: B2107.py
'''


def func():
    n, m = map(int, input().strip().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().strip().split())))

    for j in range(m):
        row = []
        for i in range(n - 1, -1, -1):
            row.append(str(matrix[i][j]))
        print(" ".join(row))


if __name__ == '__main__':
    func()
