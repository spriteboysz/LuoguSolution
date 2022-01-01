#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-17 00:02:02
LastEditTime: 2021-11-17 00:06:33
Description: Binary Decimal
FilePath: CF1530A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        num = list(input().strip())
        print(max(num))


if __name__ == '__main__':
    func()
    