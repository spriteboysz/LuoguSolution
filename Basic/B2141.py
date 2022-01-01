#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-10 22:39:49
LastEditTime: 2021-12-10 23:03:32
Description: 确定进制
FilePath: B2141.py
'''


def toDec(s, m):
    base = ["0", "1", "2", "3", "4", "5", "6", "7",
            "8", "9", "A", "B", "C", "D", "E", "F"]
    num = 0
    for i, el in enumerate(s):
        num += base.index(el) * m ** (len(s) - i - 1)
    return num


def func():
    p, q, r = input().strip().split()
    start = max(map(int, list(p + q + r))) + 1
    for i in range(start, 17):
        if toDec(p, i) * toDec(q, i) == toDec(r, i):
            print(i)
            break
    else:
        print(0)


if __name__ == '__main__':
    func()
