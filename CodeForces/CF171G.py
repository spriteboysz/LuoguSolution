#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-29 23:43:18
LastEditTime: 2021-11-29 23:49:14
Description: Mysterious numbers - 2
FilePath: CF171G.py
'''


def func():
    a1, a2, k = map(int, input().strip().split())
    lst = [a1, a2]
    for i in range(2, k + 1):
        lst.append(lst[i - 1] + lst[i - 2])
    print(lst[-1])


if __name__ == '__main__':
    func()
