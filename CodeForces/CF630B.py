#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-18 23:07:41
LastEditTime: 2021-11-18 23:09:59
Description: Moore's Law
FilePath: CF630B.py
'''


def func():
    n, t = map(int, input().strip().split())
    print("%.6f" % (n * 1.000000011 ** t))


if __name__ == '__main__':
    func()
    