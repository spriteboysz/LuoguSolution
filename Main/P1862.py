#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-10 22:47:27
LastEditTime: 2022-01-10 22:52:56
Description: 输油管道问题
FilePath: P1862.py
'''


def func():
    n = int(input())
    well = []
    for _ in range(n):
        _, y = map(int, input().strip().split())
        well.append(y)
    well = sorted(well)
    length = 0
    for i in range(n):
        length += abs(well[i] - well[n // 2])
    print(length)


if __name__ == '__main__':
    func()
