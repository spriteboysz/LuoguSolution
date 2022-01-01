#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-07 23:28:17
LastEditTime: 2021-12-07 23:53:22
Description: 单词覆盖还原
FilePath: P1321.py
'''


def func():
    s = input().strip()
    length = len(s)
    s += "." * 4
    boy, girl = 0, 0
    for i in range(length):
        if s[i] == "b" or s[i + 1] == "o" or s[i + 2] == "y":
            boy += 1
        if s[i] == "g" or s[i + 1] == "i" or s[i + 2] == "r" or s[i + 3] == "l":
            girl += 1
    print("\n".join(map(str, [boy, girl])))


if __name__ == '__main__':
    func()
