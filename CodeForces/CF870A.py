#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-08 23:22:54
LastEditTime: 2021-11-12 00:09:53
Description: Search for Pretty Integers
FilePath: CF870A.py
'''


def func():
    _, _ = map(int, input().strip().split())
    lst1 = set(map(int, input().strip().split()))
    lst2 = set(map(int, input().strip().split()))
    if len(lst1 & lst2) != 0:
        print(min(lst1 & lst2))
    else:
        a, b = sorted([min(lst1), min(lst2)])
        print(str(a) + str(b))


if __name__ == '__main__':
    func()
