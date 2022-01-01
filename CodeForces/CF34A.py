#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-12 22:51:20
LastEditTime: 2021-11-26 22:47:03
Description: Reconnaissance 2
FilePath: CF34A.py
'''


def func():
    n = int(input())
    high = list(map(int, input().strip().split()))
    high.append(high[0])
    minimum = abs(high[0] - high[1])
    a, b = 0, 1
    for i in range(1, n):
        if abs(high[i] - high[i + 1]) < minimum:
            minimum = abs(high[i] - high[i + 1])
            a, b = i, i + 1
    # *当模数为0时，取值n
    if (b + 1) % n == 0:
        print(a + 1, n)
    else:
        print(a + 1, (b + 1) % n)


if __name__ == '__main__':
    func()
