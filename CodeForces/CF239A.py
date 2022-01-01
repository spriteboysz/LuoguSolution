#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 21:51:35
LastEditTime: 2021-11-26 23:46:11
Description: Two Bags of Potatoes
FilePath: CF239A.py
'''

from math import ceil


def func():
    y, k, n = map(int, input().strip().split())
    lst = []

    for x in range(ceil(y / k) * k - y, n - y + 1, k):
        if x > 0:
            lst.append(x)

    if len(lst) == 0:
        print(-1)
    else:
        print(" ".join(map(str, lst)))


if __name__ == '__main__':
    func()
