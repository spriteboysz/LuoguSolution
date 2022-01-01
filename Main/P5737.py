#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 21:34:57
LastEditTime: 2021-10-10 21:41:43
Description: 闰年展示
FilePath: P5737.py
'''


def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def func():
    x, y = map(int, input().strip().split())
    lst = []
    for year in range(x, y + 1):
        if isLeap(year):
            lst.append(str(year))

    print(len(lst))
    print(" ".join(lst))


if __name__ == '__main__':
    func()
