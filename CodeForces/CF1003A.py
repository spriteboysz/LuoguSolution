#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-15 23:54:48
LastEditTime: 2021-11-16 00:00:12
Description: Polycarp's Pockets
FilePath: CF1003A.py
'''


def func():
    _ = int(input())
    lst = list(map(int, input().strip().split()))
    maximum = 0
    for item in set(lst):
        count = lst.count(item)
        if maximum < count:
            maximum = count
    print(maximum)


if __name__ == '__main__':
    func()
