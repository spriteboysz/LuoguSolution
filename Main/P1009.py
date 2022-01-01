#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-07 23:17:42
Description: 阶乘之和
FilePath: P1009.py
'''


def func():
    n = int(input())

    ssum = 0
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        ssum += factorial

    print(ssum)


if __name__ == '__main__':
    func()
