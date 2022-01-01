#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-18 23:00:22
LastEditTime: 2021-11-18 23:06:12
Description: Crunching Numbers Just for You
FilePath: CF784F.py
'''


def func():
    _, *lst = map(int, input().strip().strip().split())
    print(" ".join(map(str, sorted(lst))))


if __name__ == '__main__':
    func()
