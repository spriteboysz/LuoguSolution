#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 14:35:47
LastEditTime: 2021-11-26 14:38:33
Description: Palindromic Supersequence
FilePath: CF932A.py
'''


def func():
    s = input().strip()
    if s == s[::-1]:
        print(s)
    else:
        print(s + s[::-1])


if __name__ == '__main__':
    func()
