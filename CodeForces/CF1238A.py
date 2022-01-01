#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 14:37:31
LastEditTime: 2021-11-20 14:39:39
Description: Prime Subtraction
FilePath: CF1238A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().strip().split())
        print("NO" if a - b == 1 else "YES")


if __name__ == '__main__':
    func()
