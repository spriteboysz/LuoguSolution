#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-18 23:41:14
Description: 矩阵乘法
FilePath: B2105.py
'''


def func():
    n, m, k = map(int, input().strip().split())
    matrix1, matrix2 = [], []
    for _ in range(n):
        matrix1.append(list(map(int, input().strip().split())))
    for _ in range(m):
        matrix2.append(list(map(int, input().strip().split())))

    for i in range(n):
        for j in range(k):
            # *初始化目标矩阵元素
            num = 0
            for l in range(m):
                num += matrix1[i][l] * matrix2[l][j]
            print(num, end= " ")
        print()

if __name__ == '__main__':
    func()
    