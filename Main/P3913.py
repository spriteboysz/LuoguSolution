#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-04 22:47:16
LastEditTime: 2022-01-04 23:05:23
Description: 车的攻击
FilePath: P3913.py
'''


def func():
    n, k = map(int, input().strip().split())
    point = []
    for _ in range(k):
        point.extend(map(int, input().strip().split()))
    r, c = len(set(point[0::2])), len(set(point[1::2]))
    print((r + c) * n - r * c)


if __name__ == '__main__':
    func()
