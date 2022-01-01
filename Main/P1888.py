#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-06 15:18:39
Description: 三角函数
FilePath: P1888.py
'''


def gcd(a, b):
    while True:
        if a % b == 0:
            return b
        else:
            a, b = b, a % b


def func():
    a, b, c = sorted(list(map(int, input().strip().split())))
    print("%d/%d" % (a / gcd(a, c), c / gcd(a, c)))


if __name__ == '__main__':
    func()
