#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 23:37:30
LastEditTime: 2021-11-28 17:09:49
Description: Maximum Number
FilePath: CF774C.py
'''


def func():
    #input122
    n = int(input())
    if n % 2 == 0:
        print("1" * (n // 2))
    else:
        print("7" + "1" * ((n - 3) // 2))


if __name__ == '__main__':
    func()
