#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-15 23:06:44
LastEditTime: 2021-11-15 23:21:52
Description: Ordinary Numbers
FilePath: CF1520B.py
'''


def func():
    t = int(input())
    for _ in range(t):
        num = input()
        if int(num) >= int(num[0] * len(num)):
            print(9 * (len(num) - 1) + int(num[0]))
        else:
            print(9 * (len(num) - 1) + int(num[0]) - 1)

if __name__ == '__main__':
    func()
