#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-21 22:51:58
LastEditTime: 2021-11-21 23:00:17
Description: Tanya and Stairways
FilePath: CF1005A.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    stairway = []
    for i in range(1, n):
        if lst[i] <= lst[i - 1]:
            stairway.append(lst[i - 1])
    stairway.append(lst[-1])
    print(len(stairway))
    print(" ".join(map(str, stairway)))


if __name__ == '__main__':
    func()
