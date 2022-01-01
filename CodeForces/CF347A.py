#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-01 23:19:35
LastEditTime: 2021-12-01 23:23:51
Description: Difference Row
FilePath: CF347A.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    maximum, minimum = max(lst), min(lst)
    lst.remove(maximum)
    lst.remove(minimum)
    lst = list(sorted(lst))
    print(maximum, " ".join(map(str, lst)), minimum)


if __name__ == '__main__':
    func()
