#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-23 22:57:58
LastEditTime: 2021-11-23 23:00:01
Description: FashionabLee
FilePath: CF1369A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        side = int(input())
        if side % 4 == 0:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    func()
