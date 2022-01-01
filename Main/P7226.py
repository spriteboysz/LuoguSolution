#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 17:43:16
LastEditTime: 2021-10-24 17:46:29
Description: POT
FilePath: P7226.py
'''


def func():
    n = int(input())

    total = 0
    for _ in range(n):
        q = input().strip()
        total += int(q[:-1]) ** int(q[-1])
    print(total)


if __name__ == '__main__':
    func()
