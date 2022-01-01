#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 00:12:07
LastEditTime: 2021-11-26 00:14:09
Description: Wrong Subtraction
FilePath: CF977A.py
'''


def func():
    n, k = map(int, input().strip().split())
    for _ in range(k):
        if n % 10 == 0:
            n = n // 10
        else:
            n -= 1
    print(n)


if __name__ == '__main__':
    func()
    