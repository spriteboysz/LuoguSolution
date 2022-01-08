#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-08 21:59:34
Description: 回文质数
FilePath: P1217.py
'''

from math import ceil


def func():
    a, b = map(int, input().strip().split())
    for i in [5, 7, 11]:
        if a <= i <= b:
            print(i)
    for i in range(10, 10000):
        num = int(str(i)[:-1] + str(i)[::-1])
        if a <= num <= b:
            for j in range(2, ceil(num ** 0.5) + 1):
                if num % j == 0:
                    break
            else:
                print(num)


if __name__ == '__main__':
    func()
