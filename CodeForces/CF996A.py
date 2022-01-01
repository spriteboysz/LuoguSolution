#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-15 23:47:09
LastEditTime: 2021-11-15 23:51:43
Description: Hit the Lottery
FilePath: CF996A.py
'''


def func():
    num = int(input())
    count = 0
    for item in [100, 20, 10, 5, 1]:
        div, mod = divmod(num, item)
        num = mod
        count += div
    print(count)


if __name__ == '__main__':
    func()
