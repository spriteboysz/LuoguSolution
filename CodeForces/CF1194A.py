#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 14:20:01
LastEditTime: 2021-11-20 14:21:23
Description: Remove a Progression
FilePath: CF1194A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().strip().split())
        print(2 * x)


if __name__ == '__main__':
    func()
