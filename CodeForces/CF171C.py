#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-29 23:34:16
LastEditTime: 2021-11-29 23:36:05
Description: A Piece of Cake
FilePath: CF171C.py
'''


def func():
    n, *lst = map(int, input().strip().split())
    count = 0
    for i in range(n):
        count += lst[i] * (i + 1)
    print(count)


if __name__ == '__main__':
    func()
