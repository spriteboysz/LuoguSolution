#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-09 14:12:49
LastEditTime: 2022-01-09 14:44:56
Description: 跳马问题
FilePath: P1644.py
'''


def func():
    n, m = map(int, input().strip().split())
    chess = [[0] * (m + 2) for _ in range(n + 4)]
    chess[1][1] = 1
    n, m = n + 1, m + 1
    for j in range(2, m + 1):
        for i in range(1, n + 1):
            chess[i][j] = chess[i - 2][j - 1] + chess[i - 1][j - 2] + \
                chess[i + 2][j - 1] + chess[i + 1][j - 2]

    print(chess[n][m])


if __name__ == '__main__':
    func()
