#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-01 15:21:04
LastEditTime: 2022-01-01 15:27:16
Description: 晨跑
FilePath: P4057.py
'''

from math import gcd


def func():
    a, b, c = map(int, input().strip().split())
    ab = a * b // gcd(a, b)
    print(ab * c // gcd(ab, c))


if __name__ == '__main__':
    func()
