#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 17:15:32
LastEditTime: 2021-11-07 17:21:54
Description: King Moves
FilePath: CF710A.py
'''


def func():
    position = input().strip()
    if position in ["a1", "h1", "a8", "h8"]:
        print(3)
    elif position[0] in ["a", "h"] or position[1] in ["1", "8"]:
        print(5)
    else:
        print(8)


if __name__ == '__main__':
    func()
