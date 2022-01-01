#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-17 23:30:54
LastEditTime: 2021-11-20 14:35:26
Description: Commentary Boxes
FilePath: CF990A.py
'''

from math import ceil


def func():
    n, m, a, b = map(int, input().strip().split())
    if n % m == 0:
        print(0)
    else:
        print(min((n - (n // m) * m) * b, (ceil(n / m) * m - n) * a))


if __name__ == '__main__':
    func()
