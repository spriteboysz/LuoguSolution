#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 17:25:33
LastEditTime: 2021-11-07 17:31:42
Description: Optimal Point on a Line
FilePath: CF710B.py
'''


def func():
    n = int(input())
    position = sorted(map(int, input().strip().split()))
    if n % 2 == 0:
        print(position[n // 2 - 1])
    else:
        print(position[n // 2])


if __name__ == '__main__':
    func()
