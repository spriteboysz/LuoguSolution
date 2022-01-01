#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-12 16:15:32
LastEditTime: 2021-12-12 21:51:42
Description: Roads Around The Farm S
FilePath: P2907.py
'''


def group(n, k):
    if n - k > 0 and (n - k) % 2 == 0:
        return group((n - k) // 2 + k, k) + group((n - k) // 2, k)
    else:
        return 1


def func():
    n, k = map(int, input().strip().split())
    print(group(n, k))


if __name__ == '__main__':
    func()
