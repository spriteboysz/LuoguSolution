#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-28 23:26:18
LastEditTime: 2021-10-28 23:56:35
Description: 最大公约数和最小公倍数问题
FilePath: P1029.py
'''


import math


def func():
    x, y = map(int, input().strip().split())
    count = 0
    for i in range(x, y + 1, x):
        for j in range(x, y + 1, x):
            if y % i == y % j == 0:
                gcd = math.gcd(i, j)
                if gcd == x and (i * j) / gcd == y:
                    count += 1
                    print(i, j)
                    break
    print(count)


if __name__ == '__main__':
    func()
