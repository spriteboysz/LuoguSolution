#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-24 23:09:48
LastEditTime: 2021-11-24 23:12:32
Description: Special Permutation
FilePath: CF1454A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        base = [n]
        for i in range(1, n):
            base.append(i)
        print(" ".join(map(str, base)))


if __name__ == '__main__':
    func()
