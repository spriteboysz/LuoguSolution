#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 21:56:55
LastEditTime: 2021-10-22 21:59:13
Description: Modulo
FilePath: P4325.py
'''


def func():
    lst = [0] * 42
    for _ in range(10):
        num = int(input())
        lst[num % 42] += 1
    print(42 - lst.count(0))


if __name__ == '__main__':
    func()
