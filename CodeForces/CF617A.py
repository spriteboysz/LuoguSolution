#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 13:29:54
LastEditTime: 2021-11-26 13:34:13
Description: Elephant
FilePath: CF617A.py
'''


def func():
    n = int(input())
    count = 0
    for i in range(5, 0, -1):
        div, mod = divmod(n, i)
        count += div
        n = mod
        if n == 0:
            break
    print(count)


if __name__ == '__main__':
    func()
