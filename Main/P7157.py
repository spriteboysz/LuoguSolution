#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-24 22:26:20
LastEditTime: 2021-12-24 22:27:32
Description: Physics Problem
FilePath: P7157.py
'''


def func():
    n, k = map(int, input().strip().split())
    print(n * (n - 1) // 2 - k)


if __name__ == '__main__':
    func()
