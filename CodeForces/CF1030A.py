#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 23:59:54
LastEditTime: 2021-11-20 00:01:58
Description: In Search of an Easy Problem
FilePath: CF1030A.py
'''


def func():
    n = int(input())
    lst = input().strip().split()
    print("EASY" if lst.count("0") == n else "HARD")


if __name__ == '__main__':
    func()
