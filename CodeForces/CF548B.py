#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 13:36:24
LastEditTime: 2021-11-20 14:13:07
Description: 
FilePath: CF548B.py
'''


def func():
    n, m, q = map(int, input().strip().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().strip().split())))

    for _ in range(q):
        i, j = map(int, input().strip().split())
        matrix[i - 1][j - 1] = int(not matrix[i - 1][j - 1])
        pass
    


if __name__ == '__main__':
    func()
    