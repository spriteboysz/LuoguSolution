#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-09 22:09:19
Description: 求f(x,n)
FilePath: B2147.py
'''

def func():
    x, n = map(float, input().strip().split())

    ssum = x
    for i in range(1, int(n) + 1):
        ssum = (i + ssum) ** 0.5

    print("%.2f" % ssum)


if __name__ == '__main__':
    func()
    