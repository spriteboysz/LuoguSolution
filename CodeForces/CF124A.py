#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-23 23:04:30
LastEditTime: 2021-11-23 23:05:54
Description: The number of positions
FilePath: CF124A.py
'''


def func():
    n, a, b = map(int, input().strip().split())
    print(min(n - a, b + 1))


if __name__ == '__main__':
    func()
