#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-09 23:40:46
LastEditTime: 2021-12-09 23:42:41
Description: Addition
FilePath: P7917.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    total = lst[0]
    for i in range(1, n):
        total += abs(lst[i])
    print(total)


if __name__ == '__main__':
    func()
