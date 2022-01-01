#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-23 23:59:49
LastEditTime: 2021-11-24 00:03:21
Description: Equation
FilePath: CF1269A.py
'''


def func():
    n = int(input())
    base = 4 if n % 2 == 0 else 9
    print(base + n, base)


if __name__ == '__main__':
    func()
