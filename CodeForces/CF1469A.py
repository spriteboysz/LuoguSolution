#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-24 22:20:04
LastEditTime: 2021-11-24 22:23:37
Description: Regular Bracket Sequence
FilePath: CF1469A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        s = input().strip()
        if len(s) % 2 == 0 and not s.startswith(")") and not s.endswith("("):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    func()
