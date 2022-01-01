#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-11 23:01:37
LastEditTime: 2021-11-11 23:04:12
Description: Two Rabbits
FilePath: CF1304A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        x, y, a, b = map(int, input().strip().split())
        if (y - x) % (a + b) == 0:
            print((y - x) // (a + b))
        else:
            print(-1)


if __name__ == '__main__':
    func()
