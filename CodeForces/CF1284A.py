#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-11 23:23:26
LastEditTime: 2021-11-11 23:28:51
Description: New Year and Naming
FilePath: CF1284A.py
'''


def func():
    n, m = map(int, input().strip().split())
    s = input().strip().split()
    t = input().strip().split()
    q = int(input())
    for _ in range(q):
        year = int(input())
        print(s[year % n - 1] + t[year % m - 1])


if __name__ == '__main__':
    func()
