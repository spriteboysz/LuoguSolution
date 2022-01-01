#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-17 23:04:16
LastEditTime: 2021-11-17 23:07:36
Description: Game
FilePath: CF984A.py
'''


def func():
    n = int(input())
    lst = list(sorted(map(int, input().strip().split())))

    if len(lst) % 2 == 0:
        print(lst[len(lst) // 2 - 1])
    else:
        print(lst[len(lst) // 2])


if __name__ == '__main__':
    func()
