#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-03 23:48:40
LastEditTime: 2021-11-26 23:25:40
Description: Blinds
FilePath: CF38C.py
'''


def func():
    n, l = map(int, input().strip().split())
    stripes = list(map(int, input().strip().split()))
    areas = []
    for length in range(l, 100 + 1):
        count = 0
        for j in range(n):
            count += (stripes[j] // length)
        areas.append(count * length)
    print(max(areas))


if __name__ == '__main__':
    func()
