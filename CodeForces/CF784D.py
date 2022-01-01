#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-21 15:41:19
LastEditTime: 2021-11-21 15:46:19
Description: Touchy-Feely Palindromes
FilePath: CF784D.py
'''


def func():
    base = ["23", "10", "30", "11", "13", "12", "31", "33", "32", "21"]
    s1 = input().strip()
    s2 = ""
    for item in s1:
        s2 += base[int(item)]
    print("Yes" if s2 == s2[::-1] else "No")


if __name__ == '__main__':
    func()
