#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-25 23:39:21
LastEditTime: 2021-12-21 23:44:48
Description: yyy loves Maths II
FilePath: P2393.py
'''


from decimal import Decimal


def func():
    try:
        num = list(map(Decimal, input().strip().split()))
    except EOFError:
        print("0.00000")
    else:
        print('{:.5f}'.format(sum(num)))


if __name__ == '__main__':
    func()
