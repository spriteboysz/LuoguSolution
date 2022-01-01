#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-06 14:54:29
LastEditTime: 2021-11-06 14:58:43
Description: Game
FilePath: CF513A.py
'''


def func():
    n1, n2, k1, k2 = map(int, input().strip().split())
    print("First" if n1 > n2 else "Second")


if __name__ == '__main__':
    func()
