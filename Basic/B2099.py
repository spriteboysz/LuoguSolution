#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 17:28:06
Description: 矩阵交换行
FilePath: B2099.py
'''


def func():
    matrix = []
    for _ in range(5):
        row = list(map(int, input().strip().split()))
        matrix.append(row)
    m, n = map(int, input().strip().split())

    matrix[m - 1], matrix[n - 1] = matrix[n - 1], matrix[m - 1]
    for i in range(5):
        print(" ".join(map(str, matrix[i])))


if __name__ == '__main__':
    func()
