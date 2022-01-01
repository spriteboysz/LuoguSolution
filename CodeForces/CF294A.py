#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-04 22:04:39
LastEditTime: 2021-12-04 22:18:17
Description: Shaass and Oskols
FilePath: CF294A.py
'''


def func():
    n = int(input())
    birds = list(map(int, input().strip().split()))
    m = int(input())
    for _ in range(m):
        x, y = map(int, input().strip().split())
        if x - 1 - 1 >= 0:
            birds[x - 1 - 1] += y - 1
        if x - 1 + 1 <= n - 1:
            birds[x - 1 + 1] += birds[x - 1] - y
        birds[x - 1] = 0

    print("\n".join(map(str, birds)))


if __name__ == '__main__':
    func()
