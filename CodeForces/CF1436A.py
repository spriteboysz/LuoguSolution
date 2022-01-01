#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-24 23:23:16
LastEditTime: 2021-11-24 23:25:52
Description: Reorder
FilePath: CF1436A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().strip().split())
        lst = sum(map(int, input().strip().split()))
        print("YES" if lst == m else "NO")


if __name__ == '__main__':
    func()
