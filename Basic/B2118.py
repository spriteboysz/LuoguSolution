#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-20 22:53:48
LastEditTime: 2021-10-20 23:09:17
Description: 验证子串
FilePath: B2118.py
'''


def func():
    s1 = input().strip()
    s2 = input().strip()

    if s1.find(s2) != -1:
        print("{1} is substring of {0}".format(s1, s2))
    elif s2.find(s1) != -1:
        print("{} is substring of {}".format(s1, s2))
    else:
        print("No substring")


if __name__ == '__main__':
    func()
    