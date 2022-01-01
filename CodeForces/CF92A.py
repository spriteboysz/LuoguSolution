#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-12 23:22:12
LastEditTime: 2021-11-12 23:25:45
Description: Chips
FilePath: CF92A.py
'''


def func():
    n, m = map(int, input().strip().split())
    last = m % ((1 + n) * n // 2)
    for i in range(1, n + 1):
        if last < i:
            return last
        else:
            last -= i


if __name__ == '__main__':
    ans = func()
    print(ans)
    