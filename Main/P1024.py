#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-24 22:47:42
LastEditTime: 2021-12-24 23:24:56
Description: 一元三次方程求解
FilePath: P1024.py
'''


def fun(a, b, c, d, x):
    return a * (x ** 3) + b * (x ** 2) + c * x + d


def func():
    a, b, c, d = map(float, input().strip().split())
    lst = []
    for x in range(-100 * 1000, 100 * 1000 + 1):
        if fun(a, b, c, d, x / 1000) == 0:
            lst.append("%.2f" % (x / 1000))
        elif fun(a, b, c, d, x / 1000) * fun(a, b, c, d, (x + 1) / 1000) < 0:
            lst.append("%.2f" % (x / 1000))
        if len(lst) == 3:
            break
    print(" ".join(lst))


if __name__ == '__main__':
    func()
