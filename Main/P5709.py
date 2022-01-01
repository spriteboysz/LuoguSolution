#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-07 00:09:46
Description: 苹果和虫子
FilePath: P5709.py
'''

import math


def func():
    m, t, s = map(int, input().strip().split())
    try:
        if m < math.ceil(s / t):
            print(0)
        else:
            print(m - math.ceil(s / t))
    except Exception:
        print(0)


if __name__ == '__main__':
    func()
