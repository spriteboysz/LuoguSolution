#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-03 21:59:37
LastEditTime: 2022-01-03 22:08:49
Description: Wheel Rotation G
FilePath: P2913.py
'''


def func():
    n = int(input())
    direction = 0
    for _ in range(n - 1):
        _, _, d = map(int, input().strip().split())
        direction = direction ^ d
    print(direction)


if __name__ == '__main__':
    func()
