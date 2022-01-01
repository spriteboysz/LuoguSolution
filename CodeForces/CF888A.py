#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 23:18:57
LastEditTime: 2021-11-19 23:23:29
Description: Local Extrema
FilePath: CF888A.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    count = 0
    for i in range(1, n - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            count += 1
        elif lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
            count += 1
    print(count)


if __name__ == '__main__':
    func()
