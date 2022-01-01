#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-23 23:29:35
LastEditTime: 2021-11-23 23:32:11
Description: Candies and Two Sisters
FilePath: CF1335A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n % 2 == 0:
            print(n // 2 - 1)
        else:
            print(n // 2)


if __name__ == '__main__':
    func()
