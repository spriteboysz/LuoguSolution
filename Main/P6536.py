#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-26 17:03:21
LastEditTime: 2021-12-26 22:07:21
Description: KUŠAČ
FilePath: P6536.py
'''


from math import gcd


def func():
    n, m = map(int, input().strip().split())
    print(m - 1 - (gcd(n, m) - 1))


if __name__ == '__main__':
    func()
