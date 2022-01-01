#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-12 23:15:41
LastEditTime: 2021-11-12 23:19:54
Description: Toy Army
FilePath: CF84A.py
'''


def func():
    n = int(input())
    if n % 4 == 0:
        return 2 * n - n // 2
    else:
        return 2 * n - n // 4 - n // 4 - 1


if __name__ == '__main__':
    ans = func()
    print(ans)
