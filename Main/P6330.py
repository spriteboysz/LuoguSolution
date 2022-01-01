#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-23 23:02:48
LastEditTime: 2021-10-23 23:11:36
Description: [COCI2007-2008#1] CETVRTA
FilePath: P6330.py
'''


def func():
    x, y = 0, 0
    for _ in range(3):
        xi, yi = map(int, input().strip().split())
        x, y = xi ^ x, yi ^ y
    print(x, y)


if __name__ == '__main__':
    func()
    