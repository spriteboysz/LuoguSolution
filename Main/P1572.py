#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-08 22:43:04
LastEditTime: 2021-12-08 23:06:25
Description: 计算分数
FilePath: P1572.py
'''

from functools import reduce
from math import gcd


def func():
    s = input().strip()
    fraction = s.replace("-", "+-").lstrip("+").split("+")
    fraction = list(map(lambda el: list(map(int, el.split("/"))), fraction))
    ans = reduce(
        lambda x, y: [(x[0] * y[1] + x[1] * y[0]), (x[1] * y[1])], fraction)
    numerator = ans[0] // gcd(ans[0], ans[1])
    denominator = ans[1] // gcd(ans[0], ans[1])
    if denominator == 1:
        print(numerator)
    else:
        print(str(numerator) + "/" + str(denominator))


if __name__ == '__main__':
    func()
