#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 13:53:20
LastEditTime: 2021-11-26 14:09:23
Description: Watering System
FilePath: CF967B.py
'''


def func():
    n, a, b = map(int, input().strip().split())
    s1, *s = map(int, input().strip().split())
    s = sorted(s)
    closed = 0
    while a * s1 / (s1 + sum(s[:(n - 1 - closed)])) < b:
        closed += 1
    print(closed)


if __name__ == '__main__':
    func()
