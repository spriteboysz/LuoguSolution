#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-04 23:21:01
LastEditTime: 2021-11-04 23:24:08
Description: On a plane
FilePath: CF409G.py
'''


def func():
    n = int(input())
    total = 0
    for _ in range(n):
        x, y = map(float, input().strip().split())
        total += y
    print("%.3f" % (total / n + 5))


if __name__ == '__main__':
    func()
