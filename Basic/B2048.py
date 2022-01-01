#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 15:07:20
Description: 计算邮资
FilePath: B2048.py
'''

import math


def func():
    weight, urgent = input().strip().split()

    weight = int(weight)
    postage = 8
    if weight > 1000:
        postage += math.ceil((weight - 1000) / 500) * 4

    if urgent == "y":
        postage += 5

    print(postage)


if __name__ == '__main__':
    func()
