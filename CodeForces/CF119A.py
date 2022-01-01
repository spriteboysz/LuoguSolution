#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-28 22:31:48
LastEditTime: 2021-11-28 22:38:14
Description: Epic Game
FilePath: CF119A.py
'''


from math import gcd


def func():
    a, b, n = map(int, input().strip().split())
    while n >= gcd(a, n):
        n = n - gcd(a, n)
        if n >= gcd(b, n):
            n = n - gcd(b, n)
        else:
            return 0
    else:
        return 1


if __name__ == '__main__':
    ans = func()
    print(ans)
