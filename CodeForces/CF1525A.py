#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 22:24:39
LastEditTime: 2021-11-26 22:25:47
Description: Potion-making
FilePath: CF1525A.py
'''

from math import gcd


def func():
    t = int(input())
    for _ in range(t):
        k = int(input())
        print(100 // gcd(k, 100))


if __name__ == '__main__':
    func()
    