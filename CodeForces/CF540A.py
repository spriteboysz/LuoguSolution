#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-30 23:22:57
LastEditTime: 2021-11-30 23:28:22
Description: Combination Lock
FilePath: CF540A.py
'''


def func():
    _ = int(input())
    original = list(map(int, list(input().strip())))
    password = list(map(int, list(input().strip())))
    count = 0
    for i, j in zip(original, password):
        count += min(abs(i - j), 10 - abs(i - j))
    print(count)


if __name__ == '__main__':
    func()
