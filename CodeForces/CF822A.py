#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-09 00:07:47
LastEditTime: 2021-11-09 00:10:52
Description: I'm bored with life
FilePath: CF822A.py
'''


def func():
    a, b = sorted(map(int, input().strip().split()))
    factorial = 1
    for i in range(1, a + 1):
        factorial *= i
    print(factorial)


if __name__ == '__main__':
    func()
    