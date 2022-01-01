#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 17:55:30
Description: 最长平台
FilePath: B2097.py
'''


def func():
    n = int(input())
    lst1 = list(map(int, input().strip().split()))
    lst2 = [1] * n

    for i in range(1, n):
        if lst1[i] == lst1[i - 1]:
            lst2[i] = lst2[i -1] + 1
    print(max(lst2))


if __name__ == '__main__':
    func()
