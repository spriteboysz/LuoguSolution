#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-17 23:56:16
LastEditTime: 2021-11-17 23:59:25
Description: Permutation Forgery
FilePath: CF1405A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        _ = int(input())
        lst = input().strip().split()
        print(" ".join(lst[::-1]))


if __name__ == '__main__':
    func()
