#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-01 23:45:35
LastEditTime: 2021-11-05 23:25:05
Description: 
FilePath: CF12A.py
'''


def func():
    matrix = []
    for _ in range(3):
        # *中心对称，转换为一维数组
        matrix.extend(list(input().strip()))

    for i in range(len(matrix) // 2):
        if matrix[i] != matrix[8 - i]:
            return "NO"
    return "YES"


if __name__ == '__main__':
    ans = func()
    print(ans)
