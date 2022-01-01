#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 00:03:08
LastEditTime: 2021-11-19 00:07:15
Description: In-game Chat
FilePath: CF1411A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        print("YES" if 2 * len(s.rstrip(")")) < n else "NO")


if __name__ == '__main__':
    func()
