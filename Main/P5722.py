#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-08 00:17:07
Description: 数列求和
FilePath: P5722.py
'''

def func():
    n = int(input())

    ssum = 0
    for i in range(1, n + 1):
        ssum += i

    print(ssum)


if __name__ == '__main__':
    func()
    