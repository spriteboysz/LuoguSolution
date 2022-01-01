#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-30 23:29:48
LastEditTime: 2021-12-04 21:54:39
Description: Two Substrings
FilePath: CF550A.py
'''


def func():
    s = input().strip()
    if "AB" in s:
        s = s.replace("AB", "ZZZ", 1)
        if "BA" in s:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


if __name__ == '__main__':
    func()
