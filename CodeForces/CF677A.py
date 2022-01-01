#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-22 23:49:14
LastEditTime: 2021-11-22 23:52:09
Description: Vanya and Fence
FilePath: CF677A.py
'''


def func():
    n, k = map(int, input().strip().split())
    high = list(map(int, input().strip().split()))
    width = 0
    for i in range(n):
        if high[i] <= k:
            width += 1
        else:
            width += 2
    print(width)


if __name__ == '__main__':
    func()
