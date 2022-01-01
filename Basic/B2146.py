#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-09 22:36:00
Description: Hermite 多项式
FilePath: B2146.py
'''


def hermite(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2 * x * hermite(x, n - 1) - 2 * (n - 1) * hermite(x, n - 2)


def func():
    n, x = map(int, input().strip().split())
    print(hermite(x, n))


if __name__ == '__main__':
    func()
