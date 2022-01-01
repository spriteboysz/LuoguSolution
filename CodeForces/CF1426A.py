#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-16 23:50:46
LastEditTime: 2021-11-17 00:00:22
Description: Floor Number
FilePath: CF1426A.py
'''


from math import ceil


def func():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().strip().split())
        if n == 1 or n == 2:
            print(1)
        else:
            print(ceil((n - 2) / x) + 1)


if __name__ == '__main__':
    func()
