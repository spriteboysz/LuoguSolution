#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-21 22:20:48
LastEditTime: 2021-11-21 22:48:37
Description: Vladik and flights
FilePath: CF743A.py
'''


def func():
    n, a, b = map(int, input().strip().split())
    airport = list(input().strip())
    if airport[a - 1] == airport[b - 1]:
        print(0)
    else:
        print(1)


if __name__ == '__main__':
    func()
