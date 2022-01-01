#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-31 23:04:40
LastEditTime: 2021-12-31 23:33:00
Description: 众数
FilePath: P2681.py
'''

from collections import Counter


def func():
    n, m = map(int, input().strip().split())
    lst = []
    for _ in range(n):
        lst.append(int(input().strip()))
    for _ in range(m):
        flag, a, b = map(int, input().strip().split())
        a, b = a - 1, b - 1
        if flag == 0:
            temp = sorted(lst[a:b+1])
            print(max(temp, key=temp.count))
        else:
            lst[a] = b


if __name__ == '__main__':
    func()
