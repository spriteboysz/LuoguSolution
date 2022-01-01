#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 23:27:30
LastEditTime: 2021-11-19 23:30:38
Description: Div64
FilePath: CF887A.py
'''


def func():
    s = input().strip().lstrip("0")
    print("yes" if s.count("0") >= 6 else "no")


if __name__ == '__main__':
    func()
