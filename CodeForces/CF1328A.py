#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-13 22:08:00
LastEditTime: 2021-11-13 22:13:00
Description: Divisibility Problem
FilePath: CF1328A.py
'''

from math import ceil


def func():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().strip().split())
        print(ceil(a / b) * b - a)


if __name__ == '__main__':
    func()
