#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 22:48:34
LastEditTime: 2021-11-22 00:03:01
Description: Next Test
FilePath: CF27A.py
'''


def func():
    n = int(input())
    if n == 0:
        print(0)
        return
    lst = list(sorted(map(int, input().strip().split())))
    for i in range(n):
        if i + 1 != lst[i]:
            print(i + 1)
            break
    else:
        print(n + 1)


if __name__ == '__main__':
    func()