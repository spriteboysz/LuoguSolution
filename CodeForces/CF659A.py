#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-21 16:58:20
LastEditTime: 2021-11-21 17:18:45
Description: Round House
FilePath: CF659A.py
'''


def func():
    n, a, b = map(int, input().strip().split())
    if b < 0:
        b = n + b % n
    if (a + b) % n == 0:
        print(n)
    else:
        print((a + b) % n)


if __name__ == '__main__':
    func()
    