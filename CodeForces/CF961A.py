#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 22:56:48
LastEditTime: 2021-11-19 23:01:53
Description: Tetris
FilePath: CF961A.py
'''


def func():
    n, _ = map(int, input().strip().split())
    lst = list(map(int, input().strip().split()))
    count = [0] * n
    for item in lst:
        if 1 <= item <= n:
            count[item - 1] += 1
    print(min(count))


if __name__ == '__main__':
    func()
    