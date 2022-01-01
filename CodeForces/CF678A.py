#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 22:45:02
LastEditTime: 2021-11-07 22:46:19
Description: Johny Likes Numbers
FilePath: CF678A.py
'''


def func():
    n, k = map(int, input().strip().split())
    print((n // k + 1) * k)


if __name__ == '__main__':
    func()
