#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-24 22:24:59
LastEditTime: 2021-11-24 22:35:25
Description: Wizard of Orz
FilePath: CF1467A.py
'''


def func():
    t = int(input())
    num = []
    for _ in range(t):
        num.append(int(input()))

    base = "989" + "0123456789" * (max(num) // 10 + 1)
    for item in num:
        print(base[0:item])


if __name__ == '__main__':
    func()
