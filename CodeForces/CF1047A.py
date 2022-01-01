#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 22:23:54
LastEditTime: 2021-11-20 22:27:59
Description: Little C Loves 3 I
FilePath: CF1047A.py
'''


def func():
    n = int(input())
    a, b, c = 1, 1, n - 2
    if c % 3 == 0:
        b, c = b + 1, c - 1
    print(a, b, c)


if __name__ == '__main__':
    func()
