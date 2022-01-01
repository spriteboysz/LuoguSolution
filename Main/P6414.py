#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 17:00:19
LastEditTime: 2021-10-24 17:22:57
Description: PROSJEK
FilePath: P6414.py
'''


def func():
    n = int(input())
    b = [0] + list(map(int, input().strip().split()))

    a = []
    total = 0
    for i in range(1, n + 1):
        a.append(i * b[i] - total)
        total = i * b[i]
    print(" ".join(map(str, a)))


if __name__ == '__main__':
    func()
