#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-03 22:10:16
LastEditTime: 2021-11-21 23:47:04
Description: Increasing Sequence
FilePath: CF11A.py
'''


def func():
    n, d = map(int, input().strip().split())
    lst = list(map(int, input().strip().split()))
    count = 0
    for i in range(1, n):
        if lst[i - 1] >= lst[i]:
            multiple = ((lst[i - 1] - lst[i]) // d) + 1
            lst[i] += multiple * d
            count += multiple
    print(count)


if __name__ == '__main__':
    func()
