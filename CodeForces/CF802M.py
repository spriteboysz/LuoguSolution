#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-24 23:46:53
LastEditTime: 2021-11-24 23:48:39
Description: April Fools' Problem (easy)
FilePath: CF802M.py
'''


def func():
    n, k = map(int, input().strip().split())
    lst = sorted(map(int, input().strip().split()))
    print(sum(lst[:k]))


if __name__ == '__main__':
    func()
    