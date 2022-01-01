#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 21:09:55
LastEditTime: 2021-12-26 23:33:58
Description: 失踪的7
FilePath: P1590.py
'''


def func():
    t = int(input())
    for _ in range(t):
        num = input().strip()
        n = 0
        for i in range(len(num)):
            n += int(num[i]) * (9 ** (len(num) - i - 1))
        print(n)
        print(1 * 9 ** 4 + 8 * 9 ** 3 + 8 * 9 ** 2 + 9 * 9)


if __name__ == '__main__':
    func()
