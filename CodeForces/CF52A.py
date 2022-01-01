#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-03 22:50:53
LastEditTime: 2021-11-03 22:59:51
Description: 123-sequence
FilePath: CF52A.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    # func-1
    # max = 0
    # for i in range(1, 4):
    #     if max < lst.count(i):
    #         max = lst.count(i)
    # return n - max

    # func-2
    most = max(map(lambda i: lst.count(i), [1, 2, 3]))
    return n - most


if __name__ == '__main__':
    ans = func()
    print(ans)
