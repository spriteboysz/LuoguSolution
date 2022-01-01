#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 22:48:45
Description: 画矩形
FilePath: B2083.py
'''


def func():
    a, b, c, f = input().strip().split()
    a, b, c, f = int(a), int(b), str(c), int(f)
    for row in range(a):
        if row == 0 or row == a - 1 or f != 0:
            print(c * b)
        else:
            print(c + " " * (b - 2) + c)


if __name__ == '__main__':
    func()
