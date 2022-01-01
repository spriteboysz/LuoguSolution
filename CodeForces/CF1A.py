#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-01 22:50:46
LastEditTime: 2021-11-01 22:59:52
Description: Theatre Square
FilePath: CF1A.py
'''

import math


def func():
    n, m, a = map(int, input().strip().split())
    return math.ceil(n / a) * math.ceil(m / a)

if __name__ == '__main__':
    ans = func()
    print(ans)
