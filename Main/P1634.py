#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 22:53:10
LastEditTime: 2021-10-24 22:55:46
Description: 禽兽的传染病
FilePath: P1634.py
'''


def func():
    x, n = map(int, input().strip().split())

    total = 1
    for _ in range(n):
        total += total * x
    print(total)


if __name__ == '__main__':
    func()
