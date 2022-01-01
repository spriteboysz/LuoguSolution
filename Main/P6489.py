#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-16 23:37:54
LastEditTime: 2021-12-16 23:45:44
Description: USPON
FilePath: P6489.py
'''


def func():
    n = int(input())
    height = list(map(int, input().strip().split()))
    drop = [0] * n
    for i in range(1, n):
        if height[i] - height[i - 1] > 0:
            drop[i] = height[i] - height[i - 1]
    for i in range(1, n):
        if drop[i] != 0 and drop[i - 1] != 0:
            drop[i] += drop[i - 1]
    print(max(drop))


if __name__ == '__main__':
    func()
