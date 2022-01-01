#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 00:09:25
LastEditTime: 2021-11-19 00:13:07
Description: Pens and Pencils
FilePath: CF1244A.py
'''

from math import ceil


def func():
    n = int(input())
    for _ in range(n):
        a, b, c, d, k = map(int, input().strip().split())
        if ceil(a/c) + ceil(b/d) <= k:
            print(ceil(a/c), ceil(b/d))
        else:
            print(-1)


if __name__ == '__main__':
    func()
