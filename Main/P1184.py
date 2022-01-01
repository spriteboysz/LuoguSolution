#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-17 22:04:05
LastEditTime: 2021-12-18 13:45:24
Description: 高手之在一起
FilePath: P1184.py
'''


def func():
    n, m = map(int, input().split())
    place = []
    for _ in range(n):
        w = input()
        place.append(w)

    count = 0
    for _ in range(m):
        go = input()
        if go in place:
            count += 1
    print(1 if m == 1 and n == 1 else count)


if __name__ == '__main__':
    func()
