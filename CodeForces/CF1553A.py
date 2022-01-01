#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 22:32:49
LastEditTime: 2021-11-26 22:34:14
Description: Digits Sum
FilePath: CF1553A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print((n + 1) // 10)


if __name__ == '__main__':
    func()
    