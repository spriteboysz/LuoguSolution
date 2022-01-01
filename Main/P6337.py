#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-23 23:20:37
LastEditTime: 2021-10-23 23:27:10
Description: CRNE
FilePath: P6337.py
'''


def func():
    n = int(input())

    row = n // 2
    if n % 2 == 0:
        col = row
    else:
        col = row + 1
    print((row + 1) * (col + 1))


if __name__ == '__main__':
    func()
