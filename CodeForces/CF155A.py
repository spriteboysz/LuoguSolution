#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-22 23:37:35
LastEditTime: 2021-11-22 23:42:59
Description: I love username
FilePath: CF155A.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    minimum, maximum = lst[0], lst[0]
    count = 0
    for i in range(1, n):
        if lst[i] < minimum:
            minimum = lst[i]
            count += 1
        if lst[i] > maximum:
            maximum = lst[i]
            count += 1
    print(count)


if __name__ == '__main__':
    func()
