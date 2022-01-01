#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 22:58:00
LastEditTime: 2021-11-07 23:21:07
Description: Second Order Statistics
FilePath: CF22A.py
'''


def func():
    _ = int(input())
    lst = set(map(int, input().strip().split()))
    if len(lst) < 2:
        print("NO")
    else:
        minimum = min(lst)
        print(min(lst - set([minimum])))


if __name__ == '__main__':
    func()
