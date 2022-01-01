#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-01 00:03:18
LastEditTime: 2021-12-01 00:05:45
Description: Kefa and First Steps
FilePath: CF580A.py
'''


def func():
    n = int(input())
    lst1 = list(map(int, input().strip().split()))
    lst2 = [1] * n
    for i in range(1, n):
        if lst1[i - 1] <= lst1[i]:
            lst2[i] += lst2[i - 1]
    print(max(lst2))


if __name__ == '__main__':
    func()
