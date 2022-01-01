#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-01 23:33:53
LastEditTime: 2021-11-01 23:43:22
Description: Die Roll
FilePath: CF9A.py
'''


import math


def func():
    cur = max(map(int, input().strip().split()))
    gcd = math.gcd((6 - cur + 1), 6)
    ans = "%d/%d" % ((6 - cur + 1) // gcd, 6 // gcd)
    return ans


if __name__ == '__main__':
    ans = func()
    print(ans)
