#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-18 23:31:08
Description: 矩阵加法
FilePath: B2104.py
'''


def func():
    n, m = map(int, input().strip().split())
    matrix1, matrix2 = [], []
    for _ in range(n):
        matrix1.append(list(map(int, input().strip().split())))
    for _ in range(n):
        matrix2.append(list(map(int, input().strip().split())))

    # *对应元素相加后按行输出
    for i in range(n):
        row = []
        for j in range(m):
            row.append(str(matrix1[i][j] + matrix2[i][j]))
        print(" ".join(row))


if __name__ == '__main__':
    func()
