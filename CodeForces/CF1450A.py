#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-24 23:15:28
LastEditTime: 2021-11-24 23:17:07
Description: Avoid Trygub
FilePath: CF1450A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        print("".join(sorted(s)))


if __name__ == '__main__':
    func()
