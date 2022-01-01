#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-25 23:19:32
LastEditTime: 2021-11-25 23:20:43
Description: Prison Break
FilePath: CF1484A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().strip().split())
        print(a * b)


if __name__ == '__main__':
    func()
