#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-16 23:36:54
LastEditTime: 2021-11-16 23:39:44
Description: Find Divisible
FilePath: CF1096A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        l, r = map(int, input().strip().split())
        if l * 2 in range(l, r + 1):
            print(l, l * 2)


if __name__ == '__main__':
    func()
