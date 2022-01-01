#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-09 23:27:18
LastEditTime: 2021-11-09 23:30:54
Description: Minutes Before the New Year
FilePath: CF1283A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        hour, minitue = map(int, input().strip().split())
        print(24 * 60 - hour * 60 - minitue)


if __name__ == '__main__':
    func()
