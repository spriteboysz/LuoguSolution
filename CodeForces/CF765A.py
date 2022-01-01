#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-22 23:29:43
LastEditTime: 2021-11-22 23:31:44
Description: Neverending competitions
FilePath: CF765A.py
'''


def func():
    n = int(input())
    home = input().strip()
    for _ in range(n):
        a, b = input().strip().split("->")
    print("home" if n % 2 == 0 else "contest")


if __name__ == '__main__':
    func()
