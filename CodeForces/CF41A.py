#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-03 23:44:43
LastEditTime: 2021-11-03 23:46:58
Description: Translation
FilePath: CF41A.py
'''


def func():
    s1, s2 = input().strip(), input().strip()
    return "YES" if s1[::-1] == s2 else "NO"


if __name__ == '__main__':
    ans = func()
    print(ans)
