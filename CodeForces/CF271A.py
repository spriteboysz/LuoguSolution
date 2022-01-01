#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-12 22:40:15
LastEditTime: 2021-11-12 22:50:02
Description: Beautiful Year
FilePath: CF271A.py
'''


def func():
    n = int(input())
    for year in range(n + 1, 9999):
        if len(set(str(year))) == 4:
            return year


if __name__ == '__main__':
    ans = func()
    print(ans)
    