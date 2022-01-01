#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-06 23:03:22
LastEditTime: 2021-12-06 23:21:36
Description: 找筷子
FilePath: P1469.py
'''


def func():
    n = int(input())
    s = input().strip()
    length = 0
    num = ""
    for item in (s + " "):
        if item != " ":
            num += item
        else:
            length = length ^ int(num)
            num = ""
    print(length)


if __name__ == '__main__':
    func()
