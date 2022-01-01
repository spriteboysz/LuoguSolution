#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-15 22:58:51
LastEditTime: 2021-11-15 23:02:07
Description: Average Height
FilePath: CF1509A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        _ = int(input())
        lst = map(int, input().strip().split())
        lst = sorted(lst, key=lambda el: el % 2)
        print(" ".join(map(str, lst)))


if __name__ == '__main__':
    func()
