#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 23:35:59
LastEditTime: 2021-11-05 23:49:19
Description: Little Pony and Crystal Mine
FilePath: CF454A.py
'''


def func():
    n = int(input())
    # *对称结构的处理
    for i in range(-n // 2 + 1, n // 2 + 1):
        print("*" * abs(i), end="")
        print("D" * ((n//2 - abs(i)) * 2 + 1), end="")
        print("*" * abs(i))


if __name__ == '__main__':
    func()
