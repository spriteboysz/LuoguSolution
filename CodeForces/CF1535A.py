#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-15 23:33:54
LastEditTime: 2021-11-15 23:36:07
Description: Fair Playoff
FilePath: CF1535A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        a, b, c, d = map(int, input().strip().split())
        if max(a, b) < min(c, d) or min(a, b) > max(c, d):
            print("NO")
        else:
            print("YES")


if __name__ == '__main__':
    func()
