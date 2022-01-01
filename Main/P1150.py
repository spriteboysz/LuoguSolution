#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-24 00:06:10
LastEditTime: 2021-12-24 00:08:36
Description: Peter的烟
FilePath: P1150.py
'''


def func():
    n, k = map(int, input().strip().split())
    count = n
    while n >= k:
        n, mod = divmod(n, k)
        count += n
        n += mod
    print(count)


if __name__ == '__main__':
    func()
