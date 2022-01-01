#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-06 23:45:14
Description: 数的性质
FilePath: P5710.py
'''


def func():
    n = int(input())

    rst = [0] * 4
    if n % 2 == 0 and 4 < n <= 12:
        rst[0] = 1
    if n % 2 == 0 or 4 < n <= 12:
        rst[1] = 1
    if n % 2 == 0 and (n <= 4 or n > 12):
        rst[2] = 1
    elif n % 2 != 0 and 4 < n <= 12:
        rst[2] = 1
    if n % 2 != 0 and (n <= 4 or n > 12):
        rst[3] = 1

    print(" ".join(map(str, rst)))


if __name__ == '__main__':
    func()
