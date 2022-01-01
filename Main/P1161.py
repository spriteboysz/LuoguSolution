#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 09:20:06
LastEditTime: 2021-10-22 09:31:13
Description: 开灯
FilePath: P1161.py
'''


def func():
    n = int(input())

    lights, num = [False], 1
    for _ in range(n):
        a, t = map(float, input().strip().split())
        cur = int(a * t) + 1
        if cur > num:
            lights.extend([False] * (cur - num))
            num = cur
        for i in range(1, int(t) + 1):
            lights[int(a * i)] = not lights[int(a * i)]

    print(lights.index(True))


if __name__ == '__main__':
    func()
