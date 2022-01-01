#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 13:29:08
LastEditTime: 2021-11-20 13:33:44
Description: Peter and a calendar
FilePath: CF760A.py
'''


from math import ceil


def func():
    m, d = map(int, input().strip().split())
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(ceil((month[m - 1] + d - 1) / 7))


if __name__ == '__main__':
    func()
