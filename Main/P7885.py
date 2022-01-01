#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-31 22:20:11
LastEditTime: 2021-12-31 22:23:28
Description: Flight
FilePath: P7885.py
'''


def func():
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().strip().split())
        x, y = abs(a - c), abs(b - d)
        print(min(x, y) * 2 + abs(y - x) * 2 - abs(y - x) % 2)


if __name__ == '__main__':
    func()
