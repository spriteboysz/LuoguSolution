#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-11 23:09:08
LastEditTime: 2021-11-11 23:12:52
Description: Display The Number
FilePath: CF1295A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        num = int(input())
        if num % 2 == 0:
            print("1" * (num // 2))
        else:
            print("7" + "1" * (num // 2 - 1))


if __name__ == '__main__':
    func()
