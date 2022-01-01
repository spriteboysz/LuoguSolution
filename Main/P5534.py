#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 23:00:47
LastEditTime: 2021-10-22 23:03:21
Description: 等差数列
FilePath: P5534.py
'''


def func():
    a1, a2, n = map(int, input().strip().split())
    an = a1 + (n - 1) * (a2 - a1)
    total = (a1 + an) * n // 2
    print(total)


if __name__ == '__main__':
    func()
    