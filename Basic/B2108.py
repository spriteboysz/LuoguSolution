#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-19 23:29:11
LastEditTime: 2021-10-19 23:54:59
Description: 图像模糊处理
FilePath: B2108.py
'''


def func():
    n, m = map(int, input().strip().split())
    matrix1, matrix2 = [], []
    # !初始化输出二维数组，考虑更简便的方法 
    for _ in range(n):
        matrix1.append(list(map(int, input().strip().split())))
        matrix2.append([0] * m)
   
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                matrix2[i][j] = matrix1[i][j]
            else:
                matrix2[i][j] = (matrix1[i][j] + matrix1[i + 1][j] +
                                 matrix1[i - 1][j] + matrix1[i][j + 1] + matrix1[i][j - 1]) / 5

    for i in range(n):
        print(" ".join(map(str, map(round, matrix2[i]))))


if __name__ == '__main__':
    func()
