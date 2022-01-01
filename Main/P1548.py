#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-27 23:53:18
LastEditTime: 2021-12-28 22:54:10
Description: 棋盘问题
FilePath: P1548.py
'''


def func():
    n, m = map(int, input().strip().split())
    s = ((1 + n) * (1 + m) * n * m) // 4
    s1 = (n - min(n, m) + 1) * (m - min(n, m) + 1)
    print(s1, s - s1)


if __name__ == '__main__':
    func()
