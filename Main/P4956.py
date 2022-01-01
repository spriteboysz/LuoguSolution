#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-08 23:32:37
Description: Davor
FilePath: P4956.py
'''


def func():
    n = int(input())
    for k in range(1, n):
        for x in range(100, 0, -1):
            if (7 * x + 21 * k) == (n // 52):
                print(x)
                print(k)
                return


if __name__ == '__main__':
    func()
