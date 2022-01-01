#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-17 22:45:41
LastEditTime: 2021-11-17 22:54:30
Description: Minimum Binary Number
FilePath: CF976A.py
'''


def func():
    _ = int(input())
    s = input().strip()
    if s == "0":
        print("0")
    else:
        print("1" + "0" * s.count("0"))


if __name__ == '__main__':
    func()
