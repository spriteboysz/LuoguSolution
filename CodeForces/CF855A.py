#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-08 23:45:46
LastEditTime: 2021-11-08 23:47:43
Description: Tom Riddle's Diary
FilePath: CF855A.py
'''


def func():
    n = int(input())
    names = []
    for _ in range(n):
        name = input().strip()
        if name in names:
            print("YES")
        else:
            names.append(name)
            print("NO")


if __name__ == '__main__':
    func()
