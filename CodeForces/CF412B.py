#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-04 23:03:02
LastEditTime: 2021-11-04 23:06:43
Description: 
FilePath: CF412B.py
'''


def func():
    n, k = map(int, input().strip().split())
    lst = list(sorted(map(int, input().strip().split())))
    return lst[-k]


if __name__ == '__main__':
    ans = func()
    print(ans)
