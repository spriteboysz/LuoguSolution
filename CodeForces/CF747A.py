#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 13:35:48
LastEditTime: 2021-11-26 13:37:56
Description: Display Size
FilePath: CF747A.py
'''


def func():
    n = int(input())
    for a in range(int(n ** 0.5), 0, -1):
        if n % a == 0:
            print(a, n // a)
            break


if __name__ == '__main__':
    func()
