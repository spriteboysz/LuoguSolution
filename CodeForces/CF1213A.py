#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-16 23:06:44
LastEditTime: 2021-11-16 23:14:51
Description: Chips Moving
FilePath: CF1213A.py
'''


def func():
    _ = int(input())
    lst = list(map(int, input().strip().split()))
    even, odd = 0, 0
    for item in lst:
        if item % 2 == 0:
            even += 1
        else:
            odd += 1

    print(min(even, odd))


if __name__ == '__main__':
    func()
