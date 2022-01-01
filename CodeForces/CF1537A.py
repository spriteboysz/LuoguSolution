#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 22:27:36
LastEditTime: 2021-11-26 22:30:37
Description: Arithmetic Array
FilePath: CF1537A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().strip().split()))
        if sum(lst) >= n:
            print(sum(lst) - n)
        else:
            print(1)


if __name__ == '__main__':
    func()
