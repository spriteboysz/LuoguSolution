#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 22:18:11
Description: 开关灯
FilePath: B2092.py
'''


def func():
    n = int(input())
    lights = [True] * (n + 1)

    for person in range(1, n + 1):
        for light in range(1, n + 1):
            if light % person == 0:
                lights[light] = not lights[light]

    turnoff = []
    for i in range(1, n + 1):
        if lights[i] == False:
            turnoff.append(str(i))

    print(" ".join(turnoff))


if __name__ == '__main__':
    func()
