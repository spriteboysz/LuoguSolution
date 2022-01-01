#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 16:05:22
LastEditTime: 2021-10-24 16:14:40
Description: 可持久化动态仙人掌的直径问题
FilePath: P6685.py
'''

import math


def func():
    n, m = map(int, input().strip().split())

    print(int(math.pow(n, 1 / m)))


if __name__ == '__main__':
    func()
