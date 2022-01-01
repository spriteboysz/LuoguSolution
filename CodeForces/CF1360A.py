#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-23 23:00:53
LastEditTime: 2021-11-23 23:03:35
Description: Minimal Square
FilePath: CF1360A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().strip().split())
        print(min(max(a, 2 * b), max(2 * a, b)) ** 2)


if __name__ == '__main__':
    func()
