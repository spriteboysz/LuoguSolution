#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-27 23:26:32
LastEditTime: 2021-10-27 23:29:20
Description: DOM
FilePath: P7583.py
'''


def func():
    s1 = input().strip()
    s2 = ""
    deletes = ["C", "A", "M", "B", "R", "I", "D", "G", "E"]
    for item in s1:
        if item not in deletes:
            s2 += item
    print(s2)


if __name__ == '__main__':
    func()
    