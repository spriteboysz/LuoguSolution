#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-09 22:57:52
LastEditTime: 2021-12-09 23:04:22
Description: 第k小整数
FilePath: P1138.py
'''


def func():
    n, k = map(int, input().strip().split())
    lst = list(map(int, input().strip().split()))
    lst = sorted(list(set(lst)))
    if len(lst) < k:
        print("NO RESULT")
    else:
        print(lst[k - 1])


if __name__ == '__main__':
    func()
