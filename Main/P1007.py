#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-12 22:20:18
LastEditTime: 2021-12-12 22:48:04
Description: 独木桥
FilePath: P1007.py
'''


def bridge(lst, length):
    minimun, maximun = [], []
    for el in lst:
        if el < length / 2:
            minimun.append(el)
            maximun.append(length + 1 - el)
        else:
            minimun.append(length + 1 - el)
            maximun.append(el)
    return max(minimun), max(maximun)


def func():
    length = int(input())
    n = int(input())
    if n == 0:
        print(0, 0)
    else:
        position = list(map(int, input().strip().split()))
        print(" ".join(map(str, bridge(position, length))))


if __name__ == '__main__':
    func()
