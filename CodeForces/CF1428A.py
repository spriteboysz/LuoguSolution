#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-24 23:42:49
LastEditTime: 2021-11-24 23:45:04
Description: Box is Pull
FilePath: CF1428A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        x1, y1, x2, y2 = map(int, input().strip().split())
        if x1 == x2 or y1 == y2:
            print(abs(x1 - x2) + abs(y1 - y2))
        else:
            print(abs(x1 - x2) + abs(y1 - y2) + 2)


if __name__ == '__main__':
    func()
