#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-11 23:41:40
LastEditTime: 2021-12-11 23:43:28
Description: PB的游戏1
FilePath: P3150.py
'''


def func():
    n = int(input())
    for _ in range(n):
        m = int(input())
        if m % 2 == 0:
            print("pb wins")
        else:
            print("zs wins")


if __name__ == '__main__':
    func()
