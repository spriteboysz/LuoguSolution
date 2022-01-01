#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 16:51:44
LastEditTime: 2021-10-24 16:55:27
Description: TRIK
FilePath: P6461.py
'''


def func():
    operator = input().strip()
    lst = [1, 0, 0]
    for item in operator:
        if item == "A":
            lst[0], lst[1] = lst[1], lst[0]
        elif item == "B":
            lst[1], lst[2] = lst[2], lst[1]
        elif item == "C":
            lst[0], lst[2] = lst[2], lst[0]
    print(lst.index(1) + 1)


if __name__ == '__main__':
    func()
