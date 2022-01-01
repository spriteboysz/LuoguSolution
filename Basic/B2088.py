#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 14:39:45
Description: 计算书费
FilePath: B2088.py
'''


def func():
    count = list(map(int, input().strip().split()))
    price = [28.9, 32.7, 45.6, 78, 35, 86.2, 27.8, 43, 56, 65]

    total = 0
    for c, p in zip(count, price):
        total += c * p
    print("%.1f" % total)


if __name__ == '__main__':
    func()
