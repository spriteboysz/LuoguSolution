#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-25 23:36:09
LastEditTime: 2021-11-25 23:41:35
Description: Three swimmers
FilePath: CF1492A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        p, a, b, c = map(int, input().strip().split())
        if p % a == 0 or p % b == 0 or p % c == 0:
            print(0)
        else:
            print(min(a - p % a, b - p % b, c - p % c))


if __name__ == '__main__':
    func()
