#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-23 23:31:35
LastEditTime: 2021-10-23 23:40:00
Description: CETIRI
FilePath: P6352.py
'''


def func():
    a, b, c = sorted(map(int, input().strip().split()))

    increase1, increase2 = (b - a), (c - b)
    if increase1 == increase2:
        d = c + (b - a)
    elif increase1 == increase2 * 2:
        d = a + (c - b)
    elif increase1 * 2 == increase2:
        d = b + (b - a)
    print(d)

if __name__ == '__main__':
    func()
    