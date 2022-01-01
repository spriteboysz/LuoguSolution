#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-18 23:43:33
LastEditTime: 2021-11-18 23:46:17
Description: Patrick and Shopping
FilePath: CF599A.py
'''


def func():
    a, b, c = map(int, input().strip().split())
    print(min(a + b + c, 2 * (a + b), 2 * (a + c), 2 * (b + c)))


if __name__ == '__main__':
    func()
