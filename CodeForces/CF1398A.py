#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-16 23:42:46
LastEditTime: 2021-11-16 23:50:00
Description: Bad Triangle
FilePath: CF1398A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        _ = int(input())
        lst = list(map(int, input().strip().split()))
        if lst[0] + lst[1] > lst[-1]:
            print(-1)
        else:
            print(1, 2, len(lst))


if __name__ == '__main__':
    func()
