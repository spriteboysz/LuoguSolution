#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-17 22:59:52
LastEditTime: 2021-11-17 23:03:09
Description: Antipalindrome
FilePath: CF981A.py
'''


def func():
    s = input().strip()
    if len(set(list(s))) == 1:
        print(0)
    elif s == s[::-1]:
        print(len(s) - 1)
    else:
        print(len(s))


if __name__ == '__main__':
    func()
