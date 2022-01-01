#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-02 23:26:20
LastEditTime: 2021-12-03 22:58:33
Description: Wizards and Demonstration
FilePath: CF168A.py
'''


from math import ceil


def func():
    n, x, y = map(int, input().strip().split())
    if x >= ceil(n * y / 100):
        print(0)
    else:
        print(ceil(y * n / 100 - x))


if __name__ == '__main__':
    func()
