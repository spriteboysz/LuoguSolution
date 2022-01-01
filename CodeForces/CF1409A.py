#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 00:05:32
LastEditTime: 2021-11-20 00:07:22
Description: Yet Another Two Integers Problem
FilePath: CF1409A.py
'''

from math import ceil


def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().strip().split())
        print(ceil(abs(a - b) / 10))


if __name__ == '__main__':
    func()
