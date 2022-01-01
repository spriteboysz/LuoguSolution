#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-08 22:33:59
Description: 月落乌啼算钱
FilePath: P1720.py
'''


def func():
    n = int(input())

    a = ((1 + 5 ** 0.5) / 2) ** n
    b = ((1 - 5 ** 0.5) / 2) ** n
    print("%.2f" % ((a - b) / (5 ** 0.5)))


if __name__ == '__main__':
    func()
