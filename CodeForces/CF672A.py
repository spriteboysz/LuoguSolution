#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-22 22:59:56
LastEditTime: 2021-11-22 23:01:45
Description: Summer Camp
FilePath: CF672A.py
'''


def func():
    n = int(input())
    base = ""
    for i in range(1, n + 1):
        base += str(i)

    print(base[n - 1])


if __name__ == '__main__':
    func()
