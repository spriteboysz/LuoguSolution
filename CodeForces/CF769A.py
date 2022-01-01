#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 23:42:43
LastEditTime: 2021-11-19 23:44:15
Description: Year of University Entrance
FilePath: CF769A.py
'''


def func():
    n = int(input())
    year = list(sorted(map(int, input().strip().split())))
    print(year[n // 2])


if __name__ == '__main__':
    func()
