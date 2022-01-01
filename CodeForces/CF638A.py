#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-21 16:32:14
LastEditTime: 2021-11-21 16:43:26
Description: Home Numbers
FilePath: CF638A.py
'''


def func():
    n, a = map(int, input().strip().split())
    if a % 2 != 0:
        print(a // 2 + 1)
    else:
        print(n // 2 - a // 2 + 1)


if __name__ == '__main__':
    func()
    