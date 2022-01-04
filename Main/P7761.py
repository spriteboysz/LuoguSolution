#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-04 23:44:48
LastEditTime: 2022-01-05 00:04:08
Description: [COCI2016-2017#5] Pareto
FilePath: P7761.py
'''


def func():
    n = int(input())
    deposit = list(sorted(map(int, input().strip().split()), reverse=True))
    maximum = 0
    for i in range(0, n):
        a = (i + 1) / n * 100
        b = sum(deposit[:i + 1]) / sum(deposit) * 100
        if b - a > maximum:
            maximum = b - a
            a1, b1 = a, b

    print("%f\n%f" % (a1, b1))


if __name__ == '__main__':
    func()
