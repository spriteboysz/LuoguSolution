#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 22:31:48
LastEditTime: 2021-11-19 22:54:36
Description: Check the string
FilePath: CF960A.py
'''


def func():
    s = input().strip()
    if s.rstrip("c").rstrip("b").rstrip("a") == "":
        if s.count("a") >= 1 and s.count("b") >= 1:
            if (s.count("c") == s.count("b") or s.count("c") == s.count("a")):
                return "YES"
    return "NO"


if __name__ == '__main__':
    ans = func()
    print(ans)
