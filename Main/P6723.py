#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 15:54:45
LastEditTime: 2021-10-24 16:04:05
Description: ZAMKA
FilePath: P6723.py
'''


def func():
    l, d, x = int(input()), int(input()), int(input())
    for i in range(l, d + 1):
        if x == sum(map(int, list(str(i)))):
            n = i
            break
    print(n)

    for i in range(d, l - 1, -1):
        if x == sum(map(int, list(str(i)))):
            m = i
            break
    print(m)


if __name__ == '__main__':
    func()
