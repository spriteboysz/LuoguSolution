#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-20 21:56:34
LastEditTime: 2021-10-20 22:09:11
Description: 输出亲朋字符串
FilePath: B2113.py
'''


def func():
    s1 = input().strip()
    s1 += s1[0:1]

    s2 = ""
    for i in range(len(s1) - 1):
        s2 += chr(ord(s1[i]) + ord(s1[i + 1]))
    print(s2)


if __name__ == '__main__':
    func()
