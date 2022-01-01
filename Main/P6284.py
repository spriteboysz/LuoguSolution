#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-23 22:33:28
LastEditTime: 2021-10-23 22:39:34
Description: Tarifa
FilePath: P6284.py
'''


def func():
    x = int(input())
    n = int(input())

    surplus = 0
    for _ in range(n):
        used = int(input())
        surplus = surplus + x - used

    print(surplus + x)


if __name__ == '__main__':
    func()
