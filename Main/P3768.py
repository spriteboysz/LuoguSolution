#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 20:26:34
LastEditTime: 2021-10-24 20:32:02
Description: 简单的数学题
FilePath: P3768.py
'''


import math


def func():
    n, p = map(int, input().strip().split())
    total = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            total += i * j * math.gcd(i, j)

    print(total % p)


if __name__ == '__main__':
    func()
