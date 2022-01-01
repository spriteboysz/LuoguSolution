#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 21:40:49
LastEditTime: 2021-10-22 21:42:57
Description: Even? Odd? G
FilePath: P2955.py
'''


def func():
    n = int(input())
    for _ in range(n):
        num = int(input())
        if num % 2 == 0:
            print("even")
        else:
            print("odd")


if __name__ == '__main__':
    func()
