#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-21 15:49:15
LastEditTime: 2021-11-21 15:59:27
Description: Even Odds
FilePath: CF318A.py
'''


def func():
    n, k = map(int, input().strip().split())
    if n % 2 == 0:
        if k <= n // 2:
            print(2 * k - 1)
        else:
            print((k - n // 2) * 2)
    else:
        if k <= n // 2 + 1:
            print(2 * k - 1)
        else:
            print((k - n // 2 - 1) * 2)


if __name__ == '__main__':
    func()
