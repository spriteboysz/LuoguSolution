#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-14 22:19:42
LastEditTime: 2021-11-14 22:44:50
Description: New Year's Number
FilePath: CF1475B.py
'''

def func():
    n = int(input())
    for _ in range(n):
        num = int(input())
        div, mod = divmod(num, 2020)
        if div >= mod:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    func()
    