#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-26 17:00:04
LastEditTime: 2021-12-26 22:08:03
Description: PUŽ
FilePath: P6546.py
'''


from math import ceil


def func():
    a, b, v = map(int, input().strip().split())
    print(ceil((v - a) / (a - b)) + 1)


if __name__ == '__main__':
    func()
