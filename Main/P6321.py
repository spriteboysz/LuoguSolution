#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-13 23:31:19
LastEditTime: 2021-12-14 00:07:48
Description: SKENER
FilePath: P6321.py
'''


def func():
    r, c, zr, zc = map(int, input().strip().split())
    matrix1, matrix2 = [], []
    for _ in range(r):
        matrix1.append(list(input().strip()))

    row = [[] for _ in range(r * zr)]
    for i in range(r):
        for j in range(c):
            row[i].append(matrix1[i][j] * zc)
        matrix2.extend([row[i] for _ in range(zr)])

    for i in range(r * zr):
        print("".join(matrix2[i]))


if __name__ == '__main__':
    func()
